import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

LOG_PATH = Path(__file__).parent / "workspace" / "execution_log.json"


def log_write(
    status: str,
    platform: str,
    result: str,
    failure_reason: str = "none",
    entry_id: str = None,
) -> dict:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    entries = []
    if LOG_PATH.exists():
        try:
            entries = json.loads(LOG_PATH.read_text())
        except Exception:
            entries = []

    entry = {
        "id": entry_id or str(uuid.uuid4())[:8],
        "status": status,
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "platform": platform,
        "result": result,
        "failure_reason": failure_reason,
    }
    entries.append(entry)
    LOG_PATH.write_text(json.dumps(entries, indent=2))
    return {"ok": True, "entry": entry, "log_path": str(LOG_PATH)}
