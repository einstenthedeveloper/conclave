# ARCHITECTURE.md
> Conclave agentic system blueprint. Read by humans and agents. Never edited manually — updated only through a new architectural decision ratified by the Chairman and CEO.

---

## 1. System Purpose

Conclave is an agentic business orchestration framework for solo founders. It transforms founder intent into a structured, executable, VC-ready business system — before any code is written.

The system operates at the business coherence layer: vision, ICP, moat, revenue, brand, and legal structure. It does not replace execution — it makes execution inevitable.

---

## 2. Core Principles

**Derivation over interrogation.** Agents derive decisions from documents. They ask the founder only when ambiguity blocks a confident decision.

**Document ownership.** Every agent owns exactly one output document. No agent writes another agent's document.

**Conditional activation.** Agents are not always active. The CEO reads VISION.md signals and activates only the agents required by the project context.

**One question at a time.** No agent asks two questions simultaneously. Interrogation is adaptive, not exhaustive.

**Confidence scoring.** Before asking a clarifying question, an agent must evaluate whether it can derive the answer from existing documents. If confidence is high — decide. If confidence is low — ask. Maximum 3 clarifying questions per agent session.

**Deterministic output.** Every agent session ends in a written document — never in reflection, summary, or open loop.

---

## 3. Agent Registry

| Agent | Role | Input | Output document | Activation |
|---|---|---|---|---|
| **Chairman** | Vision extraction | Founder (live) | `VISION.md` | Always — first |
| **CEO** | Orchestration | `VISION.md` | `EXECUTION_PLAN.md` | Always — second |
| **CTO** | Technical architecture | `VISION.md` + CEO brief | `TECH.md` | Product exists |
| **CMO** | Go-to-market | `VISION.md` + CEO brief | `GTM.md` | Distribution undefined |
| **CRO** | Revenue model | `VISION.md` + CEO brief | `REVENUE.md` | Monetization undefined |
| **CLO** | Commercial & legal | `VISION.md` + CEO brief | `COMMERCIAL.md` | Legal/IP/contracts present |
| **CISO** | Security & trust | `VISION.md` + `TECH.md` | `SECURITY.md` | Security-sensitive product |
| **Design CTO** | Experience layer | `VISION.md` + `GTM.md` | `PRODUCT.md` | UX-critical for conversion |
| **Traffic Manager** | Acquisition sequencing | `VISION.md` + `GTM.md` | `TRAFFIC.md` | Distribution defined, no channel execution plan |
| **Social Media Manager** | Organic content execution | `GTM.md` + `PRODUCT.md` | Weekly content batch + engagement report | GTM.md exists + organic channel in acquisition motion |
| **HR** | Role research & compilation | Role name (input) | `ROLES/[role].md` + `agents/[role].md` | Founder or CEO needs new role; substance audit; 90-day revision |
| **CFO** | Finance & valuation | All documents | `FINANCE.md` | Funding intent = yes (post-MVP) |

---

## 4. Activation Flow

```
/conclave
│
├── [1] CHAIRMAN
│     Input:  founder (live conversation)
│     Output: VISION.md
│     Rules:  Layer A (intent) → Layer B (operational context)
│             Sovereignty Filter applied to every signal
│             Writes "Signals for CEO Activation" block
│
├── [2] CEO
│     Input:  VISION.md
│     Action: reads signals → builds activation plan → activates agents
│     Rules:  conditional activation only (see Section 5)
│             resolves dependency order between agents
│             validates consistency between agent outputs
│             does not write domain documents — only orchestrates
│
├── [3] AGENTS (sequential by default — parallel only if no dependency overlap)
│     Each agent:
│       - reads VISION.md + CEO brief
│       - derives decisions from documents first
│       - asks founder only if confidence is low (max 3 binary/constrained questions)
│       - writes its output document
│       - emits a confidence score per decision
│       - flags unresolved hypotheses
│       - reports summary to CEO
│
└── [4] CEO (consolidation pass)
      - validates consistency across all output documents
      - identifies conflicts and gaps
      - requests revisions if needed
      - assembles the VC-ready document package
```

---

## 5. CEO Activation Matrix

| Signal | Condition | Agent activated |
|---|---|---|
| Product exists = yes | always | **CTO** |
| Distribution defined = no | always | **CMO** |
| Revenue model defined = no | always | **CRO** |
| Legal / commercial complexity = medium or high | always | **CLO** |
| Security-sensitive = yes | product exists | **CISO** |
| UX-critical = yes | distribution defined or CMO active | **Design CTO** |
| Traffic strategy needed = yes | GTM.md exists, no channel execution plan | **Traffic Manager** |
| Funding intent = yes | post-MVP | **CFO** |

**Activation rules:**
- CTO is the most frequently activated agent. If a product exists, CTO is always on.
- CMO and CRO are activated together when both distribution and monetization are undefined — they share context and must not conflict.
- CLO is activated before any external commitment (contracts, fundraising, IP transfer).
- CISO depends on CTO output — always activated after TECH.md exists.
- Traffic Manager activates after CMO completes GTM.md. It does not define channels — it sequences and plans execution across defined channels.
- Social Media Manager and HR are not in the main pipeline — they are operational agents activated by the founder or CMO directly.
- CFO is post-MVP only. Never activated before first sale.

---

## 5a. Conflict Resolution Rule

When two agents produce conflicting decisions, the CEO applies this protocol:

1. CEO identifies the conflict explicitly in EXECUTION_PLAN.md
2. CEO determines the domain of authority:
   - GTM conflicts → CMO has priority
   - Revenue conflicts → CRO has priority
   - Technical feasibility → CTO overrides all
   - Legal / compliance → CLO overrides all
3. CEO requests revision from the lower-priority agent only
4. Final decision must be singular — dual states are not allowed in any document

---

## 5b. System Halt Condition

- More than 40% of decisions across all active agents are LOW confidence → system_status = FRAGILE
- Any of the three core signals remain undefined (product_exists, distribution_defined, revenue_model_defined) → system_status = BLOCKED
- A critical dependency document is missing → CEO activates dependency agent first

---

## 5c. Question Protocol

Agent questions must be binary or constrained. Open-ended questions are forbidden. Maximum 3 questions per agent session. Unresolved fields after 3 questions become UNRESOLVED_HYPOTHESIS.

---

## 5d. Iteration Loop

After first sale attempt or experiment failure, the CEO re-activates only the agent whose document covers the failed assumption. VISION.md is never updated in iteration — only a new /conclave session can update it. CEO logs every iteration in EXECUTION_PLAN.md.

---

## 6. Document Pipeline

```
VISION.md              ← Chairman (always first)
EXECUTION_PLAN.md      ← CEO (always second)
    │
    ├── TECH.md         ← CTO
    ├── GTM.md          ← CMO
    │     │
    │     └── TRAFFIC.md    ← Traffic Manager (requires GTM.md)
    │
    ├── REVENUE.md      ← CRO
    ├── COMMERCIAL.md   ← CLO
    │     │
    │     └── SECURITY.md   ← CISO (requires TECH.md)
    │
    └── PRODUCT.md      ← Design CTO (requires GTM.md)

FINANCE.md             ← CFO (post-MVP only)

[Operational — not in primary pipeline]
Weekly content batch + engagement report  ← Social Media Manager (requires GTM.md)
agents/[role].md                    ← HR (activated by founder, not CEO pipeline)
```

---

## 7. Agent Behavior Protocol

```
1. READ    — read VISION.md and dependency documents
2. DERIVE  — extract all decisions from existing documents
3. SCORE   — assign confidence: HIGH | MEDIUM | LOW per decision
4. ASK     — binary/constrained questions only, max 3, one at a time
5. DECIDE  — deterministic value for every field
6. WRITE   — write output document
7. FLAG    — mark UNRESOLVED_HYPOTHESIS entries
8. REPORT  — emit summary to CEO
```

---

## 8. Document Standard

Every output document:

```markdown
# [DOCUMENT_NAME].md
> Generated by [Agent]. Updated by re-running the agent session.

## Decisions
[Field: value — confidence: HIGH | MEDIUM | LOW]

## Rationale
[Why each decision was made]

## Unresolved Hypotheses
[Fields that could not be decided]

## Risks
[Known risks]

## Next Experiment
[Minimum action to validate most critical assumption]

## Change Log
| Date | Change | Author |
|---|---|---|
```

EXECUTION_PLAN.md structure:

```markdown
# EXECUTION_PLAN.md
> Generated by CEO. Updated after every agent session and iteration.

## System Status
[READY | FRAGILE | BLOCKED]

## Activated Agents
## Activation Order
## Dependencies
## Conflicts Identified
## Missing Signals
## Iteration Log
| Date | Trigger | Agent re-activated | Outcome |
|---|---|---|---|

## Change Log
| Date | Change | Author |
|---|---|---|
```

---

## 9. VC-Ready Package

**Pre-seed / First sale minimum:**
VISION.md + TECH.md + GTM.md + REVENUE.md + COMMERCIAL.md

**Post-MVP / Fundraising:**
All above + SECURITY.md + PRODUCT.md + FINANCE.md

---

## 10. System Constraints

- No agent executes tasks or writes code
- No agent writes another agent's document
- No document is final — change log is mandatory on every update
- No founder input is assumed — absent signals trigger questions, not invention
- The Chairman never returns — vision updates require a new /conclave session
- CFO never activates before first sale

---

## 11. v2 Architecture Pillars

### Pillar 1 — Skills System (token efficiency)

Agents load frameworks on demand via the Read tool. Skills are `.md` files in `~/.claude/commands/skills/`. Each skill is 200–400 tokens of pure protocol — no agent identity, no preamble.

**Token savings:** agents load only the skills relevant to their current task. Estimated 60–75% reduction in per-agent token consumption vs. embedding all frameworks in the agent file.

**CEO as skill router:** when briefing each agent, CEO identifies which skills are relevant to the project context and includes `SKILL ROUTING: REQUIRED / CONTEXTUAL` in the brief.

### Pillar 2 — 3-Strategy Decision Protocol

When an agent encounters a HIGH-consequence strategic fork (affects 2+ downstream agents or sets a founding constraint), it presents 3 named options with Approach, Advantage, Tradeoff, and Downstream impact — not an open question. Maximum 1 per session. After the founder selects, the decision is locked in EXECUTION_PLAN.md and never re-asked.

### Pillar 3 — C-Level ↔ Specialist Consultation

Before writing its output document, a C-level can spawn a specialist subagent via the Agent tool to validate its draft decisions. The specialist returns CLEAR or BLOCKER in < 200 tokens. Token cost per consultation: ~1,500–4,000 tokens vs. 6,000–15,000 for a conflict-triggered document re-run.

Allowed: CMO → Social Media Manager | Traffic Manager. CTO → Design CTO. CEO → any C-level.

### Pillar 4 — Cron-Based Token Efficiency

Social Media Manager: weekly planning session (1× per week, ~3,000 tokens) + daily execution crons (~800 tokens each). 55% token savings vs. batching all posts in one session.

HR: creates 90-day review crons at agent-approval time.

### Pillar 5 — Token Budget Awareness (conclave-usage-mcp)

`conclave-usage-mcp` is a Node.js stdio MCP server that reads `~/.claude/projects/[project]/[session-id].jsonl`, sums token usage, and returns `{tokens_used, plan_limit, percent_used, recommendation}`. CEO calls this before deciding parallel vs. sequential activation.

### Pillar 6 — State Recovery

CEO writes `## Execution State` to EXECUTION_PLAN.md after every agent activation. `/conc` reads this block on session start and resumes from the first pending agent — surviving CLI restarts and session crashes with at most 1 agent re-run.

### Pillar 7 — Execution Adapters (pluggable)

Core (agents + skills + queue) is adapter-agnostic. Three adapters:
- **Local** — runs in Claude Code CLI, manual `/conc` activations, desktop crons
- **Scheduled VPS** — Claude Code CLI on a VPS + cron daemon, desktop routines persist across restarts
- **Telegram** — mobile interface, commands forwarded to VPS Claude Code instance

All adapters share the same core. Agents are blind to the executor.
