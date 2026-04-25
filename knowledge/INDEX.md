# Conclave Knowledge Library

> Domain knowledge for Conclave agents. Each doc is loaded on-demand via Read tool.
> Maintained by HR agent — updated when new agents are built or on 90-day review cycles.

---

## How to use this library

Agents load knowledge docs with the Read tool before executing decisions in that domain:

```
Read({ file_path: "~/.claude/knowledge/[doc-name].md" })
```

Each agent's `**DOMAIN KNOWLEDGE**` section lists which docs to load and when (REQUIRED / CONTEXTUAL).

---

## Marketing

| Doc | Title | Applies to | Status |
|---|---|---|---|
| [marketing-paid-traffic.md](marketing-paid-traffic.md) | Paid Traffic Scaling | CMO, Traffic Manager, CRO | stub |
| [marketing-funnel-frameworks.md](marketing-funnel-frameworks.md) | Funnel Frameworks | CMO, CRO, Design CTO | stub |
| [marketing-copy-validation.md](marketing-copy-validation.md) | Copy Validation | CMO, Traffic Manager, Social Media Manager | stub |
| [marketing-content-strategy.md](marketing-content-strategy.md) | Content Strategy | CMO, Social Media Manager | stub |
| [marketing-attribution.md](marketing-attribution.md) | Attribution & Analytics | CMO, Traffic Manager | stub |
| [marketing-brand-positioning.md](marketing-brand-positioning.md) | Brand Positioning | CMO | stub |

---

## Engineering

| Doc | Title | Applies to | Status |
|---|---|---|---|
| [engineering-system-design.md](engineering-system-design.md) | System Design Principles | CTO | stub |
| [engineering-team-org.md](engineering-team-org.md) | Engineering Team Org | CTO | stub |
| [engineering-architecture-decisions.md](engineering-architecture-decisions.md) | Architecture Decision-Making | CTO | stub |
| [engineering-observability.md](engineering-observability.md) | Observability & Monitoring | CTO | stub |

---

## Sales & Revenue

| Doc | Title | Applies to | Status |
|---|---|---|---|
| [sales-pipeline-management.md](sales-pipeline-management.md) | Pipeline Management | CRO | stub |
| [sales-enterprise-frameworks.md](sales-enterprise-frameworks.md) | Enterprise Sales Frameworks | CRO | stub |
| [sales-negotiation.md](sales-negotiation.md) | Negotiation Frameworks | CRO | stub |
| [sales-forecasting.md](sales-forecasting.md) | Sales Forecasting | CRO | stub |

---

## Finance

| Doc | Title | Applies to | Status |
|---|---|---|---|
| [finance-saas-metrics.md](finance-saas-metrics.md) | SaaS Metrics & Benchmarks | CFO, CEO | stub |
| [finance-fundraising.md](finance-fundraising.md) | Fundraising Mechanics | CFO, CEO | stub |
| [finance-runway-management.md](finance-runway-management.md) | Runway & Cash Management | CFO | stub |

---

## Strategy (CEO)

| Doc | Title | Applies to | Status |
|---|---|---|---|
| [strategy-market-timing.md](strategy-market-timing.md) | Market Timing & Entry | CEO | stub |
| [strategy-product-market-fit.md](strategy-product-market-fit.md) | PMF Signals & Validation | CEO, CTO, CMO | stub |
| [strategy-hiring-sequence.md](strategy-hiring-sequence.md) | Hiring Sequence by Stage | CEO | stub |
| [strategy-fundraising-narrative.md](strategy-fundraising-narrative.md) | Fundraising Narrative | CEO | stub |

---

## Security

| Doc | Title | Applies to | Status |
|---|---|---|---|
| [security-compliance-roadmap.md](security-compliance-roadmap.md) | Compliance Roadmap (SOC2, ISO, GDPR) | CISO | stub |
| [security-incident-response.md](security-incident-response.md) | Incident Response Playbook | CISO | stub |

---

## Legal

| Doc | Title | Applies to | Status |
|---|---|---|---|
| [legal-startup-structure.md](legal-startup-structure.md) | Startup Legal Structure | CLO | stub |
| [legal-ip-protection.md](legal-ip-protection.md) | IP Protection Frameworks | CLO | stub |
| [legal-employment-law.md](legal-employment-law.md) | Employment & Contractor Law | CLO | stub |

---

## Product & UX

| Doc | Title | Applies to | Status |
|---|---|---|---|
| [ux-conversion-design.md](ux-conversion-design.md) | Conversion Design Patterns | Design CTO | stub |
| [ux-onboarding-patterns.md](ux-onboarding-patterns.md) | Onboarding Design Patterns | Design CTO | stub |
| [ux-usability-testing.md](ux-usability-testing.md) | Usability Testing Methods | Design CTO | stub |

---

## Status legend

| Status | Meaning |
|---|---|
| `stub` | File exists with schema, content not yet researched |
| `draft` | Research done, awaiting HR approval |
| `approved` | HR-approved, production-ready |
| `stale` | Older than 90 days, scheduled for review |
