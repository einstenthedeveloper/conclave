# ORCHESTRATION.md
> Machine-readable orchestration protocol. Read by agents, not humans. Execute exactly as written.

## CONSTANTS
MAX_QUESTIONS = 3
HALT_THRESHOLD = 0.40
QUESTION_TYPE = binary | constrained
EXECUTION_ORDER = sequential
PARALLEL_ALLOWED = false (unless dependency_overlap = none AND percent_used < 50)
MAX_STRATEGY_FORKS_PER_SESSION = 1
MAX_CONSULTATION_EXCHANGES = 3

## DOCUMENT REGISTRY
VISION.md           owner=CHAIRMAN          required=true     stage=always
EXECUTION_PLAN.md   owner=CEO               required=true     stage=always
TECH.md             owner=CTO               required=false    stage=conditional
GTM.md              owner=CMO               required=false    stage=conditional
TRAFFIC.md          owner=TRAFFIC_MANAGER   required=false    stage=conditional
REVENUE.md          owner=CRO               required=false    stage=conditional
COMMERCIAL.md       owner=CLO               required=false    stage=conditional
SECURITY.md         owner=CISO              required=false    stage=conditional
PRODUCT.md          owner=DESIGN_CTO        required=false    stage=conditional
FINANCE.md          owner=CFO               required=false    stage=post_mvp

## OPERATIONAL REGISTRY (not in main pipeline — activated by founder or CMO)
content_batch.md    owner=SOCIAL_MEDIA_MANAGER  required=false  stage=operational
ROLES/[role].md     owner=HR                    required=false  stage=on_demand

## DEPENDENCY MAP
VISION.md           depends_on=[]
EXECUTION_PLAN.md   depends_on=[VISION.md]
TECH.md             depends_on=[VISION.md, EXECUTION_PLAN.md]
GTM.md              depends_on=[VISION.md, EXECUTION_PLAN.md]
TRAFFIC.md          depends_on=[VISION.md, GTM.md]
REVENUE.md          depends_on=[VISION.md, EXECUTION_PLAN.md]
COMMERCIAL.md       depends_on=[VISION.md, EXECUTION_PLAN.md]
SECURITY.md         depends_on=[VISION.md, TECH.md]
PRODUCT.md          depends_on=[VISION.md, GTM.md]
FINANCE.md          depends_on=[VISION.md, TECH.md, GTM.md, REVENUE.md, COMMERCIAL.md]

## ACTIVATION SIGNALS
SIGNAL: product_exists              → triggers CTO if yes
SIGNAL: distribution_defined        → triggers CMO if no
SIGNAL: revenue_model_defined       → triggers CRO if no
SIGNAL: legal_commercial_complexity → triggers CLO if medium or high
SIGNAL: security_sensitive          → triggers CISO if yes AND TECH.md exists
SIGNAL: ux_critical                 → triggers DESIGN_CTO if yes AND GTM.md exists or CMO active
SIGNAL: traffic_strategy_needed     → triggers TRAFFIC_MANAGER if yes AND GTM.md exists AND TRAFFIC.md does not exist
SIGNAL: funding_intent              → triggers CFO if yes AND stage=post_mvp

## AGENT EXECUTION PROTOCOL
STEP 1  READ      → VISION.md + EXECUTION_PLAN.md + depends_on documents
STEP 2  DERIVE    → extract decisions, assign HIGH | MEDIUM | LOW confidence
STEP 3  SCORE     → if LOW_count / total > 0.40 → emit FRAGILE to CEO, halt
STEP 4  ASK       → binary/constrained only, one at a time, max 3
STEP 5  DECIDE    → deterministic value for every field
STEP 6  WRITE     → output document, confidence next to every decision
STEP 7  FLAG      → list UNRESOLVED_HYPOTHESIS entries
STEP 8  REPORT    → emit to CEO: agent_id, document, decisions, confidence distribution, hypotheses

## CONFLICT CHECK
FOR each field appearing in two documents:
  IF values differ → apply AUTHORITY MAP
  GTM conflicts → CMO wins
  Revenue conflicts → CRO wins
  Technical feasibility → CTO wins (overrides all)
  Legal/compliance → CLO wins (overrides all)
  Request revision from lower-priority agent
  Re-run conflict check
  No dual values allowed in final package

## HALT PROTOCOL
CONDITION A: LOW_decisions / total > 0.40 → FRAGILE → halt pending activations
CONDITION B: product_exists | distribution_defined | revenue_model_defined undefined → BLOCKED → halt immediately
CONDITION C: dependency document missing → activate dependency agent first

## ITERATION LOOP
TRIGGER: experiment failed | revenue=0 | ICP non-response | assumption invalidated
ACTION: re-activate owner agent of failed document only
RULES: agent re-reads all documents before deciding | VISION.md never updated in iteration | CEO logs every iteration

## TOKEN_BUDGET_PROTOCOL
TOOL: conclave-usage-mcp → usage/current
CALL: before any parallel activation decision
THRESHOLDS:
  percent_used < 50   → recommendation = parallel    (eligible if dependency_overlap = none)
  percent_used 50–70  → recommendation = sequential  (sequential always)
  percent_used 70–85  → recommendation = sequential_warn (sequential + notify founder)
  percent_used > 85   → recommendation = pause        (write Execution State, instruct /conc new session)
FALLBACK: if conclave-usage-mcp not installed → default sequential

## STRATEGY_FORK_PROTOCOL
TRIGGER: strategic fork where consequence_level = HIGH
         (affects 2+ downstream agents OR sets a founding constraint)
LIMIT: max 1 per session; lower-consequence forks use binary question protocol
FORMAT:
  [STRATEGIC DECISION — {topic}]
  Option A: {name}
    Approach: {1 sentence}
    Advantage: {primary win in this founder's context}
    Tradeoff: {what is sacrificed or deferred}
    Downstream: {how this constrains other agents}
  Option B: {same structure}
  Option C: {same structure}
  Recommended: Option [X] — {1-sentence rationale tied to VISION.md context}
  Which do you choose? (A / B / C)
POST_SELECTION:
  [You chose Option X.]
  Accepted advantage: {what this unlocks}
  Accepted tradeoffs: {what you are trading away}
  Mitigation approach: {how the system reduces tradeoff impact}
  → Decision locked in EXECUTION_PLAN.md. Will not be re-asked.
FORK_MAP:
  CHAIRMAN  → market category (new category / existing / subcategory)
  CEO       → activation sequence (sequential / parallel given budget and dependency map)
  CTO       → architecture posture (API-first / full-stack / embedded)
  CMO       → GTM motion (PLG / sales-led / community-led)
  CRO       → pricing model (usage-based / seat-based / outcome-based)

## CONSULTATION_PROTOCOL
TRIGGER: C-level has high-confidence strategy but wants specialist validation before writing document
ALLOWED: CMO → Social Media Manager | Traffic Manager
         CTO → Design CTO
         CEO → any C-level (conflict pre-resolution)
FORMAT:
  Agent({
    description: "Validate [decision] against [domain]",
    subagent_type: "[agent-name]",
    prompt: "C-level draft decision: [X]. Does this create a blocker for your domain?
             Return: CLEAR (no blocker) | BLOCKER (specific issue + recommended resolution).
             Under 200 tokens."
  })
RULES:
  - Specialist returns CLEAR or BLOCKER in < 200 tokens
  - C-level incorporates response before writing document
  - Maximum 3 exchanges per consultation — terminate if unresolved → UNRESOLVED_HYPOTHESIS
  - Specialists do not write C-level documents — they validate only
  - Token cost per consultation: ~1,500–4,000 tokens (vs 6,000–15,000 for conflict re-run)

## PARALLEL_MAP
ELIGIBLE pairs (no dependency overlap):
  CMO + CRO        (both depend only on VISION.md + EXECUTION_PLAN.md)
  CTO + CLO        (both depend only on VISION.md + EXECUTION_PLAN.md)
INELIGIBLE pairs (dependency overlap):
  CMO + Design CTO (Design CTO requires GTM.md from CMO)
  CTO + CISO       (CISO requires TECH.md from CTO)
  CMO + Traffic Manager (Traffic Manager requires GTM.md from CMO)
CONDITION: parallel activation requires dependency_overlap = none AND percent_used < 50

## FORBIDDEN
- Agent writing another agent's document
- Agent asking open-ended question
- Agent leaving field empty (use UNRESOLVED_HYPOTHESIS)
- CEO activating agent before dependencies exist
- Parallel execution with dependency overlap
- Parallel execution when percent_used ≥ 50
- System continuing after BLOCKED without founder resolution
- VISION.md updated outside /conclave session
- CFO activation before post_mvp stage
- Dual values on any field after conflict resolution
- Agent applying a framework from memory — load the skill file
- Activating an agent without including skill routing in the CEO brief
- More than 1 STRATEGY_FORK_PROTOCOL per session
- Consultation exchange exceeding 3 rounds — escalate to UNRESOLVED_HYPOTHESIS
