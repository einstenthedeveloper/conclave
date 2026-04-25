# /immortal-genesis-init

Populates `conclave-queue.json` with all agents from the organogram research file.
Run once before starting `/immortal-genesis`. Safe to re-run — skips already-built agents.

---

**PROTOCOL**

1. Read `D:/conclave/organogram-research.md` — locate the "### Agent Inventory" table in the
   "CONCLAVE SYSTEM — ARCHITECTURE REFERENCE" section. Extract every row.

2. Read `conclave-queue.json` if it exists — collect all entries with `status: "done"` or
   `status: "in_progress"`. Skip their slugs.

3. Read `ROLES/_HR_INDEX.md` if it exists — collect all slugs in the Active table. Skip them.

4. For every remaining slug: write a pending entry to `conclave-queue.json`:

```json
{
  "id": "hr-build-[role-slug]-2026-04-25",
  "type": "agent-build",
  "agent": "hr",
  "role_slug": "[role-slug]",
  "priority": [0|1|2|3],
  "status": "pending",
  "scheduled_for": "2026-04-25",
  "created_at": "2026-04-25T00:00:00Z",
  "completed_at": null,
  "gaps": []
}
```

Priority mapping:
- P0: Board + C-level core (chairman, ceo, cto, cmo, cro, clo, ciso, design-cto)
- P1: Operational specialists (G0–G4 triggers in organogram)
- P2: Scale specialists (G5–G9)
- P3: Enterprise/context-specific (G10–G12)

5. Report:
```
/immortal-genesis-init — Queue Initialized
──────────────────────────────────────────
Queued   : [N] agents (P0: X · P1: X · P2: X · P3: X)
Skipped  : [N] already built or in progress
Total    : [N] agents

Next: /immortal-genesis
```
