# Conclave Security Policy

**Scope:** package-level security policy for the Conclave system installed via `pnpm install conclave-cc`. Distinct from runtime `SECURITY.md` documents produced by the CISO agent inside user projects.

**Reference research:** This policy codifies findings from `sec-search.md` (Sept 2025) on secure multi-agent orchestration and supply-chain hardening.

---

## Seven Principles

### 1. Least Privilege
Each agent in `agents/[slug].md` declares an explicit `tools:` list in frontmatter. Agents receive only the capabilities required for their role:
- CFO: read-only access to financial docs; no posting, no API write
- Social Media Manager: posting tools; no access to financial data, no DB write
- HR: agent file write under `ROLES/` and `agents/`; no production system access
- Cross-domain operations require **CEO orchestration** (CONSULTATION_PROTOCOL), not direct agent-to-agent invocation.

### 2. Sandboxing
Agents execute via Claude Code's `Task` subagent — each in an isolated context window. Skills that touch:
- Ad spend (Google Ads, Meta Ads)
- Live posting (social platforms)
- Contract signing (e-sign integrations)
- Financial transactions
require **interactive HITL confirmation** before any write operation. Defined in each agent's frontmatter.

### 3. Strong Auth (JIT tokens)
- **No secrets in agent files or `ROLES/`** — agents reference env vars only
- All credentials via environment variables (`.env` is `.gitignore`d)
- Recommended: short-lived tokens (just-in-time) for API integrations, rotated per session
- Never commit `.env`, `credentials.json`, or `*.pem` files

### 4. PII Masking
Before sending customer data to LLM endpoints:
- Mask CPF, email, phone, address, payment data
- Future `conclave-pii-scrubber` MCP (P0 roadmap) will automate this at the tool boundary
- Until then: agents handling customer data must invoke a sanitization step explicitly

### 5. Audit + HITL
- Every agent file write logs to `~/.claude/conclave-audit.log` (timestamp, slug, file path, content hash)
- High-risk actions require human-in-the-loop approval:
  - Ad spend > $0
  - Live social posting
  - Contract signing
  - Database schema changes in user systems
- Future `conclave-audit` MCP (P0 roadmap) will centralize this

### 6. Prompt-Injection Defense
- All slash command inputs are validated structurally before becoming agent prompts
- Agent outputs are validated before being passed as input to next agent in chain
- User-provided content (file uploads, URLs) is wrapped in clearly delimited boundaries before LLM ingestion
- Knowledge files in `knowledge/` are loaded only by trusted entry points

### 7. Package Manager
- **pnpm is the default** package manager (content-addressable store, no phantom dependencies, supply-chain protection)
- **npm fallback supported** with documented degraded guarantees
- `.npmrc` settings: `engine-strict=true`, `audit-level=moderate`, `strict-peer-dependencies=true`
- Lockfile (`pnpm-lock.yaml`) is committed and verified on CI

---

## In-House MCP Policy

All MCPs that touch sensitive data (ads, social posting, financial systems, PII) are **built and owned internally**. This reduces the ongoing security audit surface to a fixed, self-controlled set — no third-party upgrade cycles reopening the analysis.

External plugins (`/octo`, GitHub MCP, Filesystem MCP, etc.) serve as **architectural inspiration only** — never as runtime dependencies for sensitive operations.

See `mcp/README.md` for the active and roadmap MCP catalog.

---

## Reporting

Security issues: **einstenrodrigues.dev@gmail.com**

Disclosure timeline: 30 days from acknowledgment to fix in next minor release. Critical issues (RCE, auth bypass, data exfiltration) handled within 7 days.
