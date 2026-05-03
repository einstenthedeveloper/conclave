#!/usr/bin/env node
/**
 * Conclave install script — runs as npm/pnpm postinstall.
 *
 * Steps:
 *   1. Copy agents/, commands/, docs/, knowledge/, templates/, mcp/ to ~/.claude/
 *   2. Non-destructively merge mcpServers into ~/.claude/settings.json (preserve user entries)
 *   3. Atomic write of settings.json (tmp + rename)
 *   4. Copy templates/ROLES stubs to cwd (skip if exist)
 *   5. Report what was added/skipped
 *
 * Safety guarantees:
 *   - Existing user mcpServers entries are NEVER overwritten
 *   - settings.json is written atomically (tmp + rename) — partial writes impossible
 *   - All copies are file-by-file (no rm -rf of user dirs)
 *   - Pre-existing files in ~/.claude/ subdirs are overwritten only for files we ship
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

const PACKAGE_ROOT = __dirname;
const CLAUDE_DIR = path.join(os.homedir(), '.claude');
const SETTINGS_PATH = path.join(CLAUDE_DIR, 'settings.json');

// Directories to copy from package → ~/.claude/ (recursive, file-by-file)
const COPY_DIRS = ['agents', 'commands', 'docs', 'knowledge', 'mcp'];

// In-house MCPs to register on install (non-destructive)
const NEW_MCPS = {
  'conclave-usage': {
    command: 'node',
    args: [path.join(CLAUDE_DIR, 'mcp', 'usage', 'src', 'index.js')]
  },
  'conclave-interface': {
    command: 'python',
    args: [path.join(CLAUDE_DIR, 'mcp', 'interface-controller', 'server.py')]
  }
};

function copyDirRecursive(src, dst) {
  if (!fs.existsSync(src)) return 0;
  fs.mkdirSync(dst, { recursive: true });
  let count = 0;
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    if (entry.name === '__pycache__' || entry.name === 'node_modules' || entry.name.endsWith('.pyc')) {
      continue;
    }
    const sp = path.join(src, entry.name);
    const dp = path.join(dst, entry.name);
    if (entry.isDirectory()) {
      count += copyDirRecursive(sp, dp);
    } else if (entry.isFile()) {
      fs.copyFileSync(sp, dp);
      count++;
    }
  }
  return count;
}

function readSettingsSafe() {
  try {
    const raw = fs.readFileSync(SETTINGS_PATH, 'utf8');
    return JSON.parse(raw);
  } catch (err) {
    if (err.code === 'ENOENT') return {};
    if (err instanceof SyntaxError) {
      const backup = SETTINGS_PATH + '.corrupt-' + Date.now();
      console.error(`  ! ${SETTINGS_PATH} is invalid JSON; backing up to ${backup}`);
      fs.copyFileSync(SETTINGS_PATH, backup);
      return {};
    }
    throw err;
  }
}

function writeSettingsAtomic(settings) {
  const tmp = SETTINGS_PATH + '.tmp.' + process.pid;
  fs.writeFileSync(tmp, JSON.stringify(settings, null, 2) + '\n');
  fs.renameSync(tmp, SETTINGS_PATH);
}

function copyTemplatesAndRolesToCwd() {
  // Templates copied to cwd as starter docs (skip if exist)
  const tplSrc = path.join(PACKAGE_ROOT, 'templates');
  if (fs.existsSync(tplSrc)) {
    for (const file of fs.readdirSync(tplSrc)) {
      const dst = path.join(process.cwd(), file);
      if (!fs.existsSync(dst)) {
        fs.copyFileSync(path.join(tplSrc, file), dst);
        console.log(`  + templates/${file} → cwd`);
      }
    }
  }
  // ROLES stubs (HR meta-files) to cwd ROLES/
  const rolesCwd = path.join(process.cwd(), 'ROLES');
  fs.mkdirSync(rolesCwd, { recursive: true });
  for (const file of ['_SCHEMA.md', '_HR_INDEX.md']) {
    const src = path.join(PACKAGE_ROOT, 'ROLES', file);
    const dst = path.join(rolesCwd, file);
    if (fs.existsSync(src) && !fs.existsSync(dst)) {
      fs.copyFileSync(src, dst);
      console.log(`  + ROLES/${file} → cwd`);
    }
  }
}

function main() {
  const pkgVersion = require('./package.json').version;
  console.log(`Conclave installer v${pkgVersion} — copying package into ~/.claude/`);

  // 1. Ensure ~/.claude/ exists
  fs.mkdirSync(CLAUDE_DIR, { recursive: true });

  // 2. Copy each shipped directory
  let totalFiles = 0;
  for (const dir of COPY_DIRS) {
    const src = path.join(PACKAGE_ROOT, dir);
    const dst = path.join(CLAUDE_DIR, dir);
    const count = copyDirRecursive(src, dst);
    if (count > 0) console.log(`  ✓ ${dir}/ → ${count} file(s)`);
  }

  // 3. Non-destructive merge of mcpServers
  const settings = readSettingsSafe();
  settings.mcpServers = settings.mcpServers || {};

  let added = 0;
  let skipped = 0;
  for (const [key, config] of Object.entries(NEW_MCPS)) {
    if (settings.mcpServers[key]) {
      console.log(`  - ${key}: already registered (preserving user config)`);
      skipped++;
    } else {
      settings.mcpServers[key] = config;
      console.log(`  + ${key}: registered → ${config.command} ${path.basename(config.args[0])}`);
      added++;
    }
  }

  // 4. Atomic write of settings
  writeSettingsAtomic(settings);

  // 5. Copy templates + ROLES stubs to cwd (project bootstrap)
  copyTemplatesAndRolesToCwd();

  console.log('');
  console.log(`✓ Conclave v${pkgVersion} installed: ${added} mcpServer(s) added, ${skipped} preserved`);
  console.log('');
  console.log('Next steps:');
  console.log('  1. Set PLAN_LIMIT in ~/.claude/docs/CONCLAVE_SYSTEM.md (Pro=44000, Max5=88000, Max20=220000)');
  console.log('  2. Restart Claude Code session (mcpServers need reload)');
  console.log('  3. Open a project directory and run: /conc');
  console.log('     → Chairman intake → VISION.md → /ceo → EXECUTION_PLAN.md → C-levels');
}

try {
  main();
} catch (err) {
  console.error('✗ Conclave install failed:', err.message);
  console.error(err.stack);
  process.exit(1);
}
