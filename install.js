const fs = require('fs');
const path = require('path');
const os = require('os');

try {
  const claudeDir = path.join(os.homedir(), '.claude');
  const agentsDir = path.join(claudeDir, 'agents');
  const commandsDir = path.join(claudeDir, 'commands');
  const skillsDir = path.join(commandsDir, 'skills');
  const knowledgeDir = path.join(claudeDir, 'knowledge');
  const pkgDir = __dirname;

  // Ensure directories
  for (const dir of [agentsDir, commandsDir, skillsDir, knowledgeDir]) {
    fs.mkdirSync(dir, { recursive: true });
  }
  console.log(`✓ Ensured ~/.claude/agents/`);
  console.log(`✓ Ensured ~/.claude/commands/skills/`);
  console.log(`✓ Ensured ~/.claude/knowledge/`);

  // Copy agents/
  for (const file of fs.readdirSync(path.join(pkgDir, 'agents'))) {
    const src = path.join(pkgDir, 'agents', file);
    if (fs.statSync(src).isFile()) {
      fs.copyFileSync(src, path.join(agentsDir, file));
      console.log(`✓ agents/${file}`);
    }
  }

  // Copy commands/ (top-level .md files — conc.md, ceo.md, conclave.md)
  for (const file of fs.readdirSync(path.join(pkgDir, 'commands'))) {
    const src = path.join(pkgDir, 'commands', file);
    if (fs.statSync(src).isFile()) {
      fs.copyFileSync(src, path.join(commandsDir, file));
      console.log(`✓ commands/${file}`);
    }
  }

  // Copy commands/skills/ library
  const srcSkillsDir = path.join(pkgDir, 'commands', 'skills');
  if (fs.existsSync(srcSkillsDir)) {
    for (const file of fs.readdirSync(srcSkillsDir)) {
      const src = path.join(srcSkillsDir, file);
      if (fs.statSync(src).isFile()) {
        fs.copyFileSync(src, path.join(skillsDir, file));
        console.log(`✓ skills/${file}`);
      }
    }
  }

  // Copy conclave-usage-mcp to ~/.claude/conclave-usage-mcp/
  const mcpSrc = path.join(pkgDir, 'conclave-usage-mcp');
  const mcpDest = path.join(claudeDir, 'conclave-usage-mcp');
  if (fs.existsSync(mcpSrc)) {
    copyDirRecursive(mcpSrc, mcpDest);
    console.log(`✓ conclave-usage-mcp → ${mcpDest}`);
  }

  // Copy knowledge/ library to ~/.claude/knowledge/
  const knowledgeSrc = path.join(pkgDir, 'knowledge');
  if (fs.existsSync(knowledgeSrc)) {
    for (const file of fs.readdirSync(knowledgeSrc)) {
      const src = path.join(knowledgeSrc, file);
      if (fs.statSync(src).isFile()) {
        fs.copyFileSync(src, path.join(knowledgeDir, file));
        console.log(`✓ knowledge/${file}`);
      }
    }
  }

  // Copy system docs to ~/.claude/
  for (const doc of ['ARCHITECTURE.md', 'ORCHESTRATION.md', 'CONCLAVE_SYSTEM.md']) {
    fs.copyFileSync(path.join(pkgDir, doc), path.join(claudeDir, doc));
    console.log(`✓ ${doc}`);
  }

  // Copy templates to cwd (skip existing)
  const templateSrc = path.join(pkgDir, 'templates');
  if (fs.existsSync(templateSrc)) {
    for (const file of fs.readdirSync(templateSrc)) {
      const dest = path.join(process.cwd(), file);
      if (!fs.existsSync(dest)) {
        fs.copyFileSync(path.join(templateSrc, file), dest);
        console.log(`✓ templates/${file} → cwd`);
      } else {
        console.log(`  (skipped — exists) ${file}`);
      }
    }
  }

  // Copy ROLES templates (skip existing)
  const rolesDir = path.join(process.cwd(), 'ROLES');
  fs.mkdirSync(rolesDir, { recursive: true });
  for (const file of ['_SCHEMA.md', '_HR_INDEX.md']) {
    const src = path.join(pkgDir, 'ROLES', file);
    const dest = path.join(rolesDir, file);
    if (fs.existsSync(src) && !fs.existsSync(dest)) {
      fs.copyFileSync(src, dest);
      console.log(`✓ ROLES/${file}`);
    }
  }

  console.log('\n✓ conclave-cc v0.5.0 installed.');
  console.log('');
  console.log('  Next steps:');
  console.log('  1. Register the usage MCP (one-time):');
  console.log('     claude mcp add conclave-usage -- node ~/.claude/conclave-usage-mcp/src/index.js');
  console.log('');
  console.log('  2. Set your plan limit in CONCLAVE_SYSTEM.md:');
  console.log('     PLAN_LIMIT: 44000   ← Pro plan');
  console.log('     PLAN_LIMIT: 88000   ← Max5 plan');
  console.log('     PLAN_LIMIT: 220000  ← Max20 plan');
  console.log('');
  console.log('  3. Start a session: /conc "your project intention"');
  console.log('');
  console.log('  Optional: register interface-controller for Social Media Manager automation:');
  console.log('     claude mcp add interface-controller python ~/.claude/interface-controller/server.py');

} catch (err) {
  console.error('conclave-cc install failed:', err.message);
  process.exit(1);
}

function copyDirRecursive(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}
