# /build

Continuous build loop for Conclave agents. Uses HR to research and compile agents from the
queue. Self-paces via ScheduleWakeup based on token budget. Designed to run inside `/loop`.

**Entry points:**
- `/loop /build` — starts the continuous build loop (recommended)
- `/build [agent-slug]` — builds one specific agent, no loop
- `/build queue` — shows queue status without building

---

## LOOP PROTOCOL

Executes on every ScheduleWakeup fire when running via `/loop /build`.

**Step 1 — Read queue**

Read `conclave-queue.json` in the current working directory.
Find all entries where `status: "pending"` AND `type: "agent-build"`.
Sort by `scheduled_for` ascending (oldest first).

If no pending entries found:
- Report: "Build queue empty. All agents completed."
- Do NOT call ScheduleWakeup. Loop ends here.

**Step 2 — Check token budget**

Call `usage/current` via the conclave-usage-mcp MCP tool.

If `recommendation = "pause"` (percent_used ≥ 85):
- Report: "Token budget at [percent]% — pausing build. Will retry in 30 min."
- Write current agent slug to `conclave-queue.json` entry as `status: "pending"` (no change)
- ScheduleWakeup(1800, "token budget near limit — retrying build loop")
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
| ≥ 85 | 1800s | "budget near limit — pausing build loop" |

Call ScheduleWakeup with delay, reason, and prompt: `/build`

---

## SINGLE AGENT PROTOCOL

When called as `/build [agent-slug]` (no loop):

1. Check if `agents/[agent-slug].md` already exists → if yes, ask: re-research or audit?
2. Call `usage/current` — if `pause`, warn and ask user to confirm before continuing
3. Activate HR subagent with the same prompt as Step 3 above
4. Report result. Do NOT call ScheduleWakeup.

---

## QUEUE STATUS PROTOCOL

When called as `/build queue`:

Read `conclave-queue.json`. Report:

```
Build Queue Status
──────────────────
Completed : [N] agents
In progress: [slug or none]
Pending   : [N] agents — next: [slug]
Draft     : [N] agents (gaps identified, awaiting fix)

Token budget: [percent]% used ([recommendation])
```

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

Priority field: 0 = P0 (pre-seed critical), 1 = P1, 2 = P2, 3 = P3.
Queue is sorted by priority ascending, then scheduled_for ascending.

---

## Initializing the queue

To populate `conclave-queue.json` with the full 118-agent build plan from the organagram,
run: `/build init` — reads `D:/conclave/organagram-research.md` (or the workspace research
file) and generates all pending entries sorted by priority.

**Step-by-step for `/build init`:**
1. Read the organagram research file to get the priority-ordered agent list
2. Read `conclave-queue.json` — skip agents already marked done or in index
3. Read `ROLES/_HR_INDEX.md` — skip agents already in Active table
4. Write all remaining agents as pending entries to `conclave-queue.json`
5. Report: total queued, already built, estimated sessions needed at current plan

---

## Notes

- The loop is resilient to compaction: state lives in `conclave-queue.json`, not in context.
  After any compaction or manual session restart, `/loop /build` picks up from the same file.
- `/conc` Step 1 already checks `conclave-queue.json` for pending tasks — so a new session
  will surface build tasks automatically.
- HR is the sole builder. `/build` is the scheduler and state manager only.
