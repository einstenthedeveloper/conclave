# /immortal-genesis-status

Build progress report for the genesis phase. No building — read-only.

---

**PROTOCOL**

1. Read `conclave-queue.json`.
2. Call `usage/current` via conclave-usage-mcp.
3. Report:

```
/immortal-genesis — Genesis Build Status
─────────────────────────────────────────
Completed : [N] agents
In progress: [slug or "none"]
Pending   : [N] agents — next: [slug] (P[priority])
Draft     : [N] agents (gaps found, need fix)

immortal-engine: [percent]% budget used
Engine state: RUNNING / THROTTLED (70–94%) / PAUSED (≥95% — reset pending)

Resume : /immortal-genesis
Init   : /immortal-genesis-init  (if queue is empty)
Single : /immortal-genesis [slug] (type slug after invoking command)
```

If `conclave-queue.json` does not exist:
Report: "Queue not initialized. Run /immortal-genesis-init first."
