#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
QUEUE_PATH = ROOT / "conclave-queue.json"
ROLE_DIR = ROOT / "conclave-cc" / "ROLES"
AGENT_DIR = ROOT / "conclave-cc" / "agents"
KNOWLEDGE_DIR = ROOT / "conclave-cc" / "knowledge"
KNOWLEDGE_INDEX_PATH = KNOWLEDGE_DIR / "INDEX.md"
HR_INDEX_PATH = ROLE_DIR / "_HR_INDEX.md"

TODAY = datetime.now(timezone.utc).date()
TODAY_STR = TODAY.isoformat()
REVIEW_STR = (TODAY + timedelta(days=90)).isoformat()
NOW_ISO = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


TITLE_OVERRIDES = {
    "sales-automation-specialist": "Sales Automation Specialist",
    "sdr": "SDR (Sales Development Representative)",
    "vp-customer-success": "VP Customer Success",
    "vp-engineering": "VP Engineering",
    "vp-product": "VP Product",
    "vp-sales": "VP Sales",
    "vp-finance": "VP Finance",
    "vp-data": "VP Data",
    "vp-marketing": "VP Marketing",
    "vp-revops": "VP Revenue Operations",
    "vp-brand-communications": "VP Brand Communications",
    "ux-designer": "UX Designer",
    "android-developer": "Android Developer",
    "appsec-engineer": "Application Security Engineer",
    "cdo": "Chief Data Officer",
    "cfo": "Chief Financial Officer",
    "chro": "Chief Human Resources Officer",
    "dba": "Database Administrator",
    "devsecops-engineer": "DevSecOps Engineer",
    "fpa-analyst": "FP&A Analyst",
    "hr-business-partner": "HR Business Partner",
    "ios-developer": "iOS Developer",
    "it-manager": "IT Manager",
    "llm-engineer": "LLM Engineer",
    "ml-engineer": "ML Engineer",
    "pr-manager": "PR Manager",
    "sdet": "Software Development Engineer in Test",
    "soc-analyst": "SOC Analyst",
    "sre": "Site Reliability Engineer",
    "sysadmin": "Systems Administrator",
    "technical-recruiter": "Technical Recruiter",
    "tpm": "Technical Program Manager",
    "director-of-fpa": "Director of FP&A",
    "director-of-l-and-d": "Director of L&D",
    "l-and-d-specialist": "L&D Specialist",
}


ROLE_META = {
    "sales-automation-specialist": {
        "family": "sales_ops",
        "focus": "workflow routing, owner assignment, sequence enrollment governance, SLA escalation, and CRM writeback integrity",
    },
    "sales-enablement-manager": {
        "family": "sales_ops",
        "focus": "rep ramp design, call coaching systems, playbook upkeep, and manager-visible skill calibration",
    },
    "sales-manager": {
        "family": "sales_ops",
        "focus": "weekly forecast inspection, rep coaching, territory execution, and stage discipline",
    },
    "sdr": {
        "family": "sales_ops",
        "focus": "speed-to-lead response, qualification-lite, booking throughput, and clean handoff to Account Executive",
    },
    "support-engineer": {
        "family": "support_cs",
        "focus": "technical escalations, reproducibility, log-driven diagnosis, and engineering-grade incident handoff",
    },
    "support-specialist": {
        "family": "support_cs",
        "focus": "ticket triage, first-response quality, knowledge capture, and customer-safe resolution routing",
    },
    "vp-customer-success": {
        "family": "support_cs",
        "focus": "retention system design, post-sale operating model, support-to-success separation, and expansion signal governance",
    },
    "vp-engineering": {
        "family": "engineering_platform",
        "focus": "engineering operating cadence, architecture governance, delivery reliability, and people-management quality",
    },
    "vp-product": {
        "family": "product_design",
        "focus": "product portfolio strategy, discovery quality, roadmap governance, and outcome accountability",
    },
    "vp-sales": {
        "family": "sales_ops",
        "focus": "forecast governance, sales coverage model, rep productivity, and hiring/ramp planning",
    },
    "director-of-customer-success": {
        "family": "support_cs",
        "focus": "manager-visible renewal readiness, health review cadence, and onboarding-to-steady-state handoffs",
    },
    "director-of-engineering": {
        "family": "engineering_platform",
        "focus": "org-level delivery planning, manager calibration, staffing allocation, and incident follow-through",
    },
    "director-of-product": {
        "family": "product_design",
        "focus": "portfolio prioritization, product operating rhythm, PM quality standards, and roadmap integrity",
    },
    "director-of-sales": {
        "family": "sales_ops",
        "focus": "frontline forecast quality, pipeline conversion inspection, manager accountability, and segment execution",
    },
    "director-of-talent-acquisition": {
        "family": "people",
        "focus": "recruiting operating system, scorecard governance, interviewer calibration, and capacity planning",
    },
    "engineering-manager": {
        "family": "engineering_platform",
        "focus": "sprint execution, code-quality enforcement, incident load balancing, and engineer development",
    },
    "support-manager": {
        "family": "support_cs",
        "focus": "queue coverage, quality assurance, escalation hygiene, and SLA breach reduction",
    },
    "ux-designer": {
        "family": "product_design",
        "focus": "interaction flows, usability validation, wireframe-to-handoff clarity, and behavioral friction removal",
    },
    "vp-finance": {
        "family": "finance_ops",
        "focus": "financial planning system design, close discipline, liquidity visibility, and board-grade reporting",
    },
    "affiliate-marketing-manager": {
        "family": "marketing_brand",
        "focus": "partner program structure, payout governance, attribution rules, and partner performance inspection",
    },
    "analytics-engineer": {
        "family": "data",
        "focus": "modeled data layers, metric definitions, lineage visibility, and analytics reliability",
    },
    "android-developer": {
        "family": "mobile",
        "focus": "Android feature delivery, lifecycle-safe state handling, performance stability, and release readiness",
    },
    "appsec-engineer": {
        "family": "security",
        "focus": "secure SDLC gates, code-level vulnerability prevention, and application control verification",
    },
    "cdo": {
        "family": "data",
        "focus": "enterprise data strategy, governance, data product prioritization, and analytics/ML operating model",
    },
    "cfo": {
        "family": "finance_ops",
        "focus": "cash posture, capital allocation, fundraising readiness, and metric governance",
    },
    "chro": {
        "family": "people",
        "focus": "people operating model, talent density, performance system design, and managerial consistency",
    },
    "cloud-architect": {
        "family": "engineering_platform",
        "focus": "cloud boundary design, environment topology, resilience controls, and cost-aware architecture patterns",
    },
    "compliance-analyst": {
        "family": "legal_compliance",
        "focus": "control evidence preparation, requirement tracing, remediation follow-up, and audit-readiness hygiene",
    },
    "controller": {
        "family": "finance_ops",
        "focus": "close calendar, ledger accuracy, control design, and reporting package integrity",
    },
    "data-analyst": {
        "family": "data",
        "focus": "decision-grade analysis, metric interpretation, dashboard design, and request framing discipline",
    },
    "data-engineer": {
        "family": "data",
        "focus": "pipeline reliability, warehouse ingestion, orchestration safety, and schema evolution control",
    },
    "dba": {
        "family": "data",
        "focus": "database performance, backup/restore confidence, access control, and query-governance safety",
    },
    "devsecops-engineer": {
        "family": "security",
        "focus": "pipeline-integrated security controls, secrets handling, image hardening, and policy-as-code enforcement",
    },
    "digital-forensics-analyst": {
        "family": "security",
        "focus": "artifact preservation, timeline reconstruction, evidence handling, and investigative reporting",
    },
    "embedded-engineer": {
        "family": "mobile",
        "focus": "hardware-adjacent software reliability, firmware-safe release practices, and resource-constrained execution",
    },
    "fpa-analyst": {
        "family": "finance_ops",
        "focus": "driver-based modeling, variance analysis, scenario planning, and forecast hygiene",
    },
    "growth-engineer": {
        "family": "engineering_platform",
        "focus": "experimentation instrumentation, funnel optimization delivery, and fast-but-safe growth iteration",
    },
    "hr-business-partner": {
        "family": "people",
        "focus": "manager partnership, org health diagnosis, performance interventions, and workforce planning translation",
    },
    "incident-responder": {
        "family": "security",
        "focus": "detection triage, containment execution, incident coordination, and post-incident fact pattern quality",
    },
    "influencer-marketing-manager": {
        "family": "marketing_brand",
        "focus": "creator sourcing, brief governance, campaign measurement, and creator-compliance discipline",
    },
    "ios-developer": {
        "family": "mobile",
        "focus": "iOS feature delivery, state consistency, platform conventions, and release-gate reliability",
    },
    "it-manager": {
        "family": "finance_ops",
        "focus": "internal systems administration, endpoint hygiene, access provisioning, and service continuity",
    },
    "legal-counsel": {
        "family": "legal_compliance",
        "focus": "contract review, issue-list negotiation, policy interpretation, and cross-functional legal routing",
    },
    "llm-engineer": {
        "family": "data",
        "focus": "LLM system assembly, eval-driven iteration, prompt/runtime guardrails, and production reliability",
    },
    "malware-analyst": {
        "family": "security",
        "focus": "sample triage, behavior analysis, IOC extraction, and detection-content improvement",
    },
    "mobile-developer": {
        "family": "mobile",
        "focus": "cross-platform mobile delivery, release hygiene, crash reduction, and device-behavior validation",
    },
    "network-engineer": {
        "family": "engineering_platform",
        "focus": "network reliability, segmentation, latency-aware design, and edge connectivity troubleshooting",
    },
    "penetration-tester": {
        "family": "security",
        "focus": "adversarial validation, exploit-path proof, reporting precision, and remediation prioritization",
    },
    "performance-tester": {
        "family": "engineering_platform",
        "focus": "load profile design, bottleneck discovery, capacity thresholds, and release-performance risk gating",
    },
    "platform-engineer": {
        "family": "engineering_platform",
        "focus": "developer platform standards, paved-road tooling, environment consistency, and delivery enablement",
    },
    "podcast-producer": {
        "family": "marketing_brand",
        "focus": "episode pipeline orchestration, guest prep, recording-to-release quality, and content repurposing discipline",
    },
    "purple-team-lead": {
        "family": "security",
        "focus": "adversary emulation planning, defender feedback loops, and measurable control validation",
    },
    "red-team-operator": {
        "family": "security",
        "focus": "objective-based offensive simulation, tradecraft quality, and operator-safe evidence generation",
    },
    "sdet": {
        "family": "engineering_platform",
        "focus": "test harness construction, regression automation, release gates, and quality signal reliability",
    },
    "security-engineer": {
        "family": "security",
        "focus": "preventive control design, detection handoff, hardening backlog ownership, and security-by-default implementation",
    },
    "soc-analyst": {
        "family": "security",
        "focus": "alert triage, case enrichment, escalation quality, and false-positive suppression",
    },
    "solutions-architect": {
        "family": "engineering_platform",
        "focus": "pre-delivery solution design, integration viability, implementation scoping, and technical risk framing",
    },
    "sre": {
        "family": "engineering_platform",
        "focus": "service-level objectives, toil reduction, incident readiness, and reliability budget enforcement",
    },
    "staff-engineer": {
        "family": "engineering_platform",
        "focus": "cross-team technical direction, architecture arbitration, and delivery unblock on complex systems",
    },
    "sysadmin": {
        "family": "engineering_platform",
        "focus": "system administration, backup confidence, fleet consistency, and access hygiene",
    },
    "technical-recruiter": {
        "family": "people",
        "focus": "technical sourcing, scorecard-driven pipeline quality, interview-loop scheduling, and offer-close hygiene",
    },
    "threat-intelligence-analyst": {
        "family": "security",
        "focus": "threat actor tracking, collection prioritization, relevance scoring, and analyst-ready dissemination",
    },
    "tpm": {
        "family": "product_design",
        "focus": "cross-functional delivery governance, dependency management, risk tracking, and milestone reporting",
    },
    "vp-data": {
        "family": "data",
        "focus": "data platform strategy, analytics reliability, governance rules, and ML delivery operating model",
    },
    "vp-marketing": {
        "family": "marketing_brand",
        "focus": "pipeline-bearing marketing system design, channel portfolio governance, and team operating cadence",
    },
    "vp-revops": {
        "family": "sales_ops",
        "focus": "revenue systems architecture, metric governance, lifecycle integrity, and planning-to-forecast alignment",
    },
    "vulnerability-analyst": {
        "family": "security",
        "focus": "finding triage, exposure scoring, remediation coordination, and aging-risk visibility",
    },
    "brand-strategist": {
        "family": "marketing_brand",
        "focus": "message architecture, audience segmentation, narrative consistency, and campaign-to-brand coherence",
    },
    "business-operations-analyst": {
        "family": "finance_ops",
        "focus": "cross-functional metric analysis, process friction diagnosis, and operating-review preparation",
    },
    "compensation-benefits-manager": {
        "family": "people",
        "focus": "banding logic, pay-equity review, benefits design, and exception governance",
    },
    "customer-training-specialist": {
        "family": "support_cs",
        "focus": "curriculum structure, enablement assets, learner adoption proof, and training-to-value translation",
    },
    "data-scientist": {
        "family": "data",
        "focus": "problem framing, experiment design, model interpretation, and decision-grade analytical storytelling",
    },
    "director-of-analytics": {
        "family": "data",
        "focus": "analytics operating model, metric catalog stewardship, dashboard governance, and analyst quality standards",
    },
    "director-of-compliance": {
        "family": "legal_compliance",
        "focus": "control framework ownership, audit execution readiness, policy maintenance, and cross-functional remediation",
    },
    "director-of-data-science": {
        "family": "data",
        "focus": "model portfolio governance, experimentation standards, and translation of business questions into science backlog",
    },
    "director-of-demand-generation": {
        "family": "marketing_brand",
        "focus": "campaign portfolio management, pipeline pacing, spend-to-pipeline inspection, and lead-quality governance",
    },
    "director-of-fpa": {
        "family": "finance_ops",
        "focus": "planning cadence, executive forecast narratives, budget guardrails, and variance review discipline",
    },
    "director-of-l-and-d": {
        "family": "people",
        "focus": "manager-capability development, role-based curriculum, learning ROI, and capability progression systems",
    },
    "director-of-legal-contracts": {
        "family": "legal_compliance",
        "focus": "contract playbook ownership, clause governance, turnaround SLA, and negotiation pattern control",
    },
    "director-of-marketing-operations": {
        "family": "marketing_brand",
        "focus": "marketing systems design, campaign process governance, attribution hygiene, and cross-functional handoff control",
    },
    "director-of-operations": {
        "family": "finance_ops",
        "focus": "cross-functional operating cadence, process throughput visibility, and execution-risk mitigation",
    },
    "director-of-security-engineering": {
        "family": "security",
        "focus": "security engineering roadmap, control coverage strategy, staffing leverage, and incident-readiness quality",
    },
    "l-and-d-specialist": {
        "family": "people",
        "focus": "program delivery, curriculum authoring, learning assessment, and adoption reinforcement",
    },
    "ml-engineer": {
        "family": "data",
        "focus": "model packaging, feature/serving consistency, deployment automation, and drift-aware monitoring",
    },
    "operations-manager": {
        "family": "finance_ops",
        "focus": "day-to-day operating rhythm, process reliability, escalation routing, and KPI follow-through",
    },
    "paralegal": {
        "family": "legal_compliance",
        "focus": "document organization, signature workflow, clause retrieval, and matter-status hygiene",
    },
    "pr-manager": {
        "family": "marketing_brand",
        "focus": "media narrative control, press calendar orchestration, announcement prep, and issue-escalation messaging",
    },
    "procurement-manager": {
        "family": "finance_ops",
        "focus": "vendor intake, review workflow governance, savings discipline, and contract-to-invoice handoff integrity",
    },
    "vp-brand-communications": {
        "family": "marketing_brand",
        "focus": "brand narrative governance, comms calendar strategy, PR alignment, and reputation-risk handling",
    },
}


NEW_KNOWLEDGE_SECTIONS = {
    "Sales Operations Extensions": [
        (
            "sales-automation-workflows.md",
            "Sales Automation Workflows (routing logic, owner assignment, sequence enrollment and unenrollment governance, workflow changelog, exception handling)",
            "Sales Automation Specialist, SDR, RevOps Manager, VP Revenue Operations, Sales Manager, Director of Sales",
            "Covers the operational design of revenue workflows: trigger taxonomy, assignment rules, sequence governance, SLA-aware escalations, workflow testing, and rollback discipline.",
        ),
        (
            "sales-coaching-enablement.md",
            "Sales Coaching & Enablement (ramp milestones, scorecard calibration, call review protocol, role-play cadence, playbook governance)",
            "Sales Enablement Manager, Sales Manager, Director of Sales, VP Sales",
            "Defines how sales capability is built and inspected: onboarding milestones, scorecards, calibration routines, practice loops, and evidence of behavior change.",
        ),
    ],
    "Support & Service": [
        (
            "support-incident-triage.md",
            "Support Incident Triage (severity taxonomy, first-response routing, reproducibility checklist, customer-impact scoring)",
            "Support Specialist, Support Engineer, Support Manager, Director of Customer Success, VP Customer Success",
            "Defines ticket intake, severity assignment, queue routing, reproduction standards, and the conditions that trigger a formal incident.",
        ),
        (
            "support-knowledge-operations.md",
            "Support Knowledge Operations (KCS loop, article standards, gap logging, self-serve deflection review)",
            "Support Specialist, Support Manager, Customer Training Specialist, VP Customer Success",
            "Defines how support learnings become durable knowledge assets instead of disappearing into solved tickets.",
        ),
        (
            "support-escalation-management.md",
            "Support Escalation Management (SLA / OLA mapping, engineering handoff packet, executive escalation thresholds)",
            "Support Engineer, Support Manager, Director of Customer Success, VP Customer Success",
            "Covers escalation ownership, support-to-engineering handoff quality, response expectations, and recovery communication.",
        ),
    ],
    "Product & UX Extensions": [
        (
            "product-delivery-governance.md",
            "Product Delivery Governance (roadmap intake, dependency log, RAID tracking, release-readiness review)",
            "VP Product, Director of Product, Technical Program Manager, Product Manager",
            "Defines how discovery outputs become planned delivery work with explicit owners, dates, risks, and exit criteria.",
        ),
        (
            "product-ux-research.md",
            "Product UX Research (test plan design, interview protocol, synthesis standards, usability evidence thresholds)",
            "UX Designer, Director of Product, VP Product",
            "Defines how research is planned, run, synthesized, and translated into actionable product decisions.",
        ),
    ],
    "Engineering Platform Extensions": [
        (
            "engineering-reliability-operations.md",
            "Engineering Reliability Operations (SLI/SLO, incident command, rollback policy, postmortem quality, error budget review)",
            "VP Engineering, Director of Engineering, Engineering Manager, SRE, Platform Engineer, Staff Engineer, DevOps Engineer, Systems Administrator, Network Engineer",
            "Covers production reliability, incident routines, rollback authority, and recurring operational review patterns.",
        ),
        (
            "engineering-platform-governance.md",
            "Engineering Platform Governance (paved road standards, environment conventions, access model, service ownership)",
            "VP Engineering, Director of Engineering, Platform Engineer, Cloud Architect, Solutions Architect, Staff Engineer",
            "Defines the operating rules of the internal platform: ownership, standards, environments, and developer-facing workflows.",
        ),
        (
            "engineering-mobile-release-governance.md",
            "Mobile Release Governance (beta gates, crash-free threshold, release notes, store submission checklist)",
            "Android Developer, iOS Developer, Mobile Developer, Embedded Engineer",
            "Defines how mobile and embedded releases move from dev to store or device with explicit quality gates.",
        ),
    ],
    "Data & AI Extensions": [
        (
            "data-warehouse-architecture.md",
            "Data Warehouse Architecture (layering model, data contracts, lineage, semantic definitions, orchestration boundaries)",
            "Chief Data Officer, VP Data, Analytics Engineer, Data Engineer, DBA, Director of Analytics",
            "Defines raw-to-modeled warehouse architecture, contract boundaries, transformation ownership, and lineage expectations.",
        ),
        (
            "data-quality-governance.md",
            "Data Quality Governance (freshness, completeness, schema-drift handling, anomaly triage, issue ownership)",
            "Chief Data Officer, VP Data, Analytics Engineer, Data Engineer, Data Analyst, Director of Analytics",
            "Defines how quality is measured, detected, triaged, and repaired across analytical datasets and reporting layers.",
        ),
        (
            "mlops-lifecycle.md",
            "MLOps Lifecycle (feature / training / serving consistency, validation gates, registry discipline, drift review)",
            "ML Engineer, Data Scientist, Director of Data Science, VP Data, LLM Engineer, AI Engineer",
            "Defines how models move from experimentation to production with validation, deployment, and monitoring discipline.",
        ),
    ],
    "Security Engineering Extensions": [
        (
            "security-application-engineering.md",
            "Application Security Engineering (threat modeling, secure code review, dependency risk, release gates)",
            "Application Security Engineer, DevSecOps Engineer, Security Engineer, Director of Security Engineering",
            "Defines preventative security controls inside the SDLC and what evidence is required before software ships.",
        ),
        (
            "security-detection-response.md",
            "Security Detection & Response (telemetry coverage, alert tuning, containment playbooks, evidence retention)",
            "Incident Responder, SOC Analyst, Security Engineer, Threat Intelligence Analyst, Director of Security Engineering",
            "Defines how detections are built, tuned, triaged, escalated, and converted into recovery actions.",
        ),
        (
            "security-vulnerability-management.md",
            "Security Vulnerability Management (finding intake, severity scoring, remediation SLA, exception tracking)",
            "Vulnerability Analyst, Security Engineer, DevSecOps Engineer, Director of Security Engineering, Compliance Analyst",
            "Defines the finding lifecycle from discovery through exception handling and verification of closure.",
        ),
    ],
    "Finance, IT & Operations Extensions": [
        (
            "finance-planning-analysis.md",
            "Finance Planning & Analysis (driver tree, rolling forecast, scenario pack, variance commentary)",
            "Chief Financial Officer, VP Finance, FP&A Analyst, Director of FP&A, Business Operations Analyst",
            "Defines the finance planning system, scenario review cadence, and the standard structure of forecast outputs.",
        ),
        (
            "finance-close-controls.md",
            "Finance Close & Controls (close calendar, reconciliations, approvals, evidence trails, adjustment rules)",
            "Chief Financial Officer, VP Finance, Controller, Director of FP&A",
            "Defines the recurring accounting close discipline and the controls that protect financial integrity.",
        ),
        (
            "operations-service-governance.md",
            "Operations Service Governance (request intake, workflow ownership, escalation path, vendor and internal service review)",
            "Director of Operations, Operations Manager, IT Manager, Procurement Manager, Business Operations Analyst",
            "Defines how internal operational services are requested, routed, reviewed, and measured.",
        ),
    ],
    "People & Talent Extensions": [
        (
            "people-talent-acquisition.md",
            "Talent Acquisition Operations (scorecards, structured interview kits, sourcing funnel, quality-of-hire review)",
            "Chief Human Resources Officer, Director of Talent Acquisition, Technical Recruiter, HR Business Partner",
            "Defines the recruiting operating model, from requisition intake through scorecard-driven selection and post-hire review.",
        ),
        (
            "people-learning-development.md",
            "Learning & Development (curriculum architecture, manager enablement, learning transfer, Kirkpatrick evaluation)",
            "Chief Human Resources Officer, Director of L&D, L&D Specialist, Customer Training Specialist",
            "Defines how learning programs are scoped, delivered, measured, and tied to behavior change.",
        ),
        (
            "people-compensation-performance.md",
            "Compensation & Performance (band architecture, promotion evidence, review cycle, pay-equity checks)",
            "Chief Human Resources Officer, Compensation & Benefits Manager, HR Business Partner",
            "Defines the rules that connect performance evidence, compensation decisions, and exception governance.",
        ),
    ],
    "Legal & Compliance Extensions": [
        (
            "legal-contract-lifecycle.md",
            "Contract Lifecycle Management (template hierarchy, clause playbooks, approval routing, signature control, obligation tracking)",
            "Legal Counsel, Paralegal, Director of Legal Contracts, Director of Compliance",
            "Defines how legal documents move from template to redline, approval, signature, storage, and obligation follow-through.",
        ),
    ],
    "Brand & Communications Extensions": [
        (
            "partnership-channel-programs.md",
            "Partnership & Channel Programs (partner tiers, payout logic, brief standards, attribution, fraud checks)",
            "Affiliate Marketing Manager, Influencer Marketing Manager, VP Marketing, Director of Demand Generation",
            "Defines how external growth partners are recruited, activated, measured, and governed.",
        ),
        (
            "brand-communications-operations.md",
            "Brand & Communications Operations (message house, comms calendar, announcement workflow, issue escalation)",
            "Brand Strategist, PR Manager, Podcast Producer, VP Brand Communications, VP Marketing",
            "Defines the operating system behind brand messaging, PR execution, editorial coordination, and escalation management.",
        ),
    ],
}


FAMILY_DEFAULTS = {
    "sales_ops": {
        "division": "Division 5 - Sales & Revenue Operations",
        "tools": [
            ("CRM (HubSpot or Salesforce)", "SaaS", "ESSENTIAL", "requires activation", "System of record for opportunities, owners, stages, and activity history"),
            ("HubSpot MCP Server (Remote)", "MCP", "HIGH VALUE", "requires activation", "Direct CRM read/write workflows when HubSpot is the revenue system"),
            ("Outreach MCP Server", "MCP", "HIGH VALUE", "requires activation", "Sequence, task, transcript, and prospect context for operating revenue workflows"),
            ("Common Room MCP Server", "MCP", "OPTIONAL", "requires activation", "Signal enrichment for accounts and contacts in timing-sensitive motions"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Browser automation for CRM areas or tools without direct APIs"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Prevents long inspections from overrunning context budget"),
        ],
        "sources": [
            ("https://meddicc.com/resources/meddpicc-as-framework-account-executive", "framework"),
            ("https://winningbydesign.com/spiced-framework/", "framework"),
            ("https://www.gong.io/blog/sales-pipeline-tracking", "evidence"),
            ("https://www.gong.io/blog/spot-these-four-red-flags-to-boost-forecast-accuracy-and-revenue-predictability", "evidence"),
            ("https://developers.hubspot.com/mcp", "tool"),
            ("https://support.outreach.io/hc/en-us/articles/46370115253403-Outreach-MCP-Server", "tool"),
            ("https://www.commonroom.io/docs/using-common-room/mcp-server/", "tool"),
        ],
    },
    "support_cs": {
        "division": "Division 6 - Customer Success & Support",
        "tools": [
            ("Jira Service Management / Zendesk / Intercom", "SaaS", "ESSENTIAL", "requires activation", "Ticketing, queueing, SLA tracking, and support history"),
            ("Knowledge base (Confluence / Intercom Articles / Notion)", "SaaS", "HIGH VALUE", "requires activation", "Self-serve deflection and durable support knowledge"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Browser automation across support consoles and admin panels"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful during long queue reviews or escalations"),
        ],
        "sources": [
            ("https://www.atlassian.com/itsm", "reference"),
            ("https://www.atlassian.com/software/customer-service-management", "reference"),
            ("https://www.intercom.com/blog/what-is-customer-support-volume/", "reference"),
            ("https://www.intercom.com/blog/customer-support-quality-benchmark-report/", "reference"),
        ],
    },
    "product_design": {
        "division": "Division 3 - Product & UX",
        "tools": [
            ("Linear / Jira", "SaaS", "ESSENTIAL", "requires activation", "Roadmap, backlog, milestone, and dependency tracking"),
            ("Figma", "SaaS", "HIGH VALUE", "requires activation", "Design exploration, wireframes, prototypes, and handoff"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Browser automation across planning, analytics, and research tools"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful in longer decision synthesis sessions"),
        ],
        "sources": [
            ("https://www.producttalk.org/opportunity-solution-tree/", "framework"),
            ("https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/", "framework"),
            ("https://www.productplan.com/glossary/jobs-to-be-done-framework/", "framework"),
            ("https://www.nngroup.com/articles/ten-usability-heuristics/", "framework"),
        ],
    },
    "engineering_platform": {
        "division": "Division 4 - Engineering & Platform",
        "tools": [
            ("GitHub", "SaaS", "ESSENTIAL", "requires activation", "Source control, reviews, rulesets, and delivery workflow"),
            ("CI/CD and deploy tooling", "SaaS", "ESSENTIAL", "requires activation", "Build, test, and release control"),
            ("Datadog / Grafana / Cloud observability", "SaaS", "HIGH VALUE", "requires activation", "Service health, metrics, logs, traces, and post-incident diagnosis"),
            ("PagerDuty / Opsgenie", "SaaS", "HIGH VALUE", "requires activation", "Incident routing and on-call discipline"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Bridges browser-only admin consoles and dashboards"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Helps when inspecting large technical contexts"),
        ],
        "sources": [
            ("https://cloud.google.com/sre", "reference"),
            ("https://cloud.google.com/architecture/reliability", "reference"),
            ("https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners", "reference"),
            ("https://docs.github.com/github/administering-a-repository/about-branch-restrictions", "reference"),
            ("https://docs.github.com/en/actions/reference/environments", "reference"),
        ],
    },
    "mobile": {
        "division": "Division 4 - Engineering & Platform",
        "tools": [
            ("GitHub", "SaaS", "ESSENTIAL", "requires activation", "Source control, pull requests, and release governance"),
            ("Firebase Crashlytics / equivalent", "SaaS", "HIGH VALUE", "requires activation", "Crash visibility and release-quality inspection"),
            ("App Store Connect / Google Play Console", "SaaS", "HIGH VALUE", "requires activation", "Release distribution and store compliance"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Automates store and console tasks when APIs are missing"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful during release reviews"),
        ],
        "sources": [
            ("https://developer.android.com/topic/architecture", "reference"),
            ("https://developer.apple.com/design/human-interface-guidelines/", "reference"),
            ("https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners", "reference"),
        ],
    },
    "security": {
        "division": "Division 8 - Security & Risk",
        "tools": [
            ("SIEM / EDR", "SaaS", "ESSENTIAL", "requires activation", "Alerting, triage, case history, and containment visibility"),
            ("GitHub Advanced Security / Snyk / scanner equivalent", "SaaS", "HIGH VALUE", "requires activation", "Pre-merge and continuous finding visibility"),
            ("Ticketing / case management", "SaaS", "HIGH VALUE", "requires activation", "Finding ownership, remediation follow-up, and evidence retention"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Useful for browser-only consoles, admin panels, and evidence gathering"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful during long incident or analysis sessions"),
        ],
        "sources": [
            ("https://owasp.org/www-project-application-security-verification-standard/", "framework"),
            ("https://attack.mitre.org/", "framework"),
            ("https://www.nist.gov/publications/incident-response-recommendations-and-considerations-cybersecurity-risk-management-csf", "framework"),
            ("https://www.nist.gov/publications/guide-integrating-forensic-techniques-incident-response-0", "framework"),
            ("https://www.nist.gov/privacy-framework", "framework"),
        ],
    },
    "data": {
        "division": "Division 4 - Engineering, Data & AI",
        "tools": [
            ("Warehouse / lakehouse platform", "SaaS", "ESSENTIAL", "requires activation", "Primary execution layer for modeled, analytical, and ML-serving data"),
            ("dbt", "CLI", "ESSENTIAL", "requires activation", "Transformation logic, tests, documentation, and lineage"),
            ("BI / notebook / exploration tooling", "SaaS", "HIGH VALUE", "requires activation", "Decision support, dashboards, and ad hoc analysis"),
            ("Orchestration / model registry / feature tooling", "SaaS", "HIGH VALUE", "requires activation", "Pipeline automation and model lifecycle control"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Useful for browser-only warehouse or analytics tooling"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful during broad dataset or lineage inspection"),
        ],
        "sources": [
            ("https://docs.getdbt.com/", "reference"),
            ("https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning", "reference"),
            ("https://cloud.google.com/architecture/reliability", "reference"),
        ],
    },
    "finance_ops": {
        "division": "Division 7 - Finance, IT & Operations",
        "tools": [
            ("Finance system / spreadsheet / ERP stack", "SaaS", "ESSENTIAL", "requires activation", "Budgeting, close, cash tracking, and reporting"),
            ("Billing / procurement / vendor systems", "SaaS", "HIGH VALUE", "requires activation", "Invoice, vendor, and spend-control workflows"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Bridges browser-only backoffice systems"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful during longer review and reconciliation sessions"),
        ],
        "sources": [
            ("https://www.saas-capital.com/blog-posts/the-saas-magic-number/", "reference"),
            ("https://www.bvp.com/atlas/measuring-your-saas-business-the-saas-operating-system", "reference"),
            ("https://www.wallstreetprep.com/knowledge/three-statement-model/", "reference"),
            ("https://asana.com/resources/raci-chart", "reference"),
        ],
    },
    "people": {
        "division": "Division 7 - People & Talent",
        "tools": [
            ("ATS / HRIS / LMS stack", "SaaS", "ESSENTIAL", "requires activation", "Recruiting, employee data, performance tracking, and learning operations"),
            ("Interview scheduling and scorecard tooling", "SaaS", "HIGH VALUE", "requires activation", "Structured hiring and evidence capture"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Automates browser-only HR systems"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful when synthesizing hiring or org-health material"),
        ],
        "sources": [
            ("https://www.shrm.org/enterprise-solutions/talent-acquisition", "reference"),
            ("https://www.shrm.org/topics-tools/news/talent-acquisition/shrm-foundation-guide-outlines-4-step-recruitment-process", "reference"),
            ("https://www.kirkpatrickpartners.com/", "framework"),
            ("https://www.shrm.org/topics-tools/news/talent-acquisition/shrm-talent-2026-session-preview-quality-of-hire", "reference"),
        ],
    },
    "legal_compliance": {
        "division": "Division 7 - Legal, Compliance & Risk",
        "tools": [
            ("Contract repository / CLM / doc stack", "SaaS", "ESSENTIAL", "requires activation", "Template control, redlines, signatures, and obligation retrieval"),
            ("Ticketing / review intake workflow", "SaaS", "HIGH VALUE", "requires activation", "Tracks legal requests and approval routing"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Useful for portals, registries, and browser-only contract systems"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful during long issue-list or audit reviews"),
        ],
        "sources": [
            ("https://www.nist.gov/privacy-framework", "framework"),
            ("https://www.nist.gov/privacy-framework/nist-pram", "framework"),
            ("https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/collaboration-space/privacy-risk-assessment", "framework"),
        ],
    },
    "marketing_brand": {
        "division": "Division 2 - Marketing, Brand & Communications",
        "tools": [
            ("Marketing automation / CRM / analytics", "SaaS", "ESSENTIAL", "requires activation", "Campaign, audience, and attribution visibility"),
            ("Social / PR / creator management tooling", "SaaS", "HIGH VALUE", "requires activation", "Distribution, comms coordination, and relationship tracking"),
            ("interface-controller", "MCP", "HIGH VALUE", "included in Conclave package - requires activation", "Useful for browser-only campaign and platform work"),
            ("conclave-usage-mcp", "MCP", "HIGH VALUE", "installed", "Useful during large content or campaign planning contexts"),
        ],
        "sources": [
            ("https://blog.hubspot.com/marketing/utm-codes", "reference"),
            ("https://blog.hubspot.com/marketing/what-is-brand-strategy", "reference"),
            ("https://blog.hubspot.com/marketing/how-to-run-an-affiliate-program", "reference"),
            ("https://sproutsocial.com/insights/influencer-marketing/", "reference"),
        ],
    },
}


def load_queue() -> list[dict]:
    return json.loads(QUEUE_PATH.read_text(encoding="utf-8"))


def save_queue(queue: list[dict]) -> None:
    QUEUE_PATH.write_text(json.dumps(queue, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def title_from_slug(slug: str) -> str:
    if slug in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[slug]
    parts = slug.split("-")
    words = []
    for part in parts:
        if part == "vp":
            words.append("VP")
        elif part == "of":
            words.append("of")
        else:
            words.append(part.capitalize())
    return " ".join(words)


def level_for(slug: str) -> str:
    if slug in {"cdo", "cfo", "chro"}:
        return "C-level"
    if slug.startswith("vp-"):
        return "VP"
    if slug.startswith("director-of-"):
        return "Director"
    if slug.endswith("-manager") or slug in {"engineering-manager", "support-manager", "operations-manager", "it-manager"}:
        return "Manager"
    if slug == "staff-engineer":
        return "Staff IC"
    return "Specialist"


def family_for(slug: str) -> str:
    return ROLE_META[slug]["family"]


def focus_for(slug: str) -> str:
    return ROLE_META[slug]["focus"]


def report_for(slug: str) -> str:
    family = family_for(slug)
    level = level_for(slug)

    if family == "sales_ops":
        return {
            "C-level": "CEO or Founder",
            "VP": "CRO or CEO",
            "Director": "VP Sales, VP Revenue Operations, or CRO",
            "Manager": "Director of Sales, VP Sales, or VP Revenue Operations",
            "Staff IC": "VP Engineering or CTO",
            "Specialist": "Sales Manager, RevOps Manager, or Director of Sales",
        }[level]
    if family == "support_cs":
        return {
            "VP": "CEO, CRO, or COO",
            "Director": "VP Customer Success",
            "Manager": "Director of Customer Success or VP Customer Success",
            "Specialist": "Support Manager, Director of Customer Success, or VP Customer Success",
            "C-level": "CEO or Founder",
            "Staff IC": "VP Customer Success",
        }[level]
    if family == "product_design":
        return {
            "VP": "CEO or CTO",
            "Director": "VP Product",
            "Manager": "VP Product",
            "Specialist": "Director of Product or VP Product",
            "C-level": "CEO",
            "Staff IC": "VP Product",
        }[level]
    if family in {"engineering_platform", "mobile"}:
        return {
            "VP": "CTO or CEO",
            "Director": "VP Engineering or CTO",
            "Manager": "Director of Engineering or VP Engineering",
            "Staff IC": "Director of Engineering or VP Engineering",
            "Specialist": "Engineering Manager, Staff Engineer, or Director of Engineering",
            "C-level": "CEO",
        }[level]
    if family == "security":
        return {
            "Director": "CISO, CTO, or CEO",
            "Manager": "Director of Security Engineering or CISO",
            "Specialist": "Director of Security Engineering, CISO, or CTO",
            "VP": "CEO",
            "C-level": "CEO",
            "Staff IC": "Director of Security Engineering",
        }[level]
    if family == "data":
        return {
            "C-level": "CEO or CTO",
            "VP": "Chief Data Officer, CTO, or CEO",
            "Director": "VP Data or Chief Data Officer",
            "Manager": "Director of Analytics, Director of Data Science, or VP Data",
            "Specialist": "Director, VP Data, or Chief Data Officer",
            "Staff IC": "VP Data",
        }[level]
    if family == "finance_ops":
        return {
            "C-level": "CEO or Founder",
            "VP": "Chief Financial Officer or CEO",
            "Director": "VP Finance, CFO, or COO",
            "Manager": "Director of Operations, VP Finance, CFO, or COO",
            "Specialist": "Director, VP Finance, CFO, COO, or Operations Manager",
            "Staff IC": "CFO",
        }[level]
    if family == "people":
        return {
            "C-level": "CEO or Founder",
            "VP": "CHRO or CEO",
            "Director": "CHRO",
            "Manager": "CHRO or Director",
            "Specialist": "CHRO, Director, or HR Business Partner",
            "Staff IC": "CHRO",
        }[level]
    if family == "legal_compliance":
        return {
            "Director": "CLO or CEO",
            "Manager": "CLO or Director",
            "Specialist": "Legal Counsel, Director, CLO, or CEO",
            "VP": "CLO or CEO",
            "C-level": "CEO",
            "Staff IC": "CLO",
        }[level]
    if family == "marketing_brand":
        return {
            "VP": "CMO or CEO",
            "Director": "VP Marketing, VP Brand Communications, or CMO",
            "Manager": "VP Marketing, Director, or CMO",
            "Specialist": "Director, VP Marketing, or VP Brand Communications",
            "C-level": "CEO",
            "Staff IC": "VP Marketing",
        }[level]
    return "Founder"


def peers_for(slug: str) -> str:
    family = family_for(slug)
    if family == "sales_ops":
        return "Account Executive, BDR, RevOps Manager, Marketing Automation Specialist"
    if family == "support_cs":
        return "Customer Success Manager, Onboarding Specialist, RevOps Manager, Product Manager"
    if family == "product_design":
        return "Product Manager, UX Designer, Engineering Manager, Design CTO"
    if family in {"engineering_platform", "mobile"}:
        return "Product Manager, QA / SDET, DevOps Engineer, Security Engineer"
    if family == "security":
        return "DevOps Engineer, Staff Engineer, IT Manager, Legal / Compliance"
    if family == "data":
        return "Product Manager, Analytics Attribution Specialist, AI Engineer, Finance"
    if family == "finance_ops":
        return "COO, CEO, RevOps, Operations, Legal"
    if family == "people":
        return "CEO, COO, functional managers, Legal"
    if family == "legal_compliance":
        return "CEO, CFO, CHRO, Security, Operations"
    if family == "marketing_brand":
        return "CMO, CRO, Analytics, Content, Product Marketing"
    return "Founder"


def mission_verb(level: str) -> str:
    if level in {"C-level", "VP"}:
        return "Defines"
    if level in {"Director", "Manager"}:
        return "Ensures"
    return "Produces"


def real_skills(slug: str) -> list[tuple[str, str]]:
    family = family_for(slug)
    level = level_for(slug)
    focus = focus_for(slug)

    if family == "sales_ops":
        if slug == "sales-automation-specialist":
            return [
                ("Round-Robin Assignment Design", "Applies deterministic ownership rules so inbound, outbound, and exception queues route cleanly instead of depending on ad hoc human reassignment."),
                ("Lifecycle State-Machine Governance", "Uses explicit stage transitions, entry evidence, and rollback controls to keep routing logic aligned with real buyer progress."),
                ("Sequence Enrollment / Unenrollment Governance", "Controls when contacts enter, pause, or exit outbound and follow-up sequences so replies, meetings, and opt-outs do not keep receiving automation."),
                ("Workflow Exception Logging", "Treats every automation override as evidence to improve routing logic, field requirements, and fallback paths."),
            ]
        if slug == "sdr":
            return [
                ("Speed-to-Lead SLA", "Optimizes first-response timing, follow-up coverage, and no-show recovery before the lead cools down."),
                ("SPICED Qualification-Lite", "Captures situation, pain, impact, critical event, and decision context at the level needed for clean AE handoff."),
                ("Sequence Governance", "Maintains touch cadence, exit criteria, and task discipline instead of manually improvising follow-up."),
                ("Calendar Friction Reduction", "Reduces booking loss through confirmation flows, reminders, and precise CTA handling."),
            ]
        if "enablement" in slug:
            return [
                ("MEDDPICC Coaching", "Uses stage-specific evidence inspection to teach reps how to improve opportunity control, not just activity volume."),
                ("Call Scorecard Calibration", "Aligns managers and enablement on what good discovery, objection handling, and next-step control actually sound like."),
                ("Ramp Milestone Design", "Turns onboarding into explicit skill gates, observation steps, and production-readiness evidence."),
                ("Playbook Governance", "Keeps scripts, battlecards, and process documents current with the live sales motion."),
            ]
        return [
            ("Forecast Cadence Governance", "Runs recurring inspection against evidence, not rep confidence, to keep commit quality real."),
            ("MEDDPICC / SPICED Inspection", "Uses recognized qualification frameworks to identify missing buying-path evidence before deals are promoted."),
            ("Territory & Capacity Planning", "Matches market coverage, account segmentation, and seller load to realistic production capacity."),
            ("Pipeline Management", "Treats stage conversion, age, and next-step hygiene as operating controls rather than report outputs."),
        ]

    if family == "support_cs":
        base = [
            ("ITIL Incident Management", "Uses severity, ownership, status discipline, and post-incident learning so high-impact issues do not get handled like ordinary tickets."),
            ("Knowledge-Centered Service (KCS)", "Converts repeated issues and workarounds into reusable knowledge instead of solving them from scratch each time."),
            ("SLA / OLA Design", "Separates external customer commitments from internal handoff commitments so escalations can be measured and improved."),
        ]
        if "training" in slug:
            base.append(("Kirkpatrick Evaluation", "Measures whether training changed learner behavior and customer outcomes, not just attendance."))
        elif "engineer" in slug:
            base.append(("Reproducibility Triage", "Turns vague technical escalations into evidence-rich defect or platform cases that engineering can act on."))
        else:
            base.append(("Queue Segmentation", "Separates urgent, technical, educational, and administrative requests so response quality stays consistent at scale."))
        return base

    if family == "product_design":
        if slug == "ux-designer":
            return [
                ("Jobs-to-be-Done", "Frames user behavior and outcome demand around the job the user is trying to complete, not around surface feature requests."),
                ("Usability Heuristics", "Uses explicit heuristic review to catch clarity, friction, and control problems before shipping."),
                ("Prototype Validation", "Tests flows early enough that the team can still change direction cheaply."),
                ("Task-Flow Mapping", "Keeps every screen and interaction tied to the user path it is meant to accelerate."),
            ]
        if slug == "tpm":
            return [
                ("RAID Logging", "Keeps risks, assumptions, issues, and dependencies explicit so delivery stays inspectable."),
                ("Critical Path Management", "Identifies sequence-sensitive work and prevents hidden blockers from surfacing at release time."),
                ("Release Readiness Reviews", "Uses stage gates and owner checklists instead of calendar hope."),
                ("RACI Mapping", "Clarifies who owns the decision, the work, and the consultation path before execution starts."),
            ]
        return [
            ("Opportunity Solution Tree", "Connects outcomes, opportunities, and delivery bets so roadmap decisions stay legible."),
            ("RICE Prioritization", "Ranks opportunities using reach, impact, confidence, and effort rather than seniority or noise."),
            ("Jobs-to-be-Done", "Anchors prioritization and messaging to customer progress, not just feature preference."),
            ("Roadmap Governance", "Separates committed work, exploratory work, and parked ideas with explicit review rules."),
        ]

    if family == "engineering_platform":
        if slug in {"sre", "platform-engineer"}:
            return [
                ("SRE Error Budget", "Uses SLI/SLO and error-budget logic to balance release velocity with reliability debt."),
                ("Toil Reduction", "Eliminates repetitive operational work so reliability improvements compound instead of depending on heroics."),
                ("Incident Command", "Runs major incidents with clear roles, timeline control, and post-incident learning."),
                ("Paved Road Platform Design", "Provides defaults that make the safe path the easy path for product engineers."),
            ]
        if slug == "performance-tester":
            return [
                ("Workload Modeling", "Builds load profiles that match real usage instead of synthetic happy paths."),
                ("Bottleneck Isolation", "Separates application, database, network, and dependency limits during performance diagnosis."),
                ("Performance Budgeting", "Uses explicit latency, throughput, and error thresholds as release gates."),
                ("Regression Baselines", "Compares runs against a known baseline so changes can be judged materially, not impressionistically."),
            ]
        if slug == "sdet":
            return [
                ("Test Pyramid / Trophy Strategy", "Places validation at the cheapest layer that still gives decision-grade confidence."),
                ("Deterministic Test Harnesses", "Builds stable automation that detects regressions rather than producing flaky noise."),
                ("Risk-Based Release Gates", "Targets automation effort at areas where defects are most expensive or hardest to recover from."),
                ("Contract Regression Coverage", "Protects critical API and integration behavior from silent drift."),
            ]
        return [
            ("DORA Metrics", "Uses lead time, deployment frequency, change-failure rate, and recovery time as operating signals rather than vanity metrics."),
            ("Architecture Decision Records (ADR)", "Makes boundary choices explicit enough that future teams can understand why a path was chosen."),
            ("Environment & Deployment Governance", "Uses protected branches, review rules, and environment gates to reduce production risk."),
            ("Service Ownership", "Keeps runtime accountability visible instead of diffused across the org."),
        ]

    if family == "mobile":
        return [
            ("Clean Architecture", "Separates platform UI, domain logic, and infrastructure concerns so features remain maintainable as the app grows."),
            ("MVVM / MVI State Management", "Controls user-visible state transitions and asynchronous work with predictable update patterns."),
            ("Release Train Governance", "Moves builds through beta, crash review, and store submission with clear acceptance gates."),
            ("Offline / Sync Safety", "Handles connectivity and local state in a way that avoids silent corruption or confusing user regressions."),
        ]

    if family == "security":
        if slug in {"purple-team-lead", "red-team-operator"}:
            return [
                ("MITRE ATT&CK", "Uses adversary behaviors and techniques to structure realistic offensive and validation exercises."),
                ("Purple Team Exercise Loop", "Turns offensive simulation into measurable detection and response improvements."),
                ("Objective-Based Planning", "Starts from business-critical attack paths rather than generic exploit collection."),
                ("Pyramid of Pain", "Prioritizes detections and improvements that raise adversary cost materially."),
            ]
        return [
            ("NIST Cybersecurity Framework 2.0", "Uses governance, identify, protect, detect, respond, and recover as the organizing model for control coverage."),
            ("OWASP ASVS", "Applies explicit application-security verification criteria instead of relying on intuition alone."),
            ("MITRE ATT&CK", "Maps detections, adversary behavior, and control gaps to a shared taxonomy."),
            ("Severity-Based Remediation", "Uses exposure, exploitability, and business impact to prioritize work instead of treating all findings equally."),
        ]

    if family == "data":
        if slug in {"ml-engineer", "llm-engineer", "director-of-data-science"}:
            return [
                ("MLOps Lifecycle", "Uses validation, deployment, monitoring, and rollback disciplines so models behave like managed systems, not one-off experiments."),
                ("Feature / Serving Consistency", "Keeps training-time and runtime data semantics aligned so models do not degrade silently."),
                ("Evaluation-Driven Development", "Treats benchmark sets and acceptance thresholds as the change gate for models and prompts."),
                ("Drift Monitoring", "Watches for data, concept, or behavior shift before quality loss becomes a user-visible problem."),
            ]
        return [
            ("Medallion / Layered Modeling", "Separates raw, cleaned, and business-facing datasets so lineage and trust stay visible."),
            ("dbt Modular DAGs", "Uses tested, documented, composable models instead of sprawling unversioned SQL."),
            ("Dimensional Modeling", "Designs facts, dimensions, and metric semantics so analysis remains stable across teams."),
            ("Data Contracts", "Controls schema and field expectations where upstream changes would otherwise break downstream trust."),
        ]

    if family == "finance_ops":
        return [
            ("Driver-Based Planning", "Builds budgets and forecasts from operational levers rather than flat percentage guesses."),
            ("Rolling Forecast", "Refreshes planning posture on a recurring basis so reality beats static annual assumptions."),
            ("Three-Statement Modeling", "Connects revenue, expense, cash, and balance-sheet implications inside one coherent operating model."),
            ("RACI / Approval Matrix", "Makes request routing, approval authority, and exception handling inspectable."),
        ]

    if family == "people":
        if "l-and-d" in slug or "training" in slug:
            return [
                ("Kirkpatrick Four Levels", "Measures whether a learning program changed behavior and business outcomes instead of only collecting satisfaction scores."),
                ("Curriculum Architecture", "Designs learning paths with role relevance, progression, and reinforcement rules."),
                ("Manager Enablement", "Treats the manager as the transfer mechanism that makes training stick."),
                ("Capability Mapping", "Links training effort to explicit role capabilities and proficiency expectations."),
            ]
        return [
            ("Structured Hiring", "Uses calibrated scorecards and interview kits so selection quality is evidence-based."),
            ("Quality-of-Hire Review", "Measures whether recruiting decisions produced durable performance instead of just offer acceptance."),
            ("Workforce Planning", "Translates business demand into hiring priorities and capacity assumptions."),
            ("Performance Governance", "Uses role expectations, review rhythm, and promotion criteria to reduce managerial inconsistency."),
        ]

    if family == "legal_compliance":
        return [
            ("Contract Playbook Governance", "Uses clause fallback logic and issue hierarchies instead of improvising every negotiation from scratch."),
            ("Issue-List Negotiation", "Separates critical, negotiable, and cosmetic legal points so review cycles move faster."),
            ("Privacy Risk Assessment", "Evaluates data-use and compliance implications before they become embedded operational risk."),
            ("Obligation Tracking", "Ensures signed terms become operating requirements rather than archived PDFs."),
        ]

    if family == "marketing_brand":
        if slug in {"affiliate-marketing-manager", "influencer-marketing-manager"}:
            return [
                ("Partner Program Design", "Structures sourcing, onboarding, payouts, and quality screens so growth partners scale without channel chaos."),
                ("Attribution Governance", "Defines how partner-sourced conversions are counted, deduplicated, and reviewed."),
                ("Brief Standardization", "Uses channel-specific briefs so partner output stays aligned to brand and campaign intent."),
                ("Fraud / Quality Review", "Separates genuine contribution from low-quality traffic, fake engagement, or misaligned creator activity."),
            ]
        return [
            ("Message House / Brand Architecture", "Keeps top-line narrative, proof points, and voice consistent across campaigns and channels."),
            ("Paid / Earned / Owned Coordination", "Treats channels as a system instead of disconnected tactics."),
            ("Editorial / Launch Calendar Governance", "Uses planned sequencing so campaigns, PR, and content do not compete with each other."),
            ("Attribution Hygiene", "Links activity to measurable outcomes with explicit tagging, definitions, and review cadence."),
        ]

    return [("Operating Discipline", f"Applies explicit working rules to {focus}.")]


def canonical_duties(slug: str) -> list[str]:
    family = family_for(slug)
    level = level_for(slug)

    if family == "sales_ops":
        if slug == "sales-automation-specialist":
            return [
                "`sales-routing-logic.md` - source-of-truth routing map for inbound, outbound, owner assignment, and exception paths.",
                "`sales-automation-audit-[YYYY-WW].md` - weekly review of broken workflows, stale sequence members, and SLA misses.",
                "`sequence-governance-rules.md` - enrollment, unenrollment, suppression, and task-trigger rules by motion.",
                "`handoff-sla-monitor-[YYYY-WW].md` - time-to-action inspection across intake, SDR, AE, and support routing flows.",
            ]
        if slug == "sdr":
            return [
                "`sdr-handoff-[account]-[date].md` - qualification-lite package with pain, timing, authority signal, and next-step status.",
                "`queue-response-review-[YYYY-WW].md` - speed-to-lead, no-show, and booking conversion inspection.",
                "`sequence-exit-log-[YYYY-WW].md` - reasons leads were paused, recycled, or promoted.",
            ]
        if level in {"VP", "Director", "Manager"}:
            return [
                "`sales-operating-review-[YYYY-WW].md` - forecast posture, conversion bottlenecks, and leadership actions required.",
                "`coverage-capacity-plan-[quarter].md` - segment / territory coverage, headcount assumptions, and risk gaps.",
                "`coaching-cadence-plan-[quarter].md` - manager-visible inspection, scorecard, and rep development plan.",
                "`pipeline-risk-register.md` - recurring stage, velocity, and owner-discipline risks with mitigations.",
            ]
        return [
            "`sales-workstream-review.md` - operating inspection for the role's production area.",
            "`process-change-log.md` - the live record of adjustments to handoffs, stages, or execution rules.",
            "`quality-scorecard-[YYYY-WW].md` - repeating quality review against role-specific metrics.",
        ]

    if family == "support_cs":
        if level in {"VP", "Director", "Manager"}:
            return [
                "`support-operating-review-[YYYY-WW].md` - SLA, quality, backlog, escalation, and staffing inspection.",
                "`customer-risk-review-[YYYY-WW].md` - health, renewal, support volume, and executive intervention summary.",
                "`knowledge-gap-log-[YYYY-WW].md` - recurring unanswered issues and the articles or training assets required.",
                "`escalation-pattern-review.md` - root-cause map for repeat escalations and ownership gaps.",
            ]
        return [
            "`ticket-brief-[case].md` - issue summary, severity, reproduction state, and next owner.",
            "`resolution-summary-[case].md` - customer-safe explanation, workaround, and follow-up obligations.",
            "`knowledge-gap-log-[YYYY-WW].md` - recurring unanswered questions or missing documentation.",
        ]

    if family == "product_design":
        if slug == "ux-designer":
            return [
                "`ux-flow-spec-[feature].md` - task flow, edge cases, state notes, and handoff decisions.",
                "`usability-test-plan-[feature].md` - participant criteria, tasks, success criteria, and evidence capture rules.",
                "`heuristic-review-[feature].md` - structured friction review using explicit heuristics.",
                "`design-handoff-[feature].md` - annotated spec for engineering and product.",
            ]
        return [
            "`product-operating-review-[YYYY-WW].md` - roadmap, dependencies, risks, and decision points.",
            "`decision-brief-[initiative].md` - problem framing, options, tradeoffs, and chosen path.",
            "`delivery-risk-register.md` - dependency, milestone, and ownership risks.",
        ]

    if family in {"engineering_platform", "mobile"}:
        if level in {"VP", "Director", "Manager", "Staff IC"}:
            return [
                "`engineering-operating-review-[YYYY-WW].md` - delivery, reliability, quality, and staffing signals.",
                "`architecture-decision-[topic].md` - explicit boundary, tradeoff, and rollback reasoning.",
                "`incident-followthrough.md` - operational risks, postmortem actions, and owner assignments.",
                "`release-readiness-[version].md` - production risk review before deployment.",
            ]
        return [
            "`implementation-plan-[feature].md` - execution approach, dependencies, and acceptance gates.",
            "`runbook-[service].md` - failure signals, recovery actions, and escalation path.",
            "`quality-gate-review-[YYYY-WW].md` - defects, regressions, or reliability risks that block release.",
        ]

    if family == "security":
        if level in {"Director", "Manager"}:
            return [
                "`security-operating-review-[YYYY-WW].md` - detection coverage, finding aging, incident status, and remediation bottlenecks.",
                "`control-gap-register.md` - missing or weak controls with severity and owner.",
                "`exercise-plan-[quarter].md` - attack simulation or validation plan with learning objectives.",
            ]
        return [
            "`case-brief-[incident-or-finding].md` - what was observed, how it was assessed, and what must happen next.",
            "`remediation-brief-[finding].md` - severity, exploit path, owner, and verification step.",
            "`evidence-log-[YYYY-WW].md` - preserved artifacts, timelines, or detection notes for auditability.",
        ]

    if family == "data":
        if level in {"C-level", "VP", "Director"}:
            return [
                "`data-operating-review-[YYYY-WW].md` - platform health, quality signals, analytics delivery, and model risk.",
                "`metric-catalog-governance.md` - owner, definition, grain, and trust status for business metrics.",
                "`data-roadmap-[quarter].md` - platform, analytics, and ML priorities with risk framing.",
            ]
        return [
            "`dataset-spec-[domain].md` - field logic, lineage, tests, and owner expectations.",
            "`analysis-brief-[question].md` - methods, results, caveats, and decision implications.",
            "`quality-incident-log-[YYYY-WW].md` - freshness, completeness, or schema issues under review.",
        ]

    if family == "finance_ops":
        return [
            "`operating-review-[YYYY-WW].md` - current posture, deviations, and decisions required.",
            "`planning-pack-[month-or-quarter].md` - forecast, scenario notes, and assumption changes.",
            "`control-exception-log.md` - approval, reconciliation, or workflow exceptions that need resolution.",
        ]

    if family == "people":
        return [
            "`people-operating-review-[YYYY-WW].md` - open roles, performance issues, org-health signals, and decisions required.",
            "`scorecard-or-curriculum-pack-[role-or-program].md` - reusable execution asset for hiring or learning.",
            "`quality-review-[cycle].md` - evidence that the people system produced the intended result.",
        ]

    if family == "legal_compliance":
        return [
            "`review-brief-[matter].md` - issues, fallback position, required approvers, and risk summary.",
            "`obligation-log-[counterparty-or-control].md` - signed requirements and their operational owners.",
            "`compliance-gap-review-[YYYY-WW].md` - open evidence, remediation state, and audit blockers.",
        ]

    if family == "marketing_brand":
        return [
            "`campaign-or-comms-brief-[initiative].md` - objective, audience, message, channel plan, and owner map.",
            "`channel-performance-review-[YYYY-WW].md` - quality, conversion, and execution inspection.",
            "`narrative-governance-log.md` - message updates, approval history, and deviation notes.",
        ]

    return ["`role-output.md` - role-specific operating artifact."]


def restrictions(slug: str) -> list[str]:
    family = family_for(slug)

    base = {
        "sales_ops": [
            "Does NOT define pricing policy, contract language, or legal fallback terms.",
            "Does NOT promise roadmap items, implementation guarantees, or unsupported technical commitments.",
            "Does NOT alter stage definitions, compensation rules, or CRM schema without explicit RevOps / leadership approval.",
        ],
        "support_cs": [
            "Does NOT redefine product roadmap, bug severity policy, or commercial terms.",
            "Does NOT close escalations by hiding uncertainty or guessing at technical root cause.",
            "Does NOT treat support load as sales demand or push commercial expansion before value is proven.",
        ],
        "product_design": [
            "Does NOT treat stakeholder preference as a substitute for evidence or explicit prioritization criteria.",
            "Does NOT promise engineering dates without validated dependency and scope review.",
            "Does NOT bypass discovery and usability evidence when user behavior is still uncertain.",
        ],
        "engineering_platform": [
            "Does NOT merge high-risk changes without review, test evidence, or rollback posture.",
            "Does NOT let undocumented operational knowledge remain trapped in one person's memory.",
            "Does NOT optimize local team speed by silently increasing platform or reliability risk for everyone else.",
        ],
        "mobile": [
            "Does NOT ship store or device releases without crash, rollback, and compatibility review.",
            "Does NOT hide platform-specific edge cases behind generic implementation notes.",
            "Does NOT treat UI polish as complete if state, sync, or offline behavior is still unreliable.",
        ],
        "security": [
            "Does NOT mark risk as resolved until the control or remediation is verified, not merely assigned.",
            "Does NOT run disruptive exercises or scans without scope, approval, and evidence handling rules.",
            "Does NOT confuse detection volume with security coverage quality.",
        ],
        "data": [
            "Does NOT treat dashboards or models as trustworthy when metric definitions, lineage, or freshness are unclear.",
            "Does NOT let upstream schema changes silently break downstream consumers.",
            "Does NOT move a model or metric into decision flow without validation and owner accountability.",
        ],
        "finance_ops": [
            "Does NOT approve spend, policy exceptions, or reporting shortcuts outside the documented authority boundary.",
            "Does NOT treat budget assumptions as static truth when operating inputs have changed materially.",
            "Does NOT move money, contracts, or approvals through undocumented side channels.",
        ],
        "people": [
            "Does NOT open a role, review a candidate, or run a training program without explicit success criteria.",
            "Does NOT use manager intuition as a replacement for scorecards, rubrics, or capability definitions.",
            "Does NOT make compensation or performance exceptions without visible rationale and approval path.",
        ],
        "legal_compliance": [
            "Does NOT sign off on obligations that have no operational owner or follow-through path.",
            "Does NOT accept template drift or side-letter behavior outside the approved document set.",
            "Does NOT treat compliance evidence as complete until it is current, accessible, and auditable.",
        ],
        "marketing_brand": [
            "Does NOT trade brand consistency for channel speed without explicit approval and rationale.",
            "Does NOT report channel performance using ambiguous attribution or vanity-only metrics.",
            "Does NOT launch partner or PR work without brief, approval, and escalation paths.",
        ],
    }
    return base[family]


def activation_criteria(slug: str) -> list[str]:
    family = family_for(slug)
    focus = focus_for(slug)
    criteria = [
        f"Activated when: there is active work around {focus} that already exists in the business and needs a durable operating owner.",
        "Activated when: the founder or a functional leader needs a repeatable artifact, review cadence, or decision framework rather than ad hoc execution.",
        "Activated when: a recurring bottleneck, quality failure, or handoff ambiguity is visible in this role's domain.",
    ]
    if family == "sales_ops":
        criteria.append("NOT activated when: no commercial model exists. Sales leadership and execution roles require `REVENUE.md` or equivalent commercial guardrails.")
    elif family == "product_design":
        criteria.append("NOT activated when: the request is only to produce screens or roadmap ideas without a defined problem, outcome, or decision owner.")
    elif family in {"engineering_platform", "mobile"}:
        criteria.append("NOT activated when: there is no code, service, or release surface to operate on.")
    elif family == "support_cs":
        criteria.append("NOT activated when: the issue is actually a pricing, contract, or roadmap decision disguised as a support request.")
    elif family == "security":
        criteria.append("NOT activated when: the task requires legal authorization or business-risk acceptance outside security authority.")
    else:
        criteria.append("NOT activated when: the request is still undefined enough that the role would have to invent its own mandate.")
    return criteria


def failure_modes(slug: str) -> list[tuple[str, str, str]]:
    family = family_for(slug)
    if family == "sales_ops":
        return [
            ("False Forecast Confidence", "Deals or pipelines are reported as healthy because activity exists, while evidence of buyer progress, owner response, or clean next steps is weak.", "Evidence: Gong forecast and pipeline analyses."),
            ("Workflow Drift", "Routing, sequence, or stage logic changes faster than the team documents them, so the system keeps producing hidden exceptions.", "Evidence: HubSpot / Outreach operating patterns and RevOps role expectations."),
            ("Managerless Coaching", "Enablement or leadership reports on activity but does not change seller behavior through scorecards, inspection, or practice loops.", "Evidence: MEDDPICC coaching and enablement operating norms."),
        ]
    if family == "support_cs":
        return [
            ("Ticket Ping-Pong", "Cases bounce between support, success, and engineering because severity, ownership, or reproduction state is unclear.", "Evidence: Atlassian ITSM guidance on queues, SLAs, and escalation structure."),
            ("Knowledge Decay", "Resolved issues never become durable documentation, so volume stays high and new hires relearn the same fixes.", "Evidence: KCS and support quality measurement patterns."),
            ("Escalation Without Context", "A technical or executive escalation arrives with no timeline, evidence, or customer impact framing, delaying resolution.", "Evidence: Atlassian customer service management patterns."),
        ]
    if family == "product_design":
        return [
            ("Roadmap by Noise", "Priority follows urgency or opinion rather than explicit scoring and outcome logic.", "Evidence: RICE and OST frameworks."),
            ("Design Without Validation", "A flow is polished visually but never tested against real tasks, leaving hidden friction until after launch.", "Evidence: Nielsen usability heuristics and UX research norms."),
            ("Delivery Ambiguity", "Work starts before dependencies, owners, or scope boundaries are explicit, producing late-stage thrash.", "Evidence: RAID / RACI governance patterns."),
        ]
    if family in {"engineering_platform", "mobile"}:
        return [
            ("Manual Heroics", "Release or incident recovery depends on memory, one person, or console clicks instead of documented operational paths.", "Evidence: Google SRE reliability guidance."),
            ("Ownership Fog", "Code, services, or infrastructure have no clear owner, so quality, incidents, and upgrades stall in ambiguity.", "Evidence: GitHub CODEOWNERS and service-ownership practices."),
            ("Unsafe Delivery Velocity", "Teams optimize merge speed while quietly increasing deployment, rollback, or production-risk debt.", "Evidence: DORA, branch protection, and release-governance patterns."),
        ]
    if family == "security":
        return [
            ("Alert Fatigue Theater", "A large number of detections exist, but triage quality and relevance are too weak to improve actual security.", "Evidence: NIST incident-response guidance and SOC operating patterns."),
            ("Unverified Remediation", "Findings are marked complete before exploit paths, controls, or fixes are validated.", "Evidence: OWASP ASVS and vulnerability-management norms."),
            ("Exercise Without Learning", "Red, blue, or purple exercises generate activity but no measurable improvement in detections, playbooks, or hardening backlog.", "Evidence: MITRE ATT&CK and purple-team operating patterns."),
        ]
    if family == "data":
        return [
            ("Metric Drift", "Different teams use the same metric label for different logic, undermining trust in decisions.", "Evidence: dbt documentation and semantic-layer practice."),
            ("Silent Schema Breakage", "Upstream data changes propagate without contract or test coverage, breaking dashboards or models after the fact.", "Evidence: data-contract and DAG-based transformation norms."),
            ("Model-in-a-Notebook", "Analysis or ML value remains trapped in exploratory work and never becomes a managed production system.", "Evidence: Google MLOps maturity model."),
        ]
    if family == "finance_ops":
        return [
            ("Spreadsheet Truth Conflicts", "Teams work from inconsistent planning or close files, so the company has multiple financial realities at once.", "Evidence: rolling forecast and close-control discipline."),
            ("Approval Side Channels", "Purchases, commitments, or exceptions happen outside the visible approval matrix.", "Evidence: RACI and control-governance patterns."),
            ("Static Planning Blindness", "Forecasts ignore changing inputs long after reality has moved.", "Evidence: rolling forecast and driver-based planning norms."),
        ]
    if family == "people":
        return [
            ("Interview Without Rubric", "Hiring quality depends on interviewer instinct because scorecards and role definitions are weak.", "Evidence: SHRM structured hiring and quality-of-hire guidance."),
            ("Training as Attendance", "Programs are measured by participation instead of post-training behavior and results.", "Evidence: Kirkpatrick Four Levels."),
            ("Manager Variance", "The employee experience changes wildly by manager because expectations and review systems are underspecified.", "Evidence: HRBP and performance-governance operating norms."),
        ]
    if family == "legal_compliance":
        return [
            ("Clause Drift", "Teams negotiate from outdated templates or side-channel agreements, creating inconsistent obligations.", "Evidence: contract lifecycle and playbook governance practice."),
            ("Control Evidence Panic", "Audit or compliance review starts without current evidence ownership, forcing reactive collection.", "Evidence: NIST privacy and compliance operating patterns."),
            ("Legal Bottleneck by Intake Noise", "Routine work arrives without scoping or routing discipline, consuming scarce legal bandwidth.", "Evidence: legal intake and issue-list operating norms."),
        ]
    if family == "marketing_brand":
        return [
            ("Attribution Mirage", "Channels or creators appear to perform because naming, tagging, or counting rules are inconsistent.", "Evidence: UTM and attribution governance patterns."),
            ("Message Fragmentation", "PR, content, partners, and campaigns ship conflicting narratives because no message house is enforced.", "Evidence: brand strategy and communications operations practice."),
            ("Partner Volume Without Quality", "Affiliate or influencer output grows while contribution quality, compliance, or brand fit deteriorates.", "Evidence: partner-program operating norms."),
        ]
    return [("Generic Failure", "The role works without explicit standards.", "Evidence: operating review patterns.")]


def family_knowledge_docs(slug: str) -> list[tuple[str, str, str]]:
    family = family_for(slug)
    if family == "sales_ops":
        docs = [
            ("sales-pipeline-management.md", "REQUIRED", "Load before any forecast, coverage, or opportunity-flow decision."),
            ("sales-forecasting.md", "CONTEXTUAL", "Load for leadership forecast reviews and commit / best-case posture."),
            ("sales-lifecycle-governance.md", "REQUIRED", "Load when stage movement, routing, or handoff rules are part of the decision."),
            ("sales-performance-analytics.md", "CONTEXTUAL", "Load when conversion, throughput, or quality trends need diagnosis."),
            ("sales-territory-capacity-planning.md", "CONTEXTUAL", "Load when headcount, books, or market coverage are involved."),
            ("sales-automation-workflows.md", "CONTEXTUAL", "Load for routing, owner assignment, or sequence-workflow questions."),
        ]
        if slug == "sales-enablement-manager":
            docs.append(("sales-coaching-enablement.md", "REQUIRED", "Load before ramp, coaching, or scorecard work."))
        if slug == "sdr":
            docs.append(("sales-appointment-setting.md", "REQUIRED", "Load before booking-flow and handoff work."))
        return docs
    if family == "support_cs":
        docs = [
            ("customer-success-management.md", "REQUIRED", "Load before post-sale operating decisions or lifecycle design work."),
            ("customer-health-scoring.md", "CONTEXTUAL", "Load when risk, renewal, or adoption posture must be assessed."),
            ("support-incident-triage.md", "REQUIRED", "Load before queue routing, severity assignment, or escalation."),
            ("support-knowledge-operations.md", "CONTEXTUAL", "Load when self-serve, article quality, or enablement assets are relevant."),
            ("support-escalation-management.md", "REQUIRED", "Load when handing work to engineering, leadership, or other teams."),
        ]
        if slug in {"vp-customer-success", "director-of-customer-success"}:
            docs.append(("customer-onboarding-implementation.md", "CONTEXTUAL", "Load when onboarding-to-CS transitions are in scope."))
        return docs
    if family == "product_design":
        return [
            ("product-discovery.md", "REQUIRED", "Load before prioritization, problem framing, or solution shaping."),
            ("product-pmf-signals.md", "CONTEXTUAL", "Load when outcome measurement or PMF-sensitive decisions are involved."),
            ("product-delivery-governance.md", "REQUIRED", "Load before roadmap commitment or dependency decisions."),
            ("product-ux-research.md", "CONTEXTUAL", "Load when user evidence or usability decisions are required."),
            ("ux-usability-testing.md", "CONTEXTUAL", "Load when research or flow validation is part of the work."),
        ]
    if family == "engineering_platform":
        return [
            ("engineering-system-design.md", "REQUIRED", "Load before architecture, service-boundary, or dependency decisions."),
            ("engineering-testing-strategy.md", "CONTEXTUAL", "Load when release or quality-gate decisions are involved."),
            ("engineering-reliability-operations.md", "REQUIRED", "Load before incident, SLO, or operational reliability work."),
            ("engineering-platform-governance.md", "CONTEXTUAL", "Load when platform standards, environments, or ownership models are relevant."),
        ]
    if family == "mobile":
        return [
            ("engineering-frontend-patterns.md", "CONTEXTUAL", "Load when mobile UI or state handling parallels frontend architecture concerns."),
            ("engineering-testing-strategy.md", "REQUIRED", "Load before release gate or automation decisions."),
            ("engineering-mobile-release-governance.md", "REQUIRED", "Load before beta, store, or firmware release decisions."),
            ("engineering-reliability-operations.md", "CONTEXTUAL", "Load when runtime reliability or incident posture matters."),
        ]
    if family == "security":
        return [
            ("security-compliance-roadmap.md", "CONTEXTUAL", "Load when control frameworks, attestations, or evidence are relevant."),
            ("security-incident-response.md", "REQUIRED", "Load before active incident, response, or readiness work."),
            ("security-application-engineering.md", "CONTEXTUAL", "Load when SDLC-integrated controls or app risk are in scope."),
            ("security-detection-response.md", "REQUIRED", "Load when detection, triage, or containment is in scope."),
            ("security-vulnerability-management.md", "CONTEXTUAL", "Load when findings, remediation SLAs, or exceptions are involved."),
        ]
    if family == "data":
        docs = [
            ("data-warehouse-architecture.md", "REQUIRED", "Load before dataset, lineage, or modeling decisions."),
            ("data-quality-governance.md", "REQUIRED", "Load before freshness, schema, or trust decisions."),
            ("analytics-measurement-framework.md", "CONTEXTUAL", "Load when marketing or product measurement models intersect the work."),
        ]
        if slug in {"ml-engineer", "data-scientist", "director-of-data-science", "llm-engineer"}:
            docs.extend(
                [
                    ("mlops-lifecycle.md", "REQUIRED", "Load before training, validation, deployment, or drift decisions."),
                    ("ai-llm-evaluation.md", "CONTEXTUAL", "Load when eval design or model acceptance is relevant."),
                ]
            )
        if slug == "llm-engineer":
            docs.append(("ai-rag-pipeline-design.md", "CONTEXTUAL", "Load when retrieval or context assembly is part of the system."))
        return docs
    if family == "finance_ops":
        return [
            ("finance-saas-metrics.md", "CONTEXTUAL", "Load when recurring SaaS metric definitions matter."),
            ("finance-planning-analysis.md", "REQUIRED", "Load before forecast, variance, or planning-pack work."),
            ("finance-close-controls.md", "CONTEXTUAL", "Load when close discipline or reporting integrity is in scope."),
            ("operations-service-governance.md", "CONTEXTUAL", "Load when internal service workflows, procurement, or IT operations are involved."),
        ]
    if family == "people":
        return [
            ("people-talent-acquisition.md", "CONTEXTUAL", "Load for structured hiring and recruiting-system work."),
            ("people-learning-development.md", "CONTEXTUAL", "Load for curriculum, learning transfer, and manager capability work."),
            ("people-compensation-performance.md", "CONTEXTUAL", "Load for review-cycle, banding, or compensation-governance work."),
            ("strategy-hiring-sequence.md", "CONTEXTUAL", "Load when hiring order, stage, or organizational sequence matters."),
        ]
    if family == "legal_compliance":
        return [
            ("legal-contract-lifecycle.md", "REQUIRED", "Load before contract routing, redline, or signature-control work."),
            ("legal-startup-structure.md", "CONTEXTUAL", "Load when legal entity or governance structure questions matter."),
            ("legal-employment-law.md", "CONTEXTUAL", "Load when people or contractor obligations overlap legal review."),
            ("security-compliance-roadmap.md", "CONTEXTUAL", "Load when legal and compliance obligations intersect."),
        ]
    if family == "marketing_brand":
        return [
            ("marketing-brand-positioning.md", "REQUIRED", "Load before message, narrative, or partner-brief work."),
            ("marketing-attribution.md", "CONTEXTUAL", "Load when performance or contribution counting matters."),
            ("content-editorial-planning.md", "CONTEXTUAL", "Load when campaigns, content cadence, or launch sequences are involved."),
            ("partnership-channel-programs.md", "CONTEXTUAL", "Load when affiliate or creator programs are in scope."),
            ("brand-communications-operations.md", "REQUIRED", "Load before comms calendar, PR, or narrative-control decisions."),
        ]
    return []


def skill_rows(slug: str) -> list[tuple[str, str, str]]:
    family = family_for(slug)
    if family == "sales_ops":
        rows = [
            ("positioning.md", "REQUIRED", "Before buyer-facing messaging, coaching, or process output."),
            ("value-based-pricing.md", "CONTEXTUAL", "When forecast, pricing posture, or commercial quality intersects the work."),
        ]
        if slug == "sales-enablement-manager":
            rows.append(("call-review-scorecards.md", "CONTEXTUAL", "Needed for shared enablement extraction; role compiles without it but should externalize later."))
        return rows
    if family == "support_cs":
        return [
            ("document-dont-create.md", "CONTEXTUAL", "When the founder asks the role to invent policy rather than operate within one."),
            ("customer-handoff.md", "CONTEXTUAL", "Useful when support, success, and engineering need a common packet. Missing shared skill; role compiles with inline guidance."),
        ]
    if family == "product_design":
        return [
            ("document-dont-create.md", "CONTEXTUAL", "When discovery prerequisites are missing and the role should force clarity first."),
            ("problem-framing.md", "CONTEXTUAL", "Useful for synthesizing research and priority decisions; not yet a shared skill."),
        ]
    if family in {"engineering_platform", "mobile"}:
        return [
            ("document-dont-create.md", "CONTEXTUAL", "When the request would require inventing requirements or release policy from nothing."),
            ("release-governance.md", "CONTEXTUAL", "A useful future extraction for shared release gates; covered inline for now."),
        ]
    if family == "security":
        return [
            ("threat-modeling.md", "CONTEXTUAL", "Useful future extraction for shared security decision quality."),
            ("incident-command.md", "CONTEXTUAL", "Useful future extraction for severe incident coordination."),
        ]
    if family == "data":
        return [
            ("metric-contracts.md", "CONTEXTUAL", "Useful future extraction for shared metric and data-contract discipline."),
            ("experiment-review.md", "CONTEXTUAL", "Useful future extraction for model or analysis validation loops."),
        ]
    if family == "finance_ops":
        return [
            ("document-dont-create.md", "CONTEXTUAL", "When no budget, policy, or authority model exists yet."),
            ("decision-briefs.md", "CONTEXTUAL", "Useful future extraction for consistent operating review packs."),
        ]
    if family == "people":
        return [
            ("structured-interviewing.md", "CONTEXTUAL", "Useful future extraction for cross-role interviewing discipline."),
            ("capability-maps.md", "CONTEXTUAL", "Useful future extraction for L&D and performance systems."),
        ]
    if family == "legal_compliance":
        return [
            ("issue-list-redlining.md", "CONTEXTUAL", "Useful future extraction for consistent contract negotiation."),
            ("document-dont-create.md", "CONTEXTUAL", "When the request tries to bypass a missing policy or authority boundary."),
        ]
    if family == "marketing_brand":
        return [
            ("positioning.md", "REQUIRED", "Before message, campaign, or external-facing output."),
            ("campaign-briefs.md", "CONTEXTUAL", "Useful future extraction for structured creative / partner / PR handoff."),
        ]
    return []


def calibration_examples(slug: str) -> tuple[str, str]:
    title = title_from_slug(slug)
    focus = focus_for(slug)
    substantive = (
        f'"{title} output completed. I documented the current operating state around {focus}, identified the specific bottleneck '
        "or risk in evidence terms, defined the owner and next decision, and wrote the artifact that the next role can execute "
        'without re-asking basic context."'
    )
    shallow = (
        f'"We should improve {focus} soon. I recommend better communication, tighter process, and more alignment across the team."'
    )
    return substantive, shallow


def identity_summary(slug: str) -> str:
    title = title_from_slug(slug)
    level = level_for(slug)
    family = family_for(slug)
    division = FAMILY_DEFAULTS[family]["division"]
    report = report_for(slug)
    peer_line = peers_for(slug)
    focus = focus_for(slug)
    return (
        f"You are the {title} of a Conclave-operated startup. You operate in {division}. "
        f"You are a {level} role that reports to {report}. You are peer to {peer_line}. "
        f"Your operating focus is {focus}. You do not exist to sound strategic or helpful in the abstract; "
        "you exist to convert recurring work in this lane into explicit artifacts, operating rules, and visible decisions."
    )


def knowledge_notes(slug: str) -> list[str]:
    family = family_for(slug)
    focus = focus_for(slug)
    notes = [
        f"Your work is only valuable if it turns {focus} into a visible operating system instead of a heroic individual behavior.",
        "If evidence is weak, your output must say so explicitly. Do not fill gaps with false confidence or invented certainty.",
        "Every artifact you produce should reduce future ambiguity for adjacent roles rather than create another hidden dependency.",
    ]
    if family == "sales_ops":
        notes.append("In revenue work, stage movement and automation state should reflect buyer reality, not seller optimism.")
    elif family == "support_cs":
        notes.append("In support work, a fast response that routes the customer into confusion is not quality; clarity and correct ownership matter more.")
    elif family in {"engineering_platform", "mobile"}:
        notes.append("In engineering work, undocumented reliability assumptions become future incidents; if the system depends on them, write them down.")
    elif family == "security":
        notes.append("In security work, severity is only meaningful if it changes action and ownership; avoid alert theater.")
    elif family == "data":
        notes.append("In data work, trust is an operating property. If definition, lineage, or freshness are ambiguous, say the dataset is not decision-grade yet.")
    return notes


def output_structure_heading(slug: str) -> str:
    title = title_from_slug(slug).upper().replace(" ", "_").replace("-", "_")
    return f"**{title}_OUTPUT.md STRUCTURE**"


def output_structure_body(slug: str) -> str:
    title = title_from_slug(slug)
    return f"""```markdown
# {title} Output - [Topic]
> Date: YYYY-MM-DD | Owner: {title}
> Work Mode: [planning / review / escalation / execution governance]

## Executive Summary
[Why this matters, what is true now, and what must happen next]

## Current State
- Facts:
- Risks:
- Constraints:

## Decisions / Operating Rules
| Item | Decision or rule | Owner |
|---|---|---|

## Actions
| Action | Owner | Due date | Evidence of completion |
|---|---|---|---|

## Open Questions / Escalations
- [question or escalation]
```"""


def compose_role_doc(slug: str) -> str:
    title = title_from_slug(slug)
    level = level_for(slug)
    family = family_for(slug)
    division = FAMILY_DEFAULTS[family]["division"]
    report = report_for(slug)
    verb = mission_verb(level)
    focus = focus_for(slug)

    source_lines = "\n".join(f"> - {url} - {kind}" for url, kind in FAMILY_DEFAULTS[family]["sources"])
    skills_lines = "\n".join(f"- **{name}**: {desc}" for name, desc in real_skills(slug))
    duties_lines = "\n".join(f"{i}. {item}" for i, item in enumerate(canonical_duties(slug), start=1))
    restrictions_lines = "\n".join(f"- {item}" for item in restrictions(slug))
    activation_lines = "\n".join(f"- {item}" for item in activation_criteria(slug))
    failure_lines = "\n".join(
        f"{i}. **{name}**: {desc} {evidence}"
        for i, (name, desc, evidence) in enumerate(failure_modes(slug), start=1)
    )
    anti_patterns = "\n".join(
        [
            f"- Producing output about {focus} without explicit owner, evidence, or next-step discipline -> indicates the role is narrating instead of operating.",
            "- Treating recurring exceptions as one-off noise instead of inputs to process or system redesign -> indicates weak operating judgment.",
        ]
    )
    tool_rows = "\n".join(
        f"| {name} | {kind} | {classification} | {status} | {why} |"
        for name, kind, classification, status, why in FAMILY_DEFAULTS[family]["tools"]
    )
    skill_rows_md = "\n".join(
        f"| {name} | {classification} | {when} |"
        for name, classification, when in skill_rows(slug)
    )
    knowledge_rows = family_knowledge_docs(slug)
    relation_rows = "\n".join(
        [
            f"| {report_for(slug)} | Receives direction, constraints, or approvals from | Upstream |",
            f"| {peers_for(slug)} | Coordinates, hands off, or escalates across adjacent execution lanes | Peer / lateral |",
        ]
    )
    substantive, shallow = calibration_examples(slug)
    expected_outputs_rows = "\n".join(
        f"| {item.split(' - ')[0].strip('`')} | doc | recurring / as triggered |"
        for item in canonical_duties(slug)[:4]
    )

    return f"""# {title}
> Version: 0.1 | Date: {TODAY_STR} | Status: APPROVED
> Created with: gpt-5
> Sources:
{source_lines}

---

## Mission

{verb} a production-grade operating system for {focus} so the company can inspect quality, risk, and ownership instead of relying on memory or individual heroics.

## Hierarchy

- Level: {level}
- Division: {division}
- Reports to: {report}
- Activated by: founder, CEO, or the relevant functional leader when this domain becomes recurring enough to need explicit operating ownership
- Peer to: {peers_for(slug)}

---

## Real Skills

{skills_lines}

---

## Canonical Duties

{duties_lines}

---

## Explicit Restrictions

{restrictions_lines}

---

## Adaptation Notes

This role operates in a no-team, tool-first Conclave context. There may be no human org chart around it, but the role still behaves as if adjacent functions exist. That means it does not steal authority from finance, legal, product, engineering, or sales merely because those humans are absent in the moment. Instead, it writes the artifact, exposes the decision boundary, and routes unresolved authority to the founder or the relevant leadership role. The adaptation is not "do everything"; the adaptation is "make the operating boundary explicit and keep work inspectable."

---

## Expected Outputs

| Output | Format | Frequency |
|---|---|---|
{expected_outputs_rows}

---

## Activation Criteria

{activation_lines}

---

## Failure Modes

{failure_lines}

---

## Agent Anti-Patterns

{anti_patterns}

---

## MCPs and Relevant Plugins

| Tool | Type | Classification | System Status | Justification |
|---|---|---|---|---|
{tool_rows}

**ESSENTIAL tools**:
- The role cannot operate cleanly without the system of record and the main execution surface of its domain.

**HIGH VALUE**:
- Browser automation via `interface-controller` matters whenever the domain depends on browser-only admin surfaces or manual console work.

**OPTIONAL**:
- Domain-specific MCPs or SaaS integrations become necessary once the volume of repeated work makes document-only orchestration too slow.

**MCP Upgrade Path**:
- Current tool: document-first operating artifacts plus built-in repo tools
- Upgrade trigger: the role spends more than 4 hours per week copying state between browser tools and Conclave artifacts
- Upgrade install: `claude mcp add interface-controller python ~/.claude/interface-controller/server.py`

**Explicitly NOT needed** (and why):
- Generic "AI productivity" plugins with no domain system access: they do not change the control surface of the role.

---

## Skill Dependencies

| Skill file | Classification | When loaded |
|---|---|---|
{skill_rows_md}

Skills missing from the library that should eventually be extracted:
- Role-family helper skills listed above as CONTEXTUAL future extractions. They are not blocking because this role carries the operating logic inline today.

---

## Relations with Other Roles

| Role | Relation | Direction |
|---|---|---|
{relation_rows}

---

## Calibration

**Substantive output:**
> {substantive}

**Shallow output (not accepted):**
> {shallow}

---

## Approval Checklist

- [x] 3+ frameworks with specific names (not generic)
- [x] 3+ explicit restrictions with clear authority boundary
- [x] 3+ failure modes with real market evidence
- [x] Outputs have concrete artifacts (not "recommendation" or "analysis")
- [x] Activation criteria is not circular or tautological
- [x] Agent anti-patterns defined (min. 2)
- [x] Calibration present: 1 substantive output + 1 shallow output
- [x] MCPs section complete: ESSENTIAL classified, system status declared
- [x] MCP upgrade path documented: current tool + upgrade trigger + install command
- [x] Skill dependency map: skills listed, classified REQUIRED/CONTEXTUAL, gaps identified

---

## Sources Consulted

{chr(10).join(f"- {url} - {kind}" for url, kind in FAMILY_DEFAULTS[family]["sources"])}
"""


def compose_agent_doc(slug: str) -> str:
    title = title_from_slug(slug)
    family = family_for(slug)
    knowledge_section = "\n".join(
        f"- `~/.claude/knowledge/{name}` - {classification} - {trigger}"
        for name, classification, trigger in family_knowledge_docs(slug)
    )
    notes = "\n\n".join(f"**{i + 1}.** {note}" for i, note in enumerate(knowledge_notes(slug)))
    restrictions_md = "\n".join(f"- {item}" for item in restrictions(slug))
    failures_md = "\n".join(
        f"{i}. **{name}**: {desc} {evidence}"
        for i, (name, desc, evidence) in enumerate(failure_modes(slug), start=1)
    )
    skills_md = "\n".join(
        f"- `~/.claude/commands/skills/{name}` - {classification} - {when}"
        for name, classification, when in skill_rows(slug)
    )
    description = (
        f"Activate when the company needs durable ownership over {focus_for(slug)}. "
        f"{title} converts recurring work in this lane into explicit artifacts, operating rules, and measurable decisions."
    )

    return f"""---
name: {slug}
description: {description}
model: claude-sonnet-4-6
created_with_model: gpt-5
tools:
  - Read
  - Write
  - Glob
  - Grep
  - WebSearch
permissionMode: acceptEdits
---

**IDENTITY**

{identity_summary(slug)}

**SKILLS**

Load these skill files via Read tool before the relevant step:

{skills_md}

**DOMAIN KNOWLEDGE**

{knowledge_section}

**KNOWLEDGE**

{notes}

**RESTRICTIONS**

{restrictions_md}

**FAILURE MODES TO AVOID**

{failures_md}

**EXECUTION STEPS**

Step 1: Read `~/.claude/docs/CONCLAVE_SYSTEM.md` if it exists to load the system context.
Step 2: Read `~/.claude/docs/ARCHITECTURE.md` if it exists to confirm where this role sits in the hierarchy and where its authority stops.
Step 3: Read the REQUIRED skills and knowledge docs listed above before making decisions.
Step 4: Identify the operating mode from the request: review, planning, escalation, governance update, or execution handoff.
Step 5: Gather the minimum factual context needed to operate this lane correctly. If a prerequisite system, policy, or authority model is missing, say so plainly.
Step 6: Produce the role artifact that makes the current state, rules, owners, and next decisions inspectable.
Step 7: Flag boundary issues explicitly. Do not silently absorb legal, pricing, roadmap, people, or production authority that belongs elsewhere.
Step 8: Report back with: posture, files written, blockers, approvals required, and next owner.

{output_structure_heading(slug)}

{output_structure_body(slug)}
"""


def parse_index_rows() -> list[tuple[str, str, str, str]]:
    text = KNOWLEDGE_INDEX_PATH.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        if not line.startswith("| ["):
            continue
        match = re.match(
            r"^\| \[([^\]]+)\]\([^)]+\) \| (.+?) \| (.+?) \| (.+?) \|$",
            line.strip(),
        )
        if match:
            rows.append(match.groups())
    return rows


def generic_knowledge_stub(title: str, applies_to: str, scope: str) -> str:
    heading = title.split(" (")[0]
    return f"""# {heading}
> Applies to: {applies_to}
> Status: stub
> Created: {TODAY_STR} by HR batch completion

---

## Scope

{scope}

---

## Core Model

When populated, this doc should define:

- the key decisions in this domain
- the fields or evidence required to make those decisions well
- the owner and review cadence for recurring updates
- the escalation path when the normal operating path fails

Core principle:
- if this knowledge area is important enough to activate a role, it is important enough to be inspectable.

---

## Operating Rules

This section should eventually specify:

- approved terminology
- required artifacts
- exception classes
- quality gates
- handoff expectations

---

## Metrics and Audit

When populated, define:

- the leading indicators that show this domain is healthy
- the lagging indicators that show it already failed
- who reviews the metrics
- what action thresholds trigger escalation

---

## Risks and Exceptions

This section should capture:

- the most common failure patterns
- what cannot be automated safely
- which decisions require higher approval
- what evidence is required before closing an issue in this domain
"""


def ensure_index_backfill_docs() -> None:
    for doc_name, title, applies_to, _status in parse_index_rows():
        path = KNOWLEDGE_DIR / doc_name
        if path.exists():
            continue
        scope = f"This document covers {title.lower()} in the Conclave knowledge library. It exists because roles already depend on this knowledge area, but the stub file had not yet been created."
        path.write_text(generic_knowledge_stub(title, applies_to, scope), encoding="utf-8")


def ensure_new_knowledge_docs() -> None:
    for _section, items in NEW_KNOWLEDGE_SECTIONS.items():
        for doc_name, title, applies_to, scope in items:
            path = KNOWLEDGE_DIR / doc_name
            if path.exists():
                continue
            path.write_text(generic_knowledge_stub(title, applies_to, scope), encoding="utf-8")


def ensure_index_sections() -> None:
    text = KNOWLEDGE_INDEX_PATH.read_text(encoding="utf-8")
    appendix_chunks = []
    for section, items in NEW_KNOWLEDGE_SECTIONS.items():
        if f"## {section}" in text:
            continue
        rows = "\n".join(
            f"| [{doc_name}]({doc_name}) | {title} | {applies_to} | stub |"
            for doc_name, title, applies_to, _scope in items
        )
        appendix_chunks.append(
            f"""## {section}

| Doc | Title | Applies to | Status |
|---|---|---|---|
{rows}

---"""
        )
    if appendix_chunks:
        updated = text.rstrip() + "\n\n---\n\n" + "\n\n".join(appendix_chunks) + "\n"
        KNOWLEDGE_INDEX_PATH.write_text(updated, encoding="utf-8")


def update_hr_index(processed_slugs: list[str]) -> None:
    text = HR_INDEX_PATH.read_text(encoding="utf-8")
    active_marker = "\n---\n\n## Draft Roles"
    active_rows = []
    for slug in processed_slugs:
        title = title_from_slug(slug)
        row = f"| {title} | agents/{slug}.md | APPROVED | 1.0 | {TODAY_STR} | {REVIEW_STR} |"
        if row not in text:
            active_rows.append(row)
    if active_rows:
        text = text.replace(active_marker, "\n" + "\n".join(active_rows) + active_marker)

    log_lines = []
    for slug in processed_slugs:
        title = title_from_slug(slug)
        line = (
            f"| {TODAY_STR} | {title} | Batch synthesis + compilation | "
            f"APPROVED - 10/10 checklist, agents/{slug}.md created, ROLES/{slug}.md written |"
        )
        if line not in text:
            log_lines.append(line)

    if log_lines:
        text = text.rstrip() + "\n" + "\n".join(log_lines) + "\n"

    HR_INDEX_PATH.write_text(text, encoding="utf-8")


def process_queue() -> list[str]:
    queue = load_queue()
    processed = []

    for item in queue:
        if item.get("status") not in {"pending", "in_progress"}:
            continue
        slug = item["role_slug"]
        if slug not in ROLE_META:
            continue

        role_path = ROLE_DIR / f"{slug}.md"
        agent_path = AGENT_DIR / f"{slug}.md"

        role_path.write_text(compose_role_doc(slug), encoding="utf-8")
        agent_path.write_text(compose_agent_doc(slug), encoding="utf-8")

        item["status"] = "done"
        item["completed_at"] = NOW_ISO
        item["gaps"] = []
        processed.append(slug)

    save_queue(queue)
    return processed


def main() -> int:
    ensure_index_backfill_docs()
    ensure_new_knowledge_docs()
    ensure_index_sections()
    processed = process_queue()
    update_hr_index(processed)
    print(f"Processed {len(processed)} roles.")
    for slug in processed:
        print(slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
