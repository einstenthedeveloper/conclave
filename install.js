const fs = require('fs');
const path = require('path');
const os = require('os');

try {
  const claudeDir = path.join(os.homedir(), '.claude');
  const agentsDir = path.join(claudeDir, 'agents');
  const commandsDir = path.join(claudeDir, 'commands');
  const pkgDir = __dirname;

  fs.mkdirSync(agentsDir, { recursive: true });
  fs.mkdirSync(commandsDir, { recursive: true });
  console.log(`✓ Ensured ${agentsDir}`);
  console.log(`✓ Ensured ${commandsDir}`);

  const agentFiles = fs.readdirSync(path.join(pkgDir, 'agents'));
  for (const file of agentFiles) {
    const src = path.join(pkgDir, 'agents', file);
    const dest = path.join(agentsDir, file);
    fs.copyFileSync(src, dest);
    console.log(`✓ Copied agents/${file} → ${dest}`);
  }

  const commandFiles = fs.readdirSync(path.join(pkgDir, 'commands'));
  for (const file of commandFiles) {
    const src = path.join(pkgDir, 'commands', file);
    const dest = path.join(commandsDir, file);
    fs.copyFileSync(src, dest);
    console.log(`✓ Copied commands/${file} → ${dest}`);
  }

  for (const systemDoc of ['ARCHITECTURE.md', 'ORCHESTRATION.md']) {
    const src = path.join(pkgDir, systemDoc);
    const dest = path.join(claudeDir, systemDoc);
    fs.copyFileSync(src, dest);
    console.log(`✓ Copied ${systemDoc} → ${dest}`);
  }

  const templateFiles = fs.readdirSync(path.join(pkgDir, 'templates'));
  for (const file of templateFiles) {
    const dest = path.join(process.cwd(), file);
    if (!fs.existsSync(dest)) {
      fs.copyFileSync(path.join(pkgDir, 'templates', file), dest);
      console.log(`✓ Copied templates/${file} → ${dest}`);
    } else {
      console.log(`  (skipped — already exists) ${file}`);
    }
  }

  const rolesDir = path.join(process.cwd(), 'ROLES');
  fs.mkdirSync(rolesDir, { recursive: true });
  for (const rolesTemplate of ['_SCHEMA.md', '_HR_INDEX.md']) {
    const src = path.join(pkgDir, 'ROLES', rolesTemplate);
    const dest = path.join(rolesDir, rolesTemplate);
    if (!fs.existsSync(dest)) {
      fs.copyFileSync(src, dest);
      console.log(`✓ Copied ROLES/${rolesTemplate} → ${dest}`);
    } else {
      console.log(`  (skipped — already exists) ROLES/${rolesTemplate}`);
    }
  }

  console.log('\n✓ conclave-cc v0.3.0 installed.');
  console.log('  Run /conclave "your project intention" to begin.');
  console.log('  After VISION.md is written, run /ceo to activate the CEO orchestration layer.');
  console.log('');
  console.log('  For Social Media Manager: register the interface-controller MCP first.');
  console.log('  → claude mcp add interface-controller python ~/.claude/interface-controller/server.py');
} catch (err) {
  console.error('conclave-cc install failed:', err.message);
  process.exit(1);
}
