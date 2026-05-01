#!/usr/bin/env python3
import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
QUEUE_PATH = ROOT / "conclave-queue.json"
ORGANOGRAM_PATH = ROOT / "organagram-research.md"
HR_INDEX_PATH = ROOT / "conclave-cc" / "ROLES" / "_HR_INDEX.md"

CORE_P0 = {
    "chairman",
    "ceo",
    "cto",
    "cmo",
    "cro",
    "clo",
    "ciso",
    "design-cto",
}

P1_SECTIONS = {"G0", "G1", "G2", "G3", "G4"}
P2_SECTIONS = {"G5", "G6", "G7", "G8", "G9"}
P3_SECTIONS = {"G10", "G11", "G12", "SCALE"}


@dataclass
class RoleSpec:
    slug: str
    section: str


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_queue() -> list[dict]:
    if not QUEUE_PATH.exists():
        return []
    return json.loads(QUEUE_PATH.read_text(encoding="utf-8"))


def save_queue(queue: list[dict]) -> None:
    QUEUE_PATH.write_text(json.dumps(queue, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def parse_hr_index_slugs() -> set[str]:
    if not HR_INDEX_PATH.exists():
        return set()
    slugs = set()
    for line in HR_INDEX_PATH.read_text(encoding="utf-8").splitlines():
        match = re.search(r"agents/([a-z0-9-]+)\.md", line)
        if match:
            slugs.add(match.group(1))
    return slugs


def parse_agent_inventory() -> list[RoleSpec]:
    text = ORGANOGRAM_PATH.read_text(encoding="utf-8")
    specs: list[RoleSpec] = []
    current_section = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        section_match = re.match(r"^###\s+(G\d+)\b", line)
        if section_match:
            current_section = section_match.group(1)
            continue

        if line.startswith("### Especialistas de Escala"):
            current_section = "SCALE"
            continue

        if not current_section or not line.startswith("|"):
            continue

        if "`" in line:
            continue

        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells or cells[0].lower() == "slug" or set(cells[0]) == {"-"}:
            continue

        slug = cells[0]
        if not re.fullmatch(r"[a-z0-9-]+", slug):
            continue

        specs.append(RoleSpec(slug=slug, section=current_section))

    return dedupe_specs(specs)


def dedupe_specs(specs: Iterable[RoleSpec]) -> list[RoleSpec]:
    seen = set()
    result = []
    for spec in specs:
        if spec.slug in seen:
            continue
        seen.add(spec.slug)
        result.append(spec)
    return result


def priority_for(spec: RoleSpec) -> int:
    if spec.slug in CORE_P0:
        return 0
    if spec.section in P1_SECTIONS:
        return 1
    if spec.section in P2_SECTIONS:
        return 2
    if spec.section in P3_SECTIONS:
        return 3
    return 3


def command_init() -> int:
    inventory = parse_agent_inventory()
    queue = load_queue()
    existing_by_slug = {item["role_slug"]: item for item in queue}
    completed_or_active = {
        item["role_slug"]
        for item in queue
        if item.get("status") in {"done", "in_progress", "draft", "pending"}
    }
    indexed = parse_hr_index_slugs()

    added = []
    skipped = 0
    today = datetime.now(timezone.utc).date().isoformat()
    created_at = now_iso()

    for spec in inventory:
        if spec.slug == "hr":
            skipped += 1
            continue
        if spec.slug in completed_or_active or spec.slug in indexed or spec.slug in existing_by_slug:
            skipped += 1
            continue
        added.append(
            {
                "id": f"hr-build-{spec.slug}-{today}",
                "type": "agent-build",
                "agent": "hr",
                "role_slug": spec.slug,
                "priority": priority_for(spec),
                "status": "pending",
                "scheduled_for": today,
                "created_at": created_at,
                "completed_at": None,
                "gaps": [],
            }
        )

    queue.extend(added)
    queue.sort(key=lambda item: (item["priority"], item["scheduled_for"], item["role_slug"]))
    save_queue(queue)

    counts = Counter(item["priority"] for item in added)
    print("/immortal-genesis-init - Queue Initialized")
    print(f"Queued   : {len(added)} agents (P0: {counts[0]} · P1: {counts[1]} · P2: {counts[2]} · P3: {counts[3]})")
    print(f"Skipped  : {skipped} already present or indexed")
    print(f"Total    : {len(queue)} queue entries")
    print("Next     : /immortal-genesis")
    return 0


def pick_next(queue: list[dict]) -> dict | None:
    in_progress = [item for item in queue if item.get("status") == "in_progress"]
    if in_progress:
        return sorted(in_progress, key=lambda item: (item["priority"], item["scheduled_for"], item["role_slug"]))[0]

    pending = [item for item in queue if item.get("status") == "pending"]
    if pending:
        return sorted(pending, key=lambda item: (item["priority"], item["scheduled_for"], item["role_slug"]))[0]

    return None


def command_status() -> int:
    queue = load_queue()
    if not queue:
        print("Queue not initialized. Run /immortal-genesis init first.")
        return 0

    counts = Counter(item.get("status", "unknown") for item in queue)
    next_item = pick_next(queue)
    current = next_item["role_slug"] if next_item else "none"
    current_priority = f"P{next_item['priority']}" if next_item else "-"

    print("/immortal-genesis - Genesis Build Status")
    print(f"Completed : {counts.get('done', 0)} agents")
    print(f"In progress: {counts.get('in_progress', 0)}")
    print(f"Pending   : {counts.get('pending', 0)} agents")
    print(f"Draft     : {counts.get('draft', 0)} agents")
    print(f"Next      : {current} ({current_priority})")
    print(f"Queue file : {QUEUE_PATH}")
    return 0


def command_next(as_json: bool) -> int:
    queue = load_queue()
    item = pick_next(queue)
    if not item:
        print("Genesis complete. No pending or in-progress roles found.")
        return 0
    if as_json:
        print(json.dumps(item, indent=2, ensure_ascii=True))
        return 0
    print(item["role_slug"])
    return 0


def command_set_status(slug: str, status: str, gaps: list[str]) -> int:
    queue = load_queue()
    target = next((item for item in queue if item.get("role_slug") == slug), None)
    if not target:
        raise SystemExit(f"Role not found in queue: {slug}")

    target["status"] = status
    if status == "done":
        target["completed_at"] = now_iso()
    if status in {"draft", "done"}:
        target["gaps"] = gaps
    save_queue(queue)
    print(f"{slug}: status={status}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Codex-friendly queue runner for Conclave genesis builds.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init")
    sub.add_parser("status")

    next_parser = sub.add_parser("next")
    next_parser.add_argument("--json", action="store_true")

    set_status = sub.add_parser("set-status")
    set_status.add_argument("slug")
    set_status.add_argument("status", choices=["pending", "in_progress", "done", "draft"])
    set_status.add_argument("--gap", action="append", default=[])

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init":
        return command_init()
    if args.command == "status":
        return command_status()
    if args.command == "next":
        return command_next(args.json)
    if args.command == "set-status":
        return command_set_status(args.slug, args.status, args.gap)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
