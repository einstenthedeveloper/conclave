# conclave-cc

Conclave is an agentic business orchestration framework for solo founders. It transforms founder intent into a structured, executable, VC-ready business system — before any code is written. The system operates at the business coherence layer: vision, ICP, moat, revenue, brand, legal structure, and acquisition sequencing. It does not replace execution — it makes execution inevitable.

## Installation

```bash
npm i conclave-cc@latest
```

The postinstall script copies all agents, commands, and system documents into `~/.claude/`, making them available globally in every Claude Code session. Role research templates are copied to `ROLES/` in your project directory.

## Usage

```
/conclave "your project intention"
```

The Chairman runs the full intake protocol and writes `VISION.md`. Then:

```
/ceo
```

The CEO reads `VISION.md`, applies the activation matrix, writes `EXECUTION_PLAN.md`, and outputs the exact command sequence to run next. Follow the CEO's instructions — run each agent command in order, then re-run `/ceo` after each one.

Example session:

```
/conclave "my project"   → Chairman writes VISION.md
/ceo                     → CEO writes EXECUTION_PLAN.md, outputs: run /cto
/cto                     → CTO writes TECH.md
/ceo                     → conflict check, outputs: run /cmo
/cmo                     → CMO writes GTM.md
/ceo                     → conflict check, outputs: run /traffic-manager
/traffic-manager         → Traffic Manager writes TRAFFIC.md (paid + organic + prospecting plan)
/ceo                     → all documents complete, system status = READY
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
- **Chairman** — Vision extraction. Runs the two-layer intake protocol. Writes `VISION.md`.
- **CEO** — Orchestration. Reads signals, applies activation matrix, sequences agents, resolves conflicts. Writes `EXECUTION_PLAN.md`.
- **CTO** — Technical architecture. Stack, delivery model, observability, fallback, security surface.
- **CMO** — Go-to-market. ICP, channel, positioning, acquisition motion.
- **Traffic Manager** — Acquisition sequencing. Three-lane plan: paid traffic, organic growth, and prospecting — with founder-context timing and CAC payback calculations. Writes `TRAFFIC.md`.
- **CRO** — Revenue model. Pricing, paywall, first sale target, LTV hypothesis.
- **CLO** — Commercial & legal. Entity structure, IP, contracts, compliance.
- **CISO** — Security & trust. Threat model, trust signals, minimum security posture.
- **Design CTO** — Experience layer. Onboarding, conversion design, perception requirements.

**Operational agents (founder-activated):**
- **Social Media Manager** — Content execution. Publishes scheduled posts via `interface-controller` MCP, maintains `calendar.json`, logs results, produces weekly performance reports with volume/quality/business metrics.
- **HR** — Role research and compilation. Researches real job postings, synthesizes validated role docs (`ROLES/[role].md`), and compiles production-ready agent files (`agents/[role].md`) with real market substance.

## Interface Controller MCP

The Social Media Manager uses `interface-controller` — a local Playwright MCP server for browser automation. To register it after installation:

```bash
claude mcp add interface-controller python ~/.claude/interface-controller/server.py
```

This enables automated posting, session management, and execution logging via browser.

## Philosophy

**Derivation over interrogation.** Agents derive decisions from documents. They ask the founder only when ambiguity blocks a confident decision.

**Document ownership.** Every agent owns exactly one output document. No agent writes another agent's document.

**Conditional activation.** The CEO reads `VISION.md` signals and activates only the agents the project requires.

**Deterministic output.** Every agent session ends in a written document — never in reflection, summary, or open loop.

**Sovereignty by inevitability.** Every signal is filtered through five structural questions before being recorded as a decision. Signals that fail the filter become unresolved hypotheses — not closed decisions.

## v0.3.0 scope

This release includes Chairman, CEO, CTO, CMO, Traffic Manager, CRO, CLO, CISO, Design CTO, Social Media Manager, and HR. CFO and full financial modeling (`FINANCE.md`) are planned for the next release (post-MVP, funding intent only).
