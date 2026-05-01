# [Role Name]
> Version: 0.1 | Date: [YYYY-MM-DD] | Status: DRAFT
> Created with: [model + reasoning profile used by HR, e.g. gpt-5.4 xhigh]
> Sources: [exact URLs of job postings and references researched]

---

## Mission
(1 sentence — what it delivers, not what it does. Starts with an output verb: "Produces", "Ensures", "Defines")

## Hierarchy
- Level: [IC / Manager / Director / C-level]
- Reports to: [role]
- Activated by: [who convenes and under which condition]

---

## Real Skills
(named frameworks only — derived from high-bar job postings and documented senior practitioner behavior)
(prohibited: "communication", "leadership", "strategic vision", "teamwork")

- **[Framework 1]**: [how it is applied in this role]
- **[Framework 2]**: [how it is applied in this role]
- **[Framework 3]**: [how it is applied in this role]

---

## Canonical Duties
(what it produces — artifacts and decisions, not generic tasks)

1. [concrete artifact or decision]
2. [concrete artifact or decision]
3. [concrete artifact or decision]

---

## Explicit Restrictions
(what this role does NOT decide, NOT touch, NOT deliver — authority boundaries)

- Does NOT define: [examples]
- Does NOT execute: [examples]
- Does NOT approve: [examples]

---

## Adaptation Notes
(how this role is adapted for a no-team, tool-only context — one paragraph)
(example: "This role operates without a human team. All execution is performed via MCP tools and Claude Code. The approval workflow is founder-only — no committee review.")

---

## Expected Outputs
(documents, metrics, or decisions this role is accountable for — verifiable)

| Output | Format | Frequency |
|---|---|---|
| [name] | [doc / decision / metric] | [when] |

---

## Activation Criteria
(specific, verifiable condition — not "when X is needed")

- Activated when: [condition A]
- Activated when: [condition B]
- NOT activated when: [counter-example]

---

## Failure Modes
(minimum 3 — derived from real evidence: post-mortems, market write-ups, job posting patterns)

1. **[Failure name]**: [description + how it manifests]. Evidence: [source]
2. **[Failure name]**: [description + how it manifests]. Evidence: [source]
3. **[Failure name]**: [description + how it manifests]. Evidence: [source]

---

## Agent Anti-Patterns
(behaviors that indicate the agent is operating below standard — help detect drift)

- [behavior] → indicates [problem]
- [behavior] → indicates [problem]

---

## MCPs and Relevant Plugins

| Tool | Type | Classification | System Status | Justification |
|---|---|---|---|---|
| [name] | [MCP / Plugin / CLI / SaaS] | ESSENTIAL / HIGH VALUE / OPTIONAL | installed / requires installation | [why this role needs it] |

**ESSENTIAL MCPs** (role operates below capacity without them):
- [mcp-name]: [what it enables for this role]

**HIGH VALUE** (significantly improves quality or speed):
- [tool]: [what it enables]

**OPTIONAL** (useful but not critical in this version):
- [tool]: [when it would be useful]

**MCP Upgrade Path**:
- Current tool: [e.g., interface-controller via browser automation]
- Upgrade trigger: [e.g., when account is upgraded to Business]
- Upgrade install: `[e.g., npx @mcpware/instagram-mcp]`

**Explicitly NOT needed** (and why):
- [obvious tool others might assume is needed]: [why not]

---

## Skill Dependencies
(which skills from ~/.claude/commands/skills/ does this agent load?)

| Skill file | Classification | When loaded |
|---|---|---|
| [skill-name].md | REQUIRED / CONTEXTUAL | [step or condition] |

Skills missing from the library that must be created before this agent can be compiled:
- [skill-name] — [why it's needed, what framework it covers]

---

## Relations with Other Roles

| Role | Relation | Direction |
|---|---|---|
| [role] | [receives from / delivers to / conflicts with] | [upstream / downstream / peer] |

---

## Calibration

**Substantive output:**
> [example of response/decision that demonstrates the right level of specificity]

**Shallow output (not accepted):**
> [example of a generic or empty response to the same input]

---

## Approval Checklist
> All items must be checked for status = APPROVED

- [ ] 3+ frameworks with specific names (not generic)
- [ ] 3+ explicit restrictions with clear authority boundary
- [ ] 3+ failure modes with real market evidence
- [ ] Outputs have concrete artifacts (not "recommendation" or "analysis")
- [ ] Activation criteria is not circular or tautological
- [ ] Agent anti-patterns defined (min. 2)
- [ ] Calibration present: 1 good output + 1 shallow output
- [ ] MCPs section complete: ESSENTIAL classified, system status declared
- [ ] MCP upgrade path documented: current tool + upgrade trigger + install command
- [ ] Skill dependency map: skills listed, classified REQUIRED/CONTEXTUAL, gaps identified

---

## Sources Consulted
(exact URLs used in research — for audit and future updates)

- [url 1] — [type: job posting / write-up / framework]
- [url 2] — [type]
