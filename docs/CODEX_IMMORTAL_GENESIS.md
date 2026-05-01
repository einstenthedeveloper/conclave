# CODEX_IMMORTAL_GENESIS

`/immortal-genesis` was originally authored as a Claude Code command backed by files in `~/.claude/commands/` and a runtime loop using `ScheduleWakeup` plus `conclave-usage-mcp`.

Inside Codex, the closest equivalent is:

- a local plugin: `plugins/immortal-genesis`
- a skill trigger named `immortal-genesis`
- a queue runner script: `conclave-cc/scripts/immortal_genesis.py`

## One-time Codex CLI install

Register the repository as a local plugin marketplace:

```powershell
cmd /c codex plugin marketplace add D:\conclave
```

This writes the marketplace registration to `~/.codex/config.toml` under:

- `marketplaces.conclave-local`

## What works now

- `init`: repopulates missing pending entries from `organagram-research.md`
- `status`: reports queue counts and next candidate
- `next`: returns the stale `in_progress` role first, then the next `pending` role
- `set-status`: updates queue state after HR work

## What does not exist in Codex

- native slash command registration identical to Claude Code
- `ScheduleWakeup` auto-loop
- automatic session-budget sensing through `usage/current`

## Practical usage in this repo

```powershell
cmd /c codex
python .\conclave-cc\scripts\immortal_genesis.py status
python .\conclave-cc\scripts\immortal_genesis.py next --json
python .\conclave-cc\scripts\immortal_genesis.py set-status osint-specialist in_progress
```

Then continue the build by following `conclave-cc/agents/hr.md` against the chosen slug.

In a fresh Codex session, `immortal-genesis` should now be available as a plugin-backed skill from the `conclave-local` marketplace.
