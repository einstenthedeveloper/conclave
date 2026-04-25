# /immortal-genesis

Genesis build command. Constructs all 118 Conclave agents from the organogram research
file using HR. Powered by the **immortal-engine** — a ScheduleWakeup + conclave-usage-mcp
loop that pauses at 95% session budget and resumes automatically when the session resets.

**Scope:** Genesis phase only — developer use. End users never run this.
**Output:** `agents/[slug].md` + `ROLES/[slug].md` + `knowledge/` stubs for all 118 agents.

**Entry points:**
- `/immortal-genesis` — starts (or resumes) the continuous build loop
- `/immortal-genesis init` — populates conclave-queue.json from organogram-research.md
- `/immortal-genesis status` — build progress report, no building
- `/immortal-genesis [agent-slug]` — builds one specific agent, no loop

---

## THE IMMORTAL-ENGINE

The immortal-engine is the pacing mechanism that makes multi-session builds resilient:

```
ScheduleWakeup (timer) + conclave-usage-mcp (budget sensor) + conclave-queue.json (state)
```

- **Timer**: ScheduleWakeup fires `/immortal-genesis` after a delay
- **Budget sensor**: `usage/current` via conclave-usage-mcp returns `percent_used`
- **State**: `conclave-queue.json` holds queue status — survives compaction and session restarts
- At 95%: engine pauses, schedules a 30-min check. When budget resets, engine resumes.
- The loop is immortal: it cannot be killed by context limits or session endings.

---

## LOOP PROTOCOL

Fires on every ScheduleWakeup (prompt: `/immortal-genesis`) and on manual invocation.

**Step 1 — Read queue**

Read `conclave-queue.json`.
Find all entries where `status: "pending"` AND `type: "agent-build"`.
Sort by `priority` ascending, then `scheduled_for` ascending (P0 first).

If no pending entries found:
- Report: "Genesis complete. All agents built. Commit agents/ + ROLES/ + knowledge/, bump version, push tag."
- Do NOT call ScheduleWakeup. Engine stops.

**Step 2 — Check budget (immortal-engine gate)**

Call `usage/current` via conclave-usage-mcp. Read `percent_used`.

```
percent_used ≥ 95  → PAUSE
  - Report: "Budget at [X]% — immortal-engine pausing. Will check again in 30 min."
  - Leave queue entry as status: "pending" (no change)
  - ScheduleWakeup(1800, "immortal-engine: checking if session budget reset")
  - STOP. Do not activate HR.

percent_used 70–94  → THROTTLE
  - Build ONE agent this iteration only
  - After HR completes, re-check budget before scheduling next wakeup

percent_used < 70   → FULL SPEED
  - Proceed normally
```

**Step 3 — Activate HR**

Mark target entry `status: "in_progress"` in `conclave-queue.json`.

```
Agent({
  description: "immortal-genesis: build [role_slug]",
  subagent_type: "hr",
  prompt: "Build the Conclave agent for role: [role_slug].
Working directory: D:/conclave/conclave-cc
Organogram reference: D:/conclave/organogram-research.md

Run the full Research Protocol (Steps 1–6 including domain knowledge mapping).
Run the 10-item checklist.
If APPROVED: compile agents/[role-slug].md and create any knowledge/ stubs flagged as GAPs.
Update ROLES/_HR_INDEX.md.
Return: status (APPROVED/DRAFT), files written, knowledge gaps identified."
})
```

**Step 4 — Update queue**

After HR returns:
- APPROVED → `status: "done"`, add `completed_at: [ISO timestamp]`
- DRAFT → `status: "draft"`, add `gaps: [list from HR report]`
- Write `conclave-queue.json`

**Step 5 — Schedule next iteration (immortal-engine timer)**

Call `usage/current` again. Pick delay:

| percent_used | delay | reason |
|---|---|---|
| < 70 | 90s | "immortal-genesis: continuing — next: [slug]" |
| 70–94 | 180s | "immortal-genesis: throttling — next: [slug]" |
| ≥ 95 | 1800s | "immortal-engine: budget at [X]% — checking reset in 30 min" |

Call ScheduleWakeup with delay, reason, prompt: `/immortal-genesis`

---

## SINGLE AGENT PROTOCOL

When called as `/immortal-genesis [agent-slug]`:

1. Check if `agents/[agent-slug].md` exists → if yes, ask: re-research or audit?
2. Call `usage/current` — if ≥ 95%, warn and ask user to confirm before continuing
3. Activate HR subagent (same prompt as Step 3)
4. Report result. Do NOT call ScheduleWakeup.

---

## STATUS PROTOCOL

When called as `/immortal-genesis status`:

Read `conclave-queue.json`. Call `usage/current`. Report:

```
/immortal-genesis — Genesis Build Status
─────────────────────────────────────────
Completed : [N] agents
In progress: [slug or none]
Pending   : [N] agents — next: [slug] (P[priority])
Draft     : [N] agents (gaps found, awaiting fix)

immortal-engine: [percent]% budget used
Status: [RUNNING / THROTTLED / PAUSED — resets in ~[time]]

Resume: /immortal-genesis
```

---

## INIT PROTOCOL

When called as `/immortal-genesis init`:

1. Read `D:/conclave/organogram-research.md` — extract Agent Inventory table from
   "CONCLAVE SYSTEM — ARCHITECTURE REFERENCE" section
2. Read `conclave-queue.json` — skip agents already done or in_progress
3. Read `ROLES/_HR_INDEX.md` — skip agents already in Active table
4. Write all remaining agents as pending entries to `conclave-queue.json`
5. Report: total queued, already built, P0/P1/P2/P3 breakdown

---

## Queue entry format

```json
{
  "id": "hr-build-[role-slug]-[YYYY-MM-DD]",
  "type": "agent-build",
  "agent": "hr",
  "role_slug": "[role-slug]",
  "priority": 0,
  "status": "pending",
  "scheduled_for": "[YYYY-MM-DD]",
  "created_at": "[ISO timestamp]",
  "completed_at": null,
  "gaps": []
}
```

Priority: 0 = P0 (Board + C-levels), 1 = P1 (operational G0-G4), 2 = P2 (scale G5-G9), 3 = P3 (enterprise G10-G12).

---

## After Genesis Completes

```bash
git add agents/ ROLES/ knowledge/
git commit -m "feat: genesis build complete — 118 agents"
# bump version in package.json to 1.0.0
git tag v1.0.0
git push origin master --tags
# GitHub Actions publishes to npm with OIDC provenance
```
