#!/usr/bin/env node
// conclave-usage-mcp — stdio MCP server for token budget awareness
// stdout is reserved for JSON-RPC. All debug output goes to stderr.

'use strict';

const fs = require('fs');
const path = require('path');
const os = require('os');
const readline = require('readline');

const CLAUDE_DIR = path.join(os.homedir(), '.claude');

// Find the most recently updated session file in ~/.claude/sessions/
function findActiveSession() {
  const sessionsDir = path.join(CLAUDE_DIR, 'sessions');
  if (!fs.existsSync(sessionsDir)) return null;

  const entries = fs.readdirSync(sessionsDir)
    .filter(f => f.endsWith('.json'))
    .map(f => {
      const full = path.join(sessionsDir, f);
      return { full, mtime: fs.statSync(full).mtimeMs };
    })
    .sort((a, b) => b.mtime - a.mtime);

  if (!entries.length) return null;

  try {
    return JSON.parse(fs.readFileSync(entries[0].full, 'utf8'));
  } catch {
    return null;
  }
}

// Derive ~/.claude/projects/ directory name from a cwd path.
// Claude Code encodes: each ':', '\', '/', and ' ' → '-'
// Example: 'C:\Users\WINDOWS 10 LITE' → 'C--Users-WINDOWS-10-LITE'
function cwdToProjectDir(cwd) {
  return (cwd || '').replace(/[:\\/\s]/g, '-');
}

// Read PLAN_LIMIT from the installed Conclave system document.
// Prefer ~/.claude/CONCLAVE_SYSTEM.md for backward compatibility,
// then fall back to ~/.claude/docs/CONCLAVE_SYSTEM.md, which is where
// the installer copies the file today. Falls back to 44000 otherwise.
function findPlanConfigPath() {
  const candidates = [
    path.join(CLAUDE_DIR, 'CONCLAVE_SYSTEM.md'),
    path.join(CLAUDE_DIR, 'docs', 'CONCLAVE_SYSTEM.md')
  ];

  return candidates.find((candidate) => fs.existsSync(candidate)) || null;
}

function readPlanLimit() {
  const docPath = findPlanConfigPath();
  if (!docPath) return 44000;

  try {
    const content = fs.readFileSync(docPath, 'utf8');
    const m = content.match(/PLAN_LIMIT[:\s]+(\d+)/);
    return m ? parseInt(m[1], 10) : 44000;
  } catch {
    return 44000;
  }
}

// Sum all token fields from a session JSONL file.
// Token data is nested at line.message.usage.*
// Only counts tokens from the last 5 hours (billing window resets every 5h).
function sumTokensFromJsonl(jsonlPath) {
  if (!fs.existsSync(jsonlPath)) return 0;

  const windowStart = Date.now() - 5 * 60 * 60 * 1000; // 5 hours ago
  let total = 0;
  const lines = fs.readFileSync(jsonlPath, 'utf8').split('\n');

  for (const line of lines) {
    if (!line.trim()) continue;
    try {
      const obj = JSON.parse(line);
      const u = obj?.message?.usage;
      if (!u) continue;

      // Filter to billing window: only count messages from last 5 hours
      const ts = obj.timestamp ? new Date(obj.timestamp).getTime() : 0;
      if (ts < windowStart) continue;

      total += (u.input_tokens || 0)
             + (u.output_tokens || 0)
             + (u.cache_creation_input_tokens || 0)
             + (u.cache_read_input_tokens || 0);
    } catch { /* skip malformed lines */ }
  }

  return total;
}

function getUsage() {
  const session = findActiveSession();
  if (!session || !session.sessionId) {
    return {
      error: 'No active session found in ~/.claude/sessions/',
      tokens_used: 0,
      plan_limit: readPlanLimit(),
      percent_used: 0,
      recommendation: 'parallel'
    };
  }

  const { sessionId, cwd } = session;
  const projectDir = cwdToProjectDir(cwd);
  const jsonlPath = path.join(CLAUDE_DIR, 'projects', projectDir, `${sessionId}.jsonl`);

  const tokens_used = sumTokensFromJsonl(jsonlPath);
  const plan_limit = readPlanLimit();
  const percent_used = plan_limit > 0 ? Math.round((tokens_used / plan_limit) * 100) : 0;

  let recommendation;
  if (percent_used < 50) recommendation = 'parallel';
  else if (percent_used < 70) recommendation = 'sequential';
  else if (percent_used < 85) recommendation = 'sequential_warn';
  else recommendation = 'pause';

  return {
    tokens_used,
    plan_limit,
    percent_used,
    recommendation,
    session_id: sessionId,
    project: projectDir
  };
}

// ── JSON-RPC over stdio ───────────────────────────────────────────────────────

function send(obj) {
  process.stdout.write(JSON.stringify(obj) + '\n');
}

function handleMessage(msg) {
  const { id, method, params } = msg;

  switch (method) {
    case 'initialize':
      send({
        jsonrpc: '2.0', id,
        result: {
          protocolVersion: '2024-11-05',
          capabilities: { tools: {} },
          serverInfo: { name: 'conclave-usage-mcp', version: '1.0.0' }
        }
      });
      break;

    case 'notifications/initialized':
      break; // notification — no response

    case 'tools/list':
      send({
        jsonrpc: '2.0', id,
        result: {
          tools: [{
            name: 'usage/current',
            description: 'Returns token budget for the active Claude Code session. Call before deciding parallel vs sequential agent activation. Returns: tokens_used, plan_limit, percent_used, recommendation (parallel|sequential|sequential_warn|pause).',
            inputSchema: { type: 'object', properties: {} }
          }]
        }
      });
      break;

    case 'tools/call':
      if (params?.name === 'usage/current') {
        const result = getUsage();
        send({
          jsonrpc: '2.0', id,
          result: { content: [{ type: 'text', text: JSON.stringify(result, null, 2) }] }
        });
      } else {
        send({
          jsonrpc: '2.0', id,
          error: { code: -32601, message: `Unknown tool: ${params?.name}` }
        });
      }
      break;

    default:
      if (id !== undefined) {
        send({
          jsonrpc: '2.0', id,
          error: { code: -32601, message: 'Method not found' }
        });
      }
  }
}

// Read line-delimited JSON-RPC from stdin
const rl = readline.createInterface({ input: process.stdin, terminal: false });
let buffer = '';

rl.on('line', (line) => {
  buffer += line;
  try {
    const msg = JSON.parse(buffer);
    buffer = '';
    handleMessage(msg);
  } catch {
    // Message spans multiple lines — accumulate
  }
});

rl.on('close', () => process.exit(0));
