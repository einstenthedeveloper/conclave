# /ceo

Activates the CEO orchestration layer.

Usage: /ceo

Precondition: VISION.md must exist in the current directory. If it does not exist, run /conclave first.

Execution:

1. CEO reads VISION.md and parses the Signals for CEO Activation block
2. CEO writes EXECUTION_PLAN.md
3. CEO outputs the ordered command sequence to execute next

The CEO does NOT automatically run agents. It outputs the exact commands the user must run manually, in the correct dependency order.

**The CEO is the only authority that decides what runs next. Never run an agent command without consulting /ceo first. Running agents out of sequence breaks dependencies and creates undetectable conflicts.**

After each agent command completes, re-run /ceo to:
- Check the new document for conflicts
- Apply conflict resolution if needed
- Output the next command in the sequence

Loop continues until all required documents are written and system status = READY | FRAGILE | BLOCKED.

Example session:

/conclave "my project"     → Chairman writes VISION.md
/ceo                       → CEO writes EXECUTION_PLAN.md, outputs: run /cto
/cto                       → CTO writes TECH.md
/ceo                       → conflict check, outputs: run /cmo
/cmo                       → CMO writes GTM.md
/ceo                       → conflict check, outputs: run /cro
...
/ceo                       → all documents complete, system status = READY

---

Use the `ceo` subagent to handle this request.

@ceo
