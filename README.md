# conclave-cc

Conclave is an agentic business orchestration framework for solo founders. It transforms founder intent into a structured, executable, VC-ready business system — before any code is written. The system operates at the business coherence layer: vision, ICP, moat, revenue, brand, legal structure, and acquisition sequencing. It does not replace execution — it makes execution inevitable.

## Installation

```bash
npm i conclave-cc@latest
```

The postinstall script copies all agents, the skills library, the usage MCP, and system documents into `~/.claude/`. Role research templates are copied to `ROLES/` in your project directory.

**After installation, run once:**

```bash
# Register the token budget MCP
claude mcp add conclave-usage -- node ~/.claude/conclave-usage-mcp/src/index.js

# Set your plan limit in CONCLAVE_SYSTEM.md (Pro / Max5 / Max20)
# PLAN_LIMIT: 44000   ← Pro
# PLAN_LIMIT: 88000   ← Max5
# PLAN_LIMIT: 220000  ← Max20
```

## Usage

```
/conc "your project intention"
```

`/conc` is the single entry point. It checks for pending tasks in `conclave-queue.json`, checks for a prior session's Execution State in `EXECUTION_PLAN.md`, then runs the Chairman if no `VISION.md` exists or the CEO if it does.

Example session:

```
/conc "my project"         → Chairman writes VISION.md
/conc                      → CEO writes EXECUTION_PLAN.md, outputs: run /cto
/cto                       → CTO writes TECH.md (+ optional Design CTO consultation)
/conc                      → CEO conflict check, outputs: run /cmo
/cmo                       → CMO writes GTM.md (+ Social Media Manager + Traffic Manager consultation)
/conc                      → CEO conflict check, outputs: run /cro
/cro                       → CRO writes REVENUE.md
/conc                      → all documents complete, system status = READY
```

## What you get

| Document | Owner | Activation |
|---|---|---|
| `VISION.md` | Chairman | Always |
| `EXECUTION_PLAN.md` | CEO | Always |
| `TECH.md` | CTO | Product exists |
| `GTM.md` | CMO | Distribution undefined |
| `TRAFFIC.md` | Traffic Manager | GTM.md defined, no channel execution plan |
| `REVENUE.md` | CRO | Revenue model undefined |
| `COMMERCIAL.md` | CLO | Legal/commercial complexity medium or high |
| `SECURITY.md` | CISO | Security-sensitive product |
| `PRODUCT.md` | Design CTO | UX-critical for conversion |

## Agent system

**Core pipeline (CEO-activated):**
- **Chairman** — Vision extraction. Two-layer intake protocol. Writes `VISION.md`. Uses 3-Strategy Protocol for market category selection.
- **CEO** — Orchestration. Reads signals, applies activation matrix, sequences agents, routes skills, resolves conflicts. Checks token budget before parallel activation. Writes `EXECUTION_PLAN.md`.
- **CTO** — Technical architecture. Stack, delivery model, observability, fallback, security surface. Consults Design CTO before writing. Uses 3-Strategy Protocol for architecture posture.
- **CMO** — Go-to-market. ICP, channel, positioning, acquisition motion. Consults Social Media Manager + Traffic Manager before writing. Uses 3-Strategy Protocol for GTM motion.
- **Traffic Manager** — Channel hypothesis execution. 30-day test protocol, full-cost CAC, LTV:CAC gate. Writes `TRAFFIC.md`.
- **CRO** — Revenue model. Pricing, paywall, first sale target, LTV hypothesis. Uses 3-Strategy Protocol for pricing model.
- **CLO** — Commercial & legal. Entity structure, IP, contracts, compliance.
- **CISO** — Security & trust. Threat model (STRIDE), trust signals, minimum security posture. Writes `SECURITY.md`.
- **Design CTO** — Experience layer. Onboarding, conversion design, perception requirements. Writes `PRODUCT.md`.

**Operational agents (founder-activated):**
- **Social Media Manager** — Content execution. Weekly planning + daily crons (55% token savings). Content batch per 50/30/20 mix. Engagement-first measurement.
- **HR** — Role research and compilation. Researches real job postings, validates 10-item checklist, compiles `agents/[role].md`. Maps skill dependencies. Schedules 90-day reviews.

## Skills Library

Agents load frameworks on demand — not pre-loaded. 15 skills included:

| Skill | Framework |
|---|---|
| `positioning` | April Dunford 10-step |
| `jtbd-interview` | JTBD interview protocol |
| `stride-threat` | STRIDE threat modeling |
| `ltv-cac-gate` | LTV:CAC ≥ 3 acquisition gate |
| `value-based-pricing` | ProfitWell value pricing |
| `fogg-behavior` | Fogg B=MAP conversion framework |
| `content-mix` | 50/30/20 content mix protocol |
| `document-dont-create` | GaryVee documenting protocol |
| `safe-agreement` | YC SAFE structure |
| `equity-vesting` | 4-year vest / 1-year cliff |
| `mvp-architecture` | Minimum Viable Architecture |
| `tech-debt-quadrant` | Technical Debt Quadrant |
| `aha-moment` | Aha Moment Protocol |
| `channel-hypothesis` | Channel hypothesis execution |
| `luxury-acquisition` | High-ticket acquisition sequence |

CEO routes the relevant skills to each agent brief. Agents load them via Read tool at the relevant step.

## Token Budget

`conclave-usage-mcp` reads your local session JSONL and returns `{tokens_used, plan_limit, percent_used, recommendation}`. CEO calls this before activating agents in parallel.

- < 50% used → parallel eligible
- 50–70% → sequential
- 70–85% → sequential + warning
- > 85% → pause, write Execution State, resume with `/conc` in a new session

Session state is written to `EXECUTION_PLAN.md` after every agent activation, so restarting Claude Code never loses more than one agent's work.

## 3-Strategy Decision Protocol

When a HIGH-consequence strategic fork is detected (affects 2+ downstream agents), the relevant agent presents 3 named options with Approach, Advantage, Tradeoff, and Downstream impact — not an open question. Maximum 1 per session. Decision is locked after selection.

## Interface Controller MCP

For automated posting via Social Media Manager, register the `interface-controller` Playwright MCP:

```bash
claude mcp add interface-controller python ~/.claude/interface-controller/server.py
```

## Philosophy

**Derivation over interrogation.** Agents derive decisions from documents. They ask the founder only when ambiguity blocks a confident decision.

**Document ownership.** Every agent owns exactly one output document. No agent writes another agent's document.

**Conditional activation.** The CEO reads `VISION.md` signals and activates only the agents the project requires.

**Deterministic output.** Every agent session ends in a written document — never in reflection, summary, or open loop.

**Token efficiency by design.** Skills loaded on demand. Cron-based execution for operational agents. Token budget awareness built into CEO orchestration.

## v0.5.0 scope

This release adds: skills library (15 skill files), CEO skill routing, 3-Strategy Decision Protocol across 5 agents, C-level ↔ specialist consultation, cron-based Social Media Manager pattern, `conclave-usage-mcp` token budget server, and `/conc` as the unified entry point with state recovery. CFO and full financial modeling are planned for post-MVP stage.
