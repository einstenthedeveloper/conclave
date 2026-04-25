# /imortal

Continuous build engine for the Conclave agent library. Manages its own ScheduleWakeup loop —
no `/loop` wrapper needed. Uses HR to research and compile agents from the queue.
State survives compaction: lives in `conclave-queue.json`, not in context.

**Entry points:**
- `/imortal` — starts the continuous build engine (self-pacing via ScheduleWakeup)
- `/imortal init` — populates conclave-queue.json from the organogram research file
- `/imortal status` — current build progress, no building
- `/imortal [agent-slug]` — builds one specific agent, no loop

---

## LOOP PROTOCOL

Executes on every ScheduleWakeup fire (prompt: `/imortal`).

**Step 1 — Read queue**

Read `conclave-queue.json` in the current working directory.
Find all entries where `status: "pending"` AND `type: "agent-build"`.
Sort by `priority` ascending, then `scheduled_for` ascending (P0 first, oldest first within tier).

If no pending entries found:
- Report: "Build queue empty. All agents completed."
- Do NOT call ScheduleWakeup. Engine stops here.

**Step 2 — Check token budget**

Call `usage/current` via the conclave-usage-mcp MCP tool.

If `recommendation = "pause"` (percent_used ≥ 85):
- Report: "Token budget at [percent]% — pausing build. Will retry in 30 min."
- Leave current queue entry as `status: "pending"` (no change)
- ScheduleWakeup(1800, "token budget near limit — retrying /imortal")
- STOP. Do not activate HR.

If `recommendation = "sequential_warn"` (70–84%):
- Build ONE agent only this iteration, regardless of queue length.

If `recommendation = "sequential"` or `"parallel"` (< 70%):
- Proceed normally.

**Step 3 — Activate HR**

Mark the target entry in `conclave-queue.json` as `status: "in_progress"`.

Activate HR subagent:

```
Agent({
  description: "Build agent: [role_slug]",
  subagent_type: "hr",
  prompt: "Build the Conclave agent for role: [role_slug].
Run the full Research Protocol (Steps 1–6 including domain knowledge mapping).
Run the 10-item checklist.
If APPROVED: compile agents/[role-slug].md and create any knowledge/ stubs flagged as GAPs.
Update ROLES/_HR_INDEX.md.
Return: status (APPROVED/DRAFT), files written, knowledge gaps identified."
})
```

**Step 4 — Update queue**

After HR returns:
- If APPROVED: set entry `status: "done"`, add `completed_at: [ISO timestamp]`
- If DRAFT: set entry `status: "draft"`, add `gaps: [list from HR report]`
- Write updated `conclave-queue.json`

**Step 5 — Schedule next iteration**

Call `usage/current` again.

Pick ScheduleWakeup delay:

| percent_used | delay | reason string |
|---|---|---|
| < 70 | 90s | "continuing build — next: [next-slug]" |
| 70–84 | 180s | "budget warning — pacing — next: [next-slug]" |
| ≥ 85 | 1800s | "budget near limit — pausing /imortal" |

Call ScheduleWakeup with delay, reason, and prompt: `/imortal`

---

## SINGLE AGENT PROTOCOL

When called as `/imortal [agent-slug]` (no loop):

1. Check if `agents/[agent-slug].md` already exists → if yes, ask: re-research or audit?
2. Call `usage/current` — if `pause`, warn and ask user to confirm before continuing
3. Activate HR subagent with the same prompt as Step 3 above
4. Report result. Do NOT call ScheduleWakeup.

---

## STATUS PROTOCOL

When called as `/imortal status`:

Read `conclave-queue.json`. Call `usage/current`. Report:

```
/imortal — Build Engine Status
──────────────────────────────
Completed : [N] agents
In progress: [slug or none]
Pending   : [N] agents — next: [slug] (P[priority])
Draft     : [N] agents (gaps identified, awaiting fix)

Token budget: [percent]% used ([recommendation])

Next action: /imortal to resume | /imortal [slug] to build specific agent
```

---

## INIT PROTOCOL

When called as `/imortal init`:

1. Read the organogram research file at `D:/conclave/organagram-research.md` — extract agent list and priority order from the "## CONCLAVE SYSTEM — ARCHITECTURE REFERENCE" section (Agent Inventory table)
2. Read `conclave-queue.json` — skip agents already marked done or in_progress
3. Read `ROLES/_HR_INDEX.md` — skip agents already in the Active table
4. Write all remaining agents as pending entries to `conclave-queue.json`
5. Report: total queued, already built, priority breakdown

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

Priority field: 0 = P0 (board + C-level core), 1 = P1 (operational specialists), 2 = P2 (scale specialists), 3 = P3 (enterprise/context-specific).
Queue sorted by priority ascending, then scheduled_for ascending.

---

## Notes

- The loop is resilient to compaction: state lives in `conclave-queue.json`, not in context.
  After any compaction or manual session restart, `/imortal` picks up from the same file.
- `/conc` Step 1 surfaces pending build tasks automatically — so a new session will
  remind the founder to run `/imortal` if builds are pending.
- HR is the sole builder. `/imortal` is the scheduler and state manager only.
