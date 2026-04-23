# ORCHESTRATION.md
> Machine-readable orchestration protocol. Read by agents, not humans. Execute exactly as written.

## CONSTANTS
MAX_QUESTIONS = 3
HALT_THRESHOLD = 0.40
QUESTION_TYPE = binary | constrained
EXECUTION_ORDER = sequential
PARALLEL_ALLOWED = false (unless dependency_overlap = none)

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
execution_log.json  owner=SOCIAL_MEDIA_MANAGER  required=false  stage=operational
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

## FORBIDDEN
- Agent writing another agent's document
- Agent asking open-ended question
- Agent leaving field empty (use UNRESOLVED_HYPOTHESIS)
- CEO activating agent before dependencies exist
- Parallel execution with dependency overlap
- System continuing after BLOCKED without founder resolution
- VISION.md updated outside /conclave session
- CFO activation before post_mvp stage
- Dual values on any field after conflict resolution
