# /conclave

Activates the Chairman to begin the Conclave intake protocol.

Usage: /conclave "[project intention]"

The Chairman will run the full intake protocol across two layers and produce VISION.md with the canonical project vision and CEO activation signals.

After VISION.md is written, run /ceo to activate the CEO orchestration layer.

Example:
/conclave "I want to build a position-based agentic company framework"

---

Use the `chairman` subagent to handle this request. Pass the user's input directly as the initial prompt to the Chairman. The Chairman will take over from here and run the full entry protocol.

@chairman $ARGUMENTS
