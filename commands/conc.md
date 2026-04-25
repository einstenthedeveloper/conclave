# /conc

Activates the Conclave system. Single entry point for all sessions.

Usage: /conc

---

**ENTRY PROTOCOL — execute in order:**

**Step 1 — Queue check**
Read `conclave-queue.json` if it exists.
If `queue` array has entries with `status: "pending"` and `scheduled_for` ≤ today:
  Execute each pending task in order before continuing.
  Update each entry to `status: "done"` after execution.
If any entries have `type: "agent-build"` and `status: "pending"`:
  Report count and next slug. Instruct founder: "Run `/loop /build` to continue the agent build queue."
  Do NOT auto-execute build tasks from /conc — they run via /build loop only.

**Step 2 — State recovery**
Read `EXECUTION_PLAN.md` if it exists.
Look for `## Execution State` block.
If `Pending:` list is not empty:
  Resume pipeline from the first pending agent — do not repeat completed agents.
  Announce: "Resuming Conclave session. Completed: [X]. Pending: [Y]."

**Step 3 — Normal flow**
If `VISION.md` does not exist:
  Activate Chairman. Run full intake protocol. Write VISION.md.
If `VISION.md` exists and pipeline is complete:
  Ask founder: "What would you like to do? (a) Start a new project — runs /conclave to overwrite VISION.md. (b) Continue — re-activate CEO for consistency pass or agent revision."

---

Use the `chairman` subagent to handle new project intake.
Use the `ceo` subagent to resume or orchestrate existing pipelines.
