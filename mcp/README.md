# In-House MCP Servers

Bundled with `conclave-cc`, auto-registered into `~/.claude/settings.json` on install via non-destructive merge.

## Active

| MCP | Path | Function |
|---|---|---|
| `conclave-usage` | `usage/` | Token budget awareness — feeds `percent_used` to CEO activation protocol |
| `conclave-interface` | `interface-controller/` | Browser automation via Playwright (navigate, click, type, upload, screenshot) |

## Roadmap

| Priority | MCP | Function | Replaces |
|---|---|---|---|
| P0 | `conclave-audit` | Centralized audit log of agent reads/writes | Datadog Audit, Splunk |
| P0 | `conclave-pii-scrubber` | Mask PII (CPF, email, phone) before LLM calls | AWS Comprehend, MS Presidio |
| P1 | `conclave-parallel-dispatch` | Parallel subagent dispatch (Claude `claude -p` pattern) | /octo parallel |
| P1 | `conclave-ads-connector` | Least-privilege, JIT-token access to Google/Meta Ads | 3rd-party ad plugins |
| P2 | `conclave-social-poster` | Social posting with mandatory HITL approval | Buffer, Hootsuite |
| P2 | `conclave-git-vault` | Encrypted versioning of strategic docs | GitHub MCP |

## Strategy

All MCPs that touch sensitive data are built and owned internally. This reduces the ongoing security audit surface to a fixed, self-controlled set — no third-party upgrade cycles reopening the analysis. External plugins (`/octo`, GitHub MCP, etc.) serve as architectural inspiration only, never as runtime dependencies.

See `architecture.md` "In-House MCP Strategy" section and `SECURITY.md` for full rationale.
