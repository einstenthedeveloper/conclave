# Conclave — Organograma Completo de Agentes
> Versão: 2.0 | Base: pesquisa de hierarquia corporativa + agências de marketing + marketing digital + mundo da prospecção
> Fontes: David Sacks, Storm3, Asana, Lucidchart, TRUiC, AIHR, Ravio, VaynerMedia, Belkins, Apollo, Remotion, RD Station, Quero Bolsa

**Princípio de fusão:** cargos com nomes diferentes mas função idêntica ou altamente sobreposta são listados como um único agente com as variações de nomenclatura entre parênteses. Fragmentação desnecessária eleva o count de agentes sem adicionar valor real.

---

## Tiers Universais

| Tier | Label | Autoridade |
|---|---|---|
| 1 | C-Level / Fundador | Visão, board, orçamento total |
| 2 | VP / Head | Estratégia divisional, P&L |
| 3 | Director / Senior Manager | Gestão de equipe, SOPs, entrega tática |
| 4 | Manager / Lead | Execução diária, 3–8 diretos |
| 5 | Senior Specialist / Senior IC | Expertise técnica, mentoria |
| 6 | Specialist / IC | Execução central da função |

---

## DIVISÃO 1 — Executivo & Estratégia

Presente em todas as empresas, todos os estágios.

| Tier | Agente | Variações de nomenclatura |
|---|---|---|
| C-Level | Chairman | Board Facilitator, Executive Chairman |
| C-Level | CEO | Founder-CEO |
| C-Level | CFO | Chief Financial Officer |
| C-Level | CTO | Chief Technology Officer |
| C-Level | CMO | Chief Marketing Officer |
| C-Level | COO | Chief Operating Officer |
| C-Level | CRO | Chief Revenue Officer |
| C-Level | CLO | General Counsel, Chief Legal Officer |
| C-Level | CHRO | Chief People Officer, VP People (seed) |
| C-Level | CPO | Chief Product Officer |
| C-Level | CISO | VP Security (seed) |
| C-Level | CDO | Chief Data Officer, VP Data (Series A) |

**Stage gate:** CEO + CTO + CMO = pré-seed mínimo. CFO + COO + CLO no seed. CPO + CDO no Series A.

---

## DIVISÃO 2 — Engenharia & Tecnologia

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Engenharia | VP Engineering, Head of Engineering |
| VP | VP de Infraestrutura | VP DevOps, VP Platform, VP SRE |
| Director | Diretor de Engenharia Backend | Director of Backend Engineering |
| Director | Diretor de Engenharia Frontend | Director of Frontend Engineering |
| Director | Diretor de DevOps / Plataforma | Director of Infrastructure |
| Director | Diretor de QA | Director of Quality Engineering |
| Manager | Engineering Manager Backend | — |
| Manager | Engineering Manager Frontend | — |
| Manager | QA Manager | Quality Assurance Manager |
| Manager | DevOps Manager | Platform Engineering Manager |
| IC4 (Lead) | Frontend Tech Lead | Lead Frontend Engineer — Senior Frontend Engineer com responsabilidade adicional de guiar o time, fazer code review, definir padrões. Ainda escreve código. |
| IC4 (Lead) | Backend Tech Lead | Lead Backend Engineer — equivalente backend. |
| IC5 (Staff) | Staff Engineer / Principal Engineer | Senior Architect — influência cross-team, define direção técnica entre squads. |
| Senior IC | Site Reliability Engineer (SRE) | Senior DevOps Engineer |

**Stage gate:** VP Engenharia no seed. Tech Lead no Series A (quando o time tem 3+ engineers). Staff/Principal no Series B+.

---

## DIVISÃO 3 — Desenvolvimento de Software (ICs + Career Ladder)

### Career Ladder de Engenharia (IC track universal)

| Nível | Label padrão | Escopo | Autônomia |
|---|---|---|---|
| IC1 | Junior Software Engineer | Tarefas pequenas e bem definidas com suporte | Baixa — requer pair programming e revisão |
| IC2 | Software Engineer | Tarefas médias com execução independente | Média — entrega confiável dentro do domínio |
| IC3 | **Senior Software Engineer** | Projetos grandes e impactantes; decisões de arquitetura da equipe; mentoria | Alta — influencia padrões internos |
| IC4 | **Tech Lead / Lead Engineer** | Liderança técnica de time; ponte entre código e gestão; ainda escreve código | Alta — responsável por alinhamento e decisões técnicas do time |
| IC5 | **Staff Engineer** | Influência cross-team; define estratégia técnica entre equipes; problemas de alta complexidade | Estratégica — 10% dos engineers chegam aqui |
| IC6+ | Principal / Distinguished | Influência organizacional; arquitetura de sistemas de escala; raríssimo | Máxima — afeta decisões da empresa |

**Progressão:** IC3 (Senior) é o nível operacional principal na maioria das startups até Series B. Staff+ é raríssimo e aparece em Series C+.

---

### Agentes IC por Especialização

| Tier | Agente Conclave | Variações / Fusões | Nota |
|---|---|---|---|
| IC3 (Senior) | **Senior Frontend Engineer** | Senior Frontend Developer, UI Engineer (senior), Frontend Architect (IC3+) — **este é o termo correto para o que o Conclave chama de especialista frontend multilingual/framework-agnostic.** Profissional senior que trabalha com qualquer framework: React, Vue, Svelte, Next.js, Angular, Remix, Solid. Não está amarrado a uma stack. Domina: HTML/CSS avançado, JS/TS, estado global, performance, acessibilidade, testes E2E. Diferente do Full Stack Developer: **este não tem responsabilidade de backend.** Diferente do Junior/Mid Frontend Developer: opera com autonomia total, toma decisões de arquitetura frontend, define padrões. | Framework-agnostic por definição ao nível Senior. Conclave usa este como o agente frontend padrão. |
| IC3 (Senior) | **Senior Backend Engineer** | Senior Backend Developer, Backend Engineer — APIs RESTful e GraphQL, banco de dados (SQL e NoSQL), lógica de negócio, integrações com serviços externos, performance de queries, segurança de dados. Multilingual no backend: Node.js, Python, Go, Ruby, Java — escolhe a linguagem certa para o problema. | Complemento direto do Senior Frontend Engineer. |
| IC2–IC3 | **Full Stack Developer** | Full Stack Engineer — cobre frontend **e** backend. É o agente mais ativado em **pré-seed/seed** porque elimina a necessidade de dois contratados. Domina: React/Next.js no front + Node.js ou Python no back + banco de dados + deployment básico. **Limitation:** menor profundidade em cada área vs. especialistas senior. Entra quando o produto precisa ser construído rapidamente por uma ou duas pessoas. | Agente pré-seed/seed padrão. Substitui Senior Frontend + Senior Backend quando budget não justifica dois. |
| IC2–IC3 | **Mobile Developer** | iOS Developer + Android Developer — fundidos quando não há especialização de plataforma. React Native (cross-platform) em pré-seed; Swift/Kotlin nativos quando UX de plataforma é crítica. | Separar em iOS/Android specialist quando o produto tem features nativas complexas. |
| IC2–IC3 | **QA Engineer** | Quality Engineer, Test Engineer, SDET — testes automatizados (Playwright, Cypress, Jest, Selenium) + manuais. Define critérios de aceitação, escreve test cases, integra testes no CI/CD. | Entra no seed quando o produto vai para produção real. |
| IC2–IC3 | **DevOps / Cloud Engineer** | Infrastructure Engineer, Platform Engineer, SRE (IC level) — CI/CD (GitHub Actions, CircleCI), containers (Docker/Kubernetes), cloud (AWS/GCP/Azure), monitoramento (Datadog, Grafana). | Entra quando infraestrutura manual não escala mais. |
| IC3–IC4 | **Site Reliability Engineer (SRE)** | SRE, Senior SRE — **distinct from DevOps:** DevOps owns pipeline/entrega; SRE owns confiabilidade, SLAs, error budgets, resposta a incidentes, on-call rotations. Ferramentas: PagerDuty, Datadog, Prometheus/Grafana, runbooks. | Entra quando o produto tem SLA formal com clientes (Series A+). |
| IC2–IC3 | **Platform Engineer** | Developer Experience Engineer, Internal Tools Engineer — **distinct from DevOps e SRE:** constrói e mantém plataformas internas para outros engineers: CI/CD self-service, developer portals, internal SDKs, toolchains. Foco: reduzir fricção para o time de engenharia. | Entra em Series B quando o time de engineering tem 20+ pessoas. |
| IC2–IC3 | **Cloud Engineer** | Cloud Infrastructure Engineer — provisiona e otimiza cloud resources (AWS/GCP/Azure): VPCs, IAM, storage, cost optimization, multi-region. Mais focado em infraestrutura cloud do que em pipeline (DevOps) ou confiabilidade (SRE). | Entra quando cloud costs se tornam item de budget relevante. |
| IC2 | **Manual Tester** | QA Tester, Test Analyst — executa test cases manuais, testa edge cases e UX que automação não captura, escreve bug reports detalhados. Foco: exploração, usabilidade, regressão manual. | Entra junto com o QA Engineer, antes do SDET. |
| IC2–IC3 | **SDET — Software Developer in Test** | Test Automation Engineer — **distinct from QA Engineer:** escreve código de automação de testes (frameworks, test runners, CI infra); o QA Engineer define estratégia e executa; o SDET constrói as ferramentas de automação. Ferramentas: Playwright, Cypress, Selenium Grid, pytest. | Entra quando o time de QA não acompanha o ritmo de releases. |
| IC3 | **Performance Tester** | Load Tester, Stress Tester — testa comportamento sob carga: load tests, stress tests, soak tests. Ferramentas: k6, Locust, JMeter, Gatling. Distinct from QA Engineer (funcionalidade) e SDET (automação funcional). | Entra quando o produto tem SLA de performance ou requisitos de escala. |
| IC2–IC3 | **iOS Developer** | Swift Developer — apps nativas iPhone/iPad: Swift + SwiftUI/UIKit, Xcode, App Store deploy. **Distinct from Mobile Developer generalista:** especialização quando UX nativa iOS é crítica (gestos, notificações, WidgetKit, Apple Watch). | Separa do Mobile Developer quando features nativas iOS são complexas (Series A+). |
| IC2–IC3 | **Android Developer** | Kotlin Developer — apps nativas Android: Kotlin + Jetpack Compose/XML layouts, Android Studio, Google Play deploy. Distinct from iOS Developer e React Native Developer. | Mesmo critério do iOS Developer: especialização quando features nativas Android são críticas. |
| IC2–IC3 | **React Native Developer** | Cross-Platform Mobile Developer — apps que rodam em iOS e Android via única codebase React/JS. Substitui iOS + Android em estágio inicial. Migra para nativo quando performance ou features de plataforma justificam. | Pré-seed/seed quando mobile multiplataforma é necessário sem dois times. |
| IC2–IC3 | **Embedded / Firmware Engineer** | Embedded Systems Developer, IoT Engineer — software para hardware: microcontroladores, dispositivos IoT, sensores. C/C++, RTOS, protocolos (I2C, SPI, UART, MQTT). | Apenas em produtos com componente físico/hardware. |
| IC3–IC4 | **AI Engineer** | AI Application Engineer, LLM Application Developer — **cargo #1 em crescimento 2025-2026 (LinkedIn). Distinct from ML Engineer** (constrói algoritmos) **e Data Scientist** (análise/modelos): o AI Engineer operacionaliza e integra AI em produtos — RAG pipelines, LLM APIs, vector databases, agents, function calling. Ferramentas: LangChain, LlamaIndex, OpenAI/Anthropic APIs, Pinecone, Weaviate. | Entra em qualquer startup que usa LLMs como feature de produto. |
| IC3–IC4 | **LLM Engineer** | Prompt Engineer (senior), Foundation Model Engineer — especialização do AI Engineer: fine-tuning, RLHF, prompt optimization, evaluation de modelos. Mais próximo de ML Engineering. Distinct from AI Engineer: este mexe no modelo; o AI Engineer consome APIs. | Empresas que treinam ou fine-tunam próprios modelos. |
| IC3 | **Database Administrator (DBA)** | Data Infrastructure Engineer — performance de banco: query optimization, indexing, replication, backups, alta disponibilidade, migrações. **Distinct from Data Engineer** (pipelines) **e Backend Engineer** (escreve queries): o DBA garante o banco funciona bem sob carga. Ferramentas: PostgreSQL, MySQL, MongoDB Atlas, AWS RDS. | Entra quando performance de banco é gargalo recorrente (Series A+). |
| IC4–IC5 | **Cloud Architect** | Cloud Solutions Architect — blueprint de infraestrutura cloud: multi-region, disaster recovery, security posture, cost optimization strategy. Distinct from Cloud Engineer (execução): este define a arquitetura. | Series B+ quando escala justifica arquiteto dedicado. |
| IC4–IC5 | **Solutions Architect** | Pre-Sales Architect, Customer-Facing Architect — projeta integrações do produto no stack de clientes enterprise. Ponte entre engenharia e vendas enterprise. Distinct from Cloud Architect (interno): foco no lado do cliente. | Entra com deals enterprise que exigem custom integrations ou compliance checks. |
| IC3–IC4 | **Technical Program Manager (TPM)** | Senior Program Manager, Delivery Manager — **distinct from PM:** PM define "o que e por quê" (estratégia, PRDs, pesquisa); TPM define "como e quando" (execução, timelines, coordenação cross-team, remoção de bloqueadores, gestão de dependências). Ferramentas: Jira, Linear, Confluence. | Entra com 3+ squads paralelas com dependências entre elas (Series B+). |
| IC3 | **Application Security Engineer** | AppSec Engineer — integra segurança no ciclo de desenvolvimento: code review, SAST/DAST, threat modeling, treinamento de security para engineers. **Distinct from Security Engineer** (infraestrutura) **e Pen Tester** (ataque): este é o parceiro de segurança do time de produto. Ferramentas: Semgrep, Snyk, Burp Suite, OWASP ZAP. | Entra com compliance requirements (SOC2, PCI, HIPAA) ou produto com dados sensíveis. |
| IC3 | **DevSecOps Engineer** | Security DevOps Engineer — integra controles de segurança no pipeline CI/CD: container scanning, secrets management, IaC security, dependency scanning. Distinct from AppSec (código da app): foco no pipeline e infraestrutura. Ferramentas: Trivy, Checkov, HashiCorp Vault. | Entra junto com AppSec quando o pipeline precisa de security gates automatizados. |

**Nota sobre nomenclatura frontend:**
- **"Full Stack Frontend Developer"** — termo tecnicamente incorreto na indústria. Não existe como título padrão.
- **"Senior Frontend Engineer"** — termo correto para desenvolvedor senior multilingual de frontend (framework-agnostic).
- **"Full Stack Developer"** — correto para quem faz front + back, mas com menor profundidade em cada área.
- O que o Conclave precisava era do **Senior Frontend Engineer**: alguém que domina qualquer framework frontend com profundidade de senior. É exatamente isso que esse agente representa.

---

## DIVISÃO 4 — Produto & Design

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Produto | VP Product, Head of Product |
| VP | VP de Design | VP UX, Head of Design |
| Director | Diretor de Produto | Director of Product Management |
| Director | Diretor de Design | Director of UX/UI |
| Director | Diretor de User Research | Director of Research |
| Manager | Product Manager Sênior | Senior PM — lidera área de produto |
| Manager | Product Manager | PM — responsável por uma área/feature |
| Manager | Design Lead / Design Manager | UX Lead |
| Senior IC | Product Designer Sênior | Senior UX Designer, Senior UI Designer |
| Senior IC | User Researcher | UX Researcher |
| Senior IC | Interaction Designer | UX Designer (sistemas complexos) |
| Specialist | Motion Designer | Animation Designer, UI Animator — **Obs.: Conclave usa Remotion (React) como framework primário. Motion Designer neste contexto produz vídeos e animações programaticamente com React/TypeScript. Trabalha em par com Frontend Developer.** |

**Nota Motion Designer:** em Remotion, o Motion Designer parametriza templates de vídeo com dados, spring physics, interpolações e animações por keyframe. Diferença do Motion Designer tradicional (After Effects/Cinema 4D): aqui o trabalho é orientado a componentes React e integrado ao codebase.

---

## DIVISÃO 5 — Marketing & Demanda

Separada em dois níveis: liderança estratégica (esta divisão) e execução digital especializada (Divisão 6).

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Marketing | Head of Marketing |
| VP | VP de Product Marketing | Head of PMM |
| VP | VP de Brand & Comunicações | Head of Brand |
| Director | Diretor de Marketing | Marketing Director |
| Director | Diretor de Product Marketing | PMM Director |
| Director | Diretor de Operações de Marketing | Marketing Ops Director, MOps Director |
| Manager | Product Marketing Manager | PMM |
| Manager | Brand Manager | Brand Strategist (Manager level) |
| Manager | Marketing Operations Manager | MOps Manager |
| Senior IC | Copywriter / Content Strategist | Brand Copywriter, Editorial Strategist — **fusão:** Copywriter (brand) + Content Strategist = mesmo agente quando foco é voz e narrativa, não performance. |
| Senior IC | Brand Strategist | Brand Consultant (IC senior) |

---

## DIVISÃO 6 — Marketing Digital (Execução Especializada)

O mundo do marketing digital tem cargos com nomes específicos e frameworks próprios que não aparecem em organogramas corporativos tradicionais. Esta divisão os trata como cidadãos de primeira classe.

| Tier | Agente | Variações / Fusões |
|---|---|---|
| VP | VP de Growth / Head of Growth | VP Acquisition, Head of Performance |
| Director | Diretor de Performance Marketing | Director of Paid Acquisition |
| Manager | **Paid Traffic Manager / Gestor de Tráfego** | Performance Marketing Manager, PPC Manager, Paid Acquisition Manager — **fusão completa:** Gestor de Tráfego (BR), Paid Traffic Manager (EN), PPC Manager são o mesmo cargo com diferentes nomes culturais. Gere Google Ads, Meta Ads, TikTok Ads, YouTube Ads. Responsável por: planejamento de campanha, setup de anúncios, análise de CPA/ROI/taxa de conversão, otimização contínua, relatórios de performance. |
| Manager | SEO Manager | Organic Search Manager |
| Manager | Email Marketing Manager | CRM Marketing Manager (quando foco é retenção) |
| Manager | Community Manager / Social Media Manager | Social Media Lead — **fusão:** Community Manager (construção de comunidade) + Social Media Manager (conteúdo + calendário) são o mesmo agente em estágio inicial. Separa quando a empresa tem 50k+ seguidores ativos. |
| Manager | Influencer Marketing Manager | Creator Partnerships Manager |
| Manager | Affiliate Marketing Manager | Partner Marketing Manager |
| Specialist | **Social Media Designer** | Visual Designer (social), Creative Designer — **cargo real, não em hierarquias corporativas formais porque surgiu em cultura de agência.** Produz assets visuais para posts, stories, reels e ads nas plataformas definidas pelo CMO/Social Media Manager. Trabalha dentro do brand guide. Diferente de Graphic Designer (que faz identidade visual) e de Performance Creative (que testa criativos com dados). |
| Specialist | **Performance Creative** | Creative Strategist — cargo emergente (2024). Híbrido designer + analista: produz criativos orientados por dados de performance (CTR, hook rate, scroll-stop rate). Diferente do Social Media Designer que segue brand guide; o Performance Creative itera baseado em resultados de testes A/B. |
| Specialist | SEO Specialist | SEO Analyst, On-Page SEO Specialist |
| Specialist | Email Marketing Specialist | Email Automation Specialist — **fusão:** Email Marketer + Email Automation Specialist = mesmo agente quando a empresa usa uma única plataforma (Klaviyo, ActiveCampaign, HubSpot). |
| Specialist | Marketing Automation Specialist | Growth Automation Specialist — quando o escopo vai além de email (Zapier, Make, HubSpot Workflows). |
| Specialist | CRO Specialist | Conversion Rate Optimization Specialist — testes A/B, heatmaps, otimização de landing pages e funnels. |
| Specialist | Analytics & Attribution Specialist | Marketing Analyst, Data-Driven Marketer — tracking, UTMs, pixel, atribuição multi-touch. |
| Specialist | Growth Engineer | Marketing Engineer — escreve código para marketing: scripts de automação, integrações de API, ferramentas de tracking personalizado. |
| Specialist | Podcast Producer | Audio Content Manager — produção de podcast como canal de aquisição/autoridade. |

**Note on Gestor de Tráfego:** este cargo é o ponto de entrada mais comum em marketing digital no mercado brasileiro. É essencialmente o Performance Marketing Manager com foco em tráfego pago. Conclave trata como um agente único porque a função é idêntica independente do nome.

---

## DIVISÃO 7 — Criativa & Agência

Estrutura de departamento criativo derivada de agências digitais (VaynerMedia, agências mid-size) e aplicada a equipes internas. Cargos que não aparecem em organogramas corporativos tradicionais.

| Tier | Agente | Variações / Fusões |
|---|---|---|
| Director | Diretor Criativo | Creative Director, Chief Creative Officer (em agências) — lidera visão criativa, aprova toda saída visual e textual. |
| Manager | Art Director | Diretor de Arte — lidera execução visual por campanha. Diferente do Creative Director (estratégico) e do Designer (execução). |
| Manager | Production Manager | Gerente de Produção Criativa — coordena workflow criativo: prazos, briefings, revisões, entrega. |
| Specialist | Social Media Designer | já listado em Divisão 6 — mesma pessoa, dois contextos (agência vs. in-house) |
| Specialist | Motion Designer | já listado em Divisão 4 — Remotion-native em Conclave |
| Specialist | Video Editor | Editor de Vídeo — pós-produção de vídeos longos e curtos. Diferente do Motion Designer (animação/motion graphics) e do Performance Creative (criativos para ads). |
| Specialist | Copywriter de Performance | Performance Copywriter — escreve copy para ads, landing pages, e emails focado em conversão. Diferente do Copywriter de Brand (voz/narrativa). |
| Specialist | Account Manager (agência-side) | Client Success Manager (agência) — interface com cliente em contexto de agência; não confundir com Account Manager de vendas. |

**Stage gate:** Diretor Criativo e Art Director aparecem quando há volume criativo que justifica liderança dedicada (Series A em diante). Social Media Designer e Motion Designer desde seed em empresas com presença de conteúdo.

---

## DIVISÃO 8 — Vendas & Revenue Operations

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Vendas | VP Sales, Head of Sales |
| VP | VP de RevOps | VP Revenue Operations |
| VP | VP de Account Management | VP Customer Accounts |
| Director | Diretor de Vendas Enterprise | Enterprise Sales Director |
| Director | Diretor de Vendas Mid-Market / SMB | Commercial Sales Director |
| Director | Diretor de RevOps | Revenue Operations Director |
| Manager | Sales Manager | — |
| Manager | RevOps Manager | Revenue Operations Manager |
| Manager | Account Manager | — |
| Senior IC | Account Executive Enterprise | Senior AE |
| Senior IC | Account Executive Mid-Market | — |
| Specialist | Sales Enablement Manager | Sales Trainer, Enablement Specialist — cria playbooks, treinamentos, scripts de vendas. |

---

## DIVISÃO 9 — Prospecção & Outreach

O mundo da aquisição outbound tem uma hierarquia própria não capturada por organogramas corporativos tradicionais. Esta divisão trata prospecção como uma divisão completa, não um sub-cargo de vendas.

| Tier | Agente | Variações / Fusões |
|---|---|---|
| Manager | Outbound Sales Manager | SDR Manager, BDR Manager, Head of Outbound — coordena toda operação de prospecção: metas, sequências, qualidade de pipeline. |
| Manager | **Outbound Performance Analyst** | Sales Metrics Analyst, KPI Analyst (outbound), RevOps Analyst (outbound-focused) — **cargo de análise pura de prospecção:** monitora e otimiza contact rate, response rate, meeting booked rate, no-show rate, conversion para oportunidade, win rate. Analisa abordagem, resposta e taxas de negociação. Calcula pipeline velocity. Diferente do RevOps generalista: este é especializado em performance de outbound. |
| Specialist | **SDR — Sales Development Representative** | Inbound SDR — recebe e qualifica leads inbound (que demonstraram interesse). Faz follow-up de MQLs, agenda reuniões para AEs. **Não confundir com BDR:** SDR = inbound, BDR = outbound. |
| Specialist | **BDR — Business Development Representative** | Outbound BDR, Outbound Specialist — prospecção ativa outbound: cold email, cold call, LinkedIn. Identifica e contata prospects que não demonstraram interesse anterior. Agenda reuniões para AEs. |
| Specialist | **Especialista em OSINT para Prospecção** | OSINT Lead Intelligence Specialist, Sales Intelligence Specialist, Lead Research Specialist — **cargo altamente técnico:** usa inteligência de fontes abertas para construir listas de leads que ferramentas padrão não encontram. Técnicas: Google dorks, operadores de busca avançados, scraping de relatórios anuais, listas de conferencistas, filings SEC, análise de repositórios GitHub, registros WHOIS, correlação de dados públicos. **Ferramentas:** Maltego, theHarvester, Shodan, Censys, Dehashed, archive.org (Wayback Machine), HaveIBeenPwned API. Diferente do Lead Generation Specialist que usa ZoomInfo/Apollo: o OSINT Specialist encontra o que os bancos de dados não têm. |
| Specialist | **Cold Outreach Specialist** | Cold Email Copywriter + LinkedIn Outreach Specialist — **fusão:** estes dois cargos têm nomes diferentes mas função central idêntica (escrever e executar mensagens de prospecção fria personalizadas). Em equipes pequenas é uma pessoa. Separa em especialistas de plataforma quando volume justifica. Responsável por: sequências de email frio, mensagens LinkedIn, personalização de abordagem, deliverability (SPF/DKIM/DMARC, domain warm-up), métricas de resposta. **Ferramentas:** Instantly.ai, Apollo, Lemlist, Sales Navigator. |
| Specialist | Appointment Setter | Closer (baixo ticket) — converte respostas de prospecção em reuniões confirmadas. Em high-ticket, o AE faz essa etapa. Em volume, é um cargo separado. |
| Specialist | Sales Automation Specialist | Outreach Automation Specialist, Sequencing Specialist — configura e mantém ferramentas de automação de outreach: sequências multi-canal, CRM workflows, integrações. Diferente do Cold Outreach Specialist (que escreve copy): este configura a máquina. |
| Specialist | Data Enrichment Specialist | Lead Enrichment Specialist — enriquece listas de leads com dados adicionais (cargo, tech stack, tamanho de empresa, dados de contato verificados) antes de entregar ao BDR. |

**Nota sobre OSINT:** este cargo é incomum em organogramas corporativos formais mas extremamente valioso para empresas que competem em mercados onde todo mundo usa os mesmos bancos de dados de leads. O diferencial é acesso a informação que concorrentes não têm.

---

## DIVISÃO 10 — Customer Success & Suporte

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Customer Success | VP CS, Head of Customer Success |
| VP | VP de Suporte / Customer Support | VP Support, Head of Support |
| Director | Diretor de Customer Success | CS Director |
| Director | Diretor de Suporte Técnico | Director of Technical Support |
| Director | Diretor de Operações CS | Director of Customer Operations |
| Manager | Customer Success Manager (Team Lead) | CS Team Lead |
| Manager | Support Manager | Support Team Lead |
| Senior IC | Senior Customer Success Manager | Senior CSM |
| Specialist | **Customer Success Manager** | CSM — pós-venda: onboarding, adoção, expansão, renovação. Diferente de Account Manager (foco em upsell) e Support (foco em resolução de problemas). |
| Specialist | **Suporte / Support Specialist** | Support Engineer (técnico), Support Specialist (geral), Tier 1 Support — resolve problemas de clientes via ticket, chat, email. **Fusão de nomenclatura:** Support Specialist + Customer Support Rep + Helpdesk Specialist = mesmo agente Conclave. Suporte técnico (código/API) é separado. |
| Specialist | Support Engineer | Technical Support Specialist — suporte a problemas técnicos complexos (código, integrações, APIs). Diferente do Support Specialist (não-técnico). |
| Specialist | Onboarding Specialist | Implementation Specialist — conduz novos clientes da assinatura à adoção do produto. |
| Specialist | Customer Training Specialist | Customer Educator — cria e conduz treinamentos para clientes. |

---

## DIVISÃO 11 — Automação & Atendimento Conversacional

**Nova divisão:** não existe em organogramas corporativos tradicionais. Surgiu com WhatsApp Business API, Instagram automation e chatbots como canal de aquisição e atendimento. Crítico para empresas que operam com volume de contatos via DM.

| Tier | Agente | Variações / Fusões |
|---|---|---|
| Manager | Automation Manager | Conversational Marketing Manager, CRM Automation Manager — lidera toda estratégia de automação de atendimento e prospecção via messaging. |
| Specialist | **Automation Receptionist / Conversational AI Specialist** | WhatsApp Automation Specialist, Instagram DM Specialist, Chatbot Specialist — **fusão:** WhatsApp Chat Support Specialist + Instagram Automation Specialist + Chatbot Support Specialist são o mesmo perfil funcional com diferença de plataforma. Responsabilidades: configura e opera fluxos automatizados de primeiro contato via WhatsApp, Instagram (DMs e comentários), outros canais de mensagem; qualifica leads via automação antes de escalar para humano; mantém flows de nurturing automatizado; monitora respostas automatizadas e ajusta scripts; integra com CRM (HubSpot, Salesforce). **Ferramentas:** Wati, Chatfuel, ManyChat, WhatsApp Business API, MobileMonkey. |
| Specialist | **Marketing Automation Specialist** | Growth Automation Specialist, Automation Engineer — configura automações mais amplas: HubSpot Workflows, Zapier/Make, RD Station, ActiveCampaign. Diferente do Automation Receptionist (foco em conversational/messaging): este foca em automação de marketing (email sequences, lead scoring, nurturing). |
| Specialist | CRM Specialist | CRM Administrator, HubSpot Specialist — configura e mantém CRM, dados de clientes, pipelines. |

**Nota:** o Automation Receptionist é o cargo que o usuário descreveu como "especialista em automações para receber clientes em WhatsApp, Instagram comentários e DM." É um cargo de execução/configuração, não de estratégia. Reporta ao Automation Manager ou ao COO/CMO dependendo do estágio.

---

## DIVISÃO 12 — Dados & Analytics

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Dados | VP Data, Head of Data |
| VP | VP de Analytics | Head of Analytics |
| Director | Diretor de Data Engineering | Director of Data Engineering |
| Director | Diretor de Analytics | Director of Analytics & Insights |
| Director | Diretor de Data Science | Director of ML/AI |
| Manager | Data Engineering Manager | — |
| Manager | Analytics Manager | BI Manager |
| Manager | Data Science Manager | ML Manager |
| Senior IC | Staff Data Engineer | Senior Data Architect |
| Senior IC | Senior Data Scientist | Senior ML Engineer |
| Senior IC | Analytics Engineer | Analytics Architect |
| Specialist | Data Engineer | — |
| Specialist | Business Intelligence Analyst | BI Analyst, BI Developer |
| Specialist | Data Analyst | — |
| Specialist | ML Engineer | Machine Learning Engineer |

---

## DIVISÃO 13 — Segurança & Compliance

**Três camadas:** liderança (CISO/VP layer), operações de segurança (Red/Blue/Purple teams + Compliance), engenharia de segurança (Application Security Engineer, DevSecOps — listados em Divisão 3 por serem ICs de produto).

### Liderança

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Segurança | VP Security |
| VP | VP de Compliance / Risk | VP Risk Management |
| Director | Diretor de Security Engineering | Director of InfoSec |
| Director | **Diretor de SOC** | Head of Security Operations — lidera o Blue Team operacional. Distinct from Diretor de Security Engineering (arquitetura e código). |
| Director | Diretor de Compliance | Compliance Director |
| Manager | Security Engineering Manager | — |
| Manager | **SOC Manager** | Blue Team Lead — gerencia analistas SOC Tier 1/2/3 |
| Manager | Compliance Manager | Risk Manager |
| IC4–IC5 | Security Architect | — projeta arquitetura de segurança da empresa: zero trust, IAM strategy, data classification. |

### Red Team — Ofensivo

| Tier | Agente | Variações / Notas |
|---|---|---|
| IC3 | **Penetration Tester** | Ethical Hacker, Security Analyst (offensive) — testa defesas simulando ataques: web apps, APIs, redes, engenharia social. Produz relatório de vulnerabilidades por engajamento. Testes pontuais (por projeto). |
| IC4 | **Red Team Operator** | Adversary Simulation Specialist — campanhas avançadas e contínuas de simulação de adversários reais (APT emulation). Usa TTPs documentadas no MITRE ATT&CK framework. Distinct from Pen Tester: foco em bypass de defesas Blue Team existentes, campanhas multi-semana. |

### Blue Team — Defensivo (SOC)

| Tier | Agente | Variações / Notas |
|---|---|---|
| IC1–IC2 | **SOC Analyst Tier 1** | L1 SOC Analyst — primeira linha: triagem de alertas, descarte de falsos positivos, escalonamento de incidentes confirmados para Tier 2. Trabalha em turnos 24/7. Ferramentas: SIEM (Splunk, Microsoft Sentinel), EDR (CrowdStrike, SentinelOne). |
| IC2–IC3 | **SOC Analyst Tier 2** | L2 SOC Analyst — investigação profunda: correlaciona eventos, analisa logs, contém incidentes ativos, coordena resposta inicial. Distinct from Tier 1 (triagem) e Tier 3 (proativo/threat hunting). |
| IC4–IC5 | **SOC Analyst Tier 3 / Threat Hunter** | Senior Security Analyst, Threat Intelligence Lead — proativo: caça ameaças que ainda não geraram alertas, desenvolve detecções customizadas, orienta arquitetura defensiva. O mais sênior do Blue Team operacional. |
| IC3 | **Incident Responder** | IR Specialist, DFIR Analyst — resposta a incidentes ativos: contenção, erradicação, recuperação, análise pós-incidente. Distinct from SOC Tier 2 (detecta): o IR coordena a resposta executiva e gerencia o timeline do incidente. |
| IC3 | **Threat Intelligence Analyst** | CTI Analyst — coleta e analisa inteligência sobre ameaças externas: grupos APT, TTPs emergentes, IOCs, vulnerabilidades críticas no ecossistema. Alimenta o SOC com contexto de ameaças em tempo real. |
| IC3 | **Malware Analyst** | Reverse Engineer (security), Malware Researcher — engenharia reversa de samples de malware: comportamento, origem, impacto, IoCs. Ferramentas: Ghidra, IDA Pro, Cuckoo Sandbox, x64dbg. |
| IC3 | **Digital Forensics Analyst** | DFIR Analyst (forensics) — coleta e analisa evidências digitais após incidente: imagens de disco, análise de memória, cadeia de custódia. Relevante em violações com implicações legais ou regulatórias. |
| IC2–IC3 | **Vulnerability Analyst** | Vuln Management Specialist — ciclo de vulnerabilidades: scanning contínuo, priorização (CVSS + business context), tracking de remediação, reporting executivo. Ferramentas: Tenable/Nessus, Qualys, Rapid7 InsightVM. |

### Purple Team

| Tier | Agente | Variações / Notas |
|---|---|---|
| IC4 | **Purple Team Lead** | Purple Team Facilitator — coordena exercícios onde Red Team ataca e Blue Team defende em tempo real, compartilhando TTPs para melhorar ambas as partes. Não é um time permanente: é um modo de operação entre Red e Blue Teams maduros. Aparece em Series C+. |

### Compliance & Engenharia de Segurança

| Tier | Agente | Variações |
|---|---|---|
| Specialist | Security Engineer | — defesa de infraestrutura: firewalls, WAF, IAM, VPN, segurança de rede. Distinct from AppSec (código de produto) e SOC Analyst (monitoramento). |
| Specialist | Compliance Analyst | Risk Analyst — auditorias de conformidade (SOC2, ISO 27001, GDPR, HIPAA), manutenção de políticas, questionários de segurança de clientes. |

**Stage gate:** CISO ao seed (security-sensitive). SOC Tier 1 + Pen Tester ao Series A. Red Team Operator + SOC Tier 2/3 + Threat Intelligence ao Series B+. Purple Team em Series C+.

---

## DIVISÃO 14 — Jurídico & Comercial

| Tier | Agente | Variações |
|---|---|---|
| VP | VP Jurídico | VP Legal |
| VP | VP de Corporate Development | VP Corp Dev |
| Director | Diretor de Contratos | Director of Commercial Contracts |
| Director | Diretor de Propriedade Intelectual | Director of IP |
| Manager | Legal Manager | — |
| Manager | Contract Manager | — |
| Senior IC | Advogado / Counsel | Attorney, In-House Counsel |
| Specialist | Paralegal | Legal Analyst |
| Specialist | Contract Specialist | — |

---

## DIVISÃO 15 — Pessoas & RH

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Talent Acquisition | VP TA, Head of Recruiting |
| VP | VP de People Operations | VP HR Ops |
| VP | VP de L&D | VP Learning & Development |
| VP | VP de Comp & Benefits | VP Total Rewards |
| Director | Diretor de Talent Acquisition | TA Director |
| Director | Diretor de HR Operations | HR Ops Director |
| Director | Diretor de L&D | L&D Director |
| Manager | Recruiting Manager | — |
| Manager | HR Business Partner Manager | — |
| Manager | L&D Manager | — |
| Manager | Comp & Benefits Manager | Total Rewards Manager |
| Senior IC | Technical Recruiter | — |
| Senior IC | HR Business Partner | HRBP |
| Senior IC | L&D Specialist | Learning Specialist |
| Specialist | Recruiter | — |
| Specialist | HR Coordinator | HR Specialist |
| Specialist | Compensation Analyst | — |
| Specialist | Onboarding Coordinator | HR Onboarding Specialist |

---

## DIVISÃO 16 — Finanças & Contabilidade

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Finanças | VP Finance |
| VP | VP de FP&A | VP Financial Planning & Analysis |
| VP | VP de Contabilidade | VP Accounting, Controller (VP level) |
| Director | Controller / Diretor de Contabilidade | Director of Accounting |
| Director | Diretor de FP&A | FP&A Director |
| Director | Diretor de Investor Relations | IR Director |
| Manager | Accounting Manager | — |
| Manager | FP&A Manager | — |
| Senior IC | Senior Financial Analyst | Senior FP&A Analyst |
| Senior IC | Senior Accountant | — |
| Specialist | FP&A Analyst | Financial Analyst |
| Specialist | Accounts Payable / Receivable | AP/AR Specialist |
| Specialist | Bookkeeper | — |

---

## DIVISÃO 17 — Operações & Business Management

| Tier | Agente | Variações |
|---|---|---|
| VP | VP de Operações | VP Operations, Head of Ops |
| VP | VP de Business Operations | VP BizOps |
| Director | Diretor de Operações | Operations Director |
| Director | Diretor de Vendor Management | Procurement Director |
| Manager | Operations Manager | — |
| Manager | Business Operations Manager | BizOps Manager |
| Manager | Procurement Manager | Procurement & Vendor Manager |
| Manager | Facilities Manager | Office Manager (seed/Series A) |
| Senior IC | Business Operations Analyst | BizOps Analyst |
| Specialist | Operations Analyst | — |
| Specialist | Procurement Specialist | Vendor Management Specialist |
| Specialist | Project Coordinator | — |

---

## DIVISÃO 18 — TI & Operações de Infraestrutura Interna

**Distinct from Division 2 (Engineering):** enquanto Engineering constrói e opera o produto, TI opera a infraestrutura interna — computadores, redes, contas, dispositivos, helpdesk. Aparece em empresas com escritórios físicos ou times distribuídos que precisam de suporte de TI interno.

| Tier | Agente | Variações / Notas |
|---|---|---|
| Manager | **IT Manager** | Head of IT, IT Director (small company) — lidera toda operação de TI interna: helpdesk, infraestrutura de escritório, MDM (device management), políticas de acesso. |
| Specialist | **SysAdmin** | Systems Administrator, IT Systems Engineer — gerencia servidores internos, Active Directory/Okta, Google Workspace/Microsoft 365, backups, atualizações de sistema. **Distinct from Cloud Engineer** (que gerencia cloud de produto): este cuida da infra de escritório e colaboração. |
| Specialist | **Network Engineer** | Network Administrator — switches, firewalls, VPNs, monitoramento de rede, troubleshooting de conectividade. Relevante em empresas com escritórios físicos ou requisitos de rede segura. |
| IC1–IC2 | **Help Desk L1** | IT Support Technician (Tier 1) — primeira linha de suporte de TI: reset de senhas, setup de computadores novos, troubleshooting básico, acesso a sistemas. Trabalha com scripts e base de conhecimento. |
| IC2 | **Help Desk L2** | IT Support Technician (Tier 2) — problemas intermediários: software complexo, hardware, configurações de rede, integrações de sistemas internos. Escalona para L3 quando não resolve. |
| IC3 | **Help Desk L3** | IT Support Engineer (Tier 3) — problemas complexos escalados de L2: issues de sistema, bugs de infraestrutura interna, problemas sem solução documentada. Endpoint de escalação interno. |

**Stage gate:** SysAdmin ao seed quando equipe tem 10+ pessoas. IT Manager ao Series A. Help Desk L1/L2 ao Series B. Network Engineer quando há escritório físico ou requisitos de rede segura.
**Nota:** empresas 100% remote-first frequentemente terceirizam L1/L2 e mantêm apenas SysAdmin + IT Manager internos.

---

## Sistema de Agentes Conclave — Manifesto de Build

**Já construídos (11):** chairman · ceo · cto · cmo · cro · clo · ciso · design-cto · traffic-manager · social-media-manager · hr

---

## Framework de Modos de Trabalho

Todos os agentes compilados pelo HR devem definir trabalhos nos três modos. O HR inclui isso na compilação como seção `**WORK MODES**`.

| Modo | Cadência | Natureza |
|---|---|---|
| **Rotina** | Diário / Semanal | Trabalho recorrente que mantém o sistema operando — métricas, publicações, triagem |
| **Projeto** | 30–90 dias | Iniciativa com entrega e prazo definidos — lançamento, campanha, auditoria |
| **Estratégico** | Trimestral / Anual | Direção, pivôs, expansões, decisões de alto impacto |

---

## Processos-Âncora por Framework

Processos que atravessam múltiplos agentes. Cada agente relevante deve saber seu papel dentro do processo.

| Framework | Processo | Agentes responsáveis |
|---|---|---|
| **Lean Startup** (Ries) | Build-Measure-Learn cycle | CTO, Design CTO, Product Manager |
| **Lean Startup** | MVP definition + validated learning | CTO, CMO, CEO |
| **Lean Startup** | Pivot / Persevere decision | CEO, CTO, CMO |
| **Growth Hacking** (Ellis) | AARRR: Acquisition | CMO, Traffic Manager, BDR |
| **Growth Hacking** | AARRR: Activation | Design CTO, Product Manager, CRO Specialist |
| **Growth Hacking** | AARRR: Retention | VP Customer Success, Customer Success Manager, Email Marketing Manager |
| **Growth Hacking** | AARRR: Referral | CMO, Social Media Manager, Community Manager |
| **Growth Hacking** | AARRR: Revenue | CRO, RevOps Manager, Account Executive |
| **4HWW** (Ferriss) | Elimination — remover trabalho de baixo ROI | COO, CEO |
| **4HWW** | Automation — sistematizar antes de delegar | Automation Receptionist, Marketing Automation Specialist |
| **4HWW** | Delegation — quando escalar vs. executar | COO, HR |
| **Aquecimento de conta** | Gradual budget ramp + pixel warming + account history | Traffic Manager, Social Media Manager |
| **Construção de marca** | Positioning → Identity → Content → Community | CMO, Social Media Manager, Copywriter, Motion Designer |
| **Funil de vendas** | TOFU/MOFU/BOFU com benchmarks por estágio | CMO, CRO, Traffic Manager, BDR, Account Executive |
| **Validação de produto** | Smoke test → MVP → retention signal → PMF | CTO, Design CTO, Product Manager |
| **Observabilidade de métricas** | North Star metric + alertas por camada | CEO, CMO, CRO, CFO |
| **Compliance jurídico** | Verificação de deveres legais por milestone de receita | CLO, CFO |

---

## Mapa de Ativação por Gatilho Estratégico

Substitui o modelo de prioridade por estágio de funding. Agentes são ativados quando o gatilho ocorre.

| Gatilho | Evento | Agentes ativados | Processo-âncora |
|---|---|---|---|
| **G0** — Projeto iniciado | VISION.md criado | Chairman, CEO | — |
| **G1** — Produto definido | Hipótese de produto validada | CTO, Design CTO, Product Manager | Lean Startup MVP |
| **G2** — Canal orgânico escolhido | GTM motion = content / organic | CMO, Social Media Manager, Social Media Designer, Motion Designer, Copywriter | Construção de marca |
| **G3** — Tráfego pago iniciado | Budget alocado para paid acquisition | Traffic Manager, Analytics & Attribution Specialist | Aquecimento de conta |
| **G4** — Conta aquecida (30d) | Pixel ≥ 1k events, sem punições, histórico limpo | Performance Creative, CRO Specialist | Funil de vendas |
| **G5** — Audiência em construção | 1k seguidores / lista de email ativa | Email Marketing Manager, Content Strategist, Community Manager | AARRR: Activation |
| **G6** — Primeiros leads | Pipeline ≥ 10 leads qualificados | BDR, Cold Outreach Specialist, OSINT Specialist, Outbound Performance Analyst | Funil TOFU/MOFU |
| **G7** — Primeira venda | MRR > $0 | **CRO** (First Sale Protocol owner), Support Specialist, Automation Receptionist, Account Executive | AARRR: Revenue |
| **G8** — Funil validado | CAC payback < 12 meses | RevOps Manager, Sales Manager, Sales Enablement Manager, SDR | Funil de vendas |
| **G9** — PMF signals | NPS ≥ 40 OU crescimento orgânico consistente por 60d | VP Sales, VP Customer Success, VP Engineering, Customer Success Manager, VP Product | AARRR: Retention + Referral |
| **G10** — $10k MRR | Marco de receita | CFO, CLO (compliance check), FP&A Analyst, Data Analyst | Compliance jurídico |
| **G11** — $100k ARR | Inflexão de escala | CHRO, VP Marketing / VP Growth, Technical Recruiter, CISO (se não ativado), VP Data | Observabilidade de métricas |
| **G12** — Expansão jurídica | Novo mercado / nova entidade / GDPR scope | CLO (estrutura), CDO | Compliance jurídico |

---

## Manifesto de Build — Agentes por Gatilho

Ordem de build: G0 → G1 → G2... Dentro de cada gatilho: C-levels antes de specialists.
`slug` = nome do arquivo `agents/[slug].md` que o HR produz.

### G0 — Projeto iniciado
| Slug | Agente | Modos |
|---|---|---|
| chairman | Chairman / Board Facilitator | Estratégico | 
| ceo | CEO | Estratégico |
| coo | COO | Estratégico + Rotina |

### G1 — Produto definido
| Slug | Agente | Modos |
|---|---|---|
| cto | CTO | Estratégico |
| design-cto | Design CTO | Estratégico + Projeto |
| product-manager | Product Manager | Projeto + Rotina |
| full-stack-developer | Full Stack Developer | Projeto + Rotina |
| senior-frontend-engineer | Senior Frontend Engineer | Projeto + Rotina |
| senior-backend-engineer | Senior Backend Engineer | Projeto + Rotina |
| qa-engineer | QA Engineer | Rotina + Projeto |
| devops-engineer | DevOps / Cloud Engineer | Rotina |
| ai-engineer | AI Engineer | Projeto + Rotina |

### G2 — Canal orgânico
| Slug | Agente | Modos |
|---|---|---|
| cmo | CMO | Estratégico |
| social-media-manager | Social Media Manager | Rotina + Projeto |
| social-media-designer | Social Media Designer | Rotina |
| motion-designer | Motion Designer (Remotion) | Projeto + Rotina |
| copywriter-performance | Copywriter de Performance | Rotina + Projeto |
| creative-director | Diretor Criativo | Estratégico + Projeto |
| art-director | Art Director | Projeto + Rotina |
| video-editor | Video Editor | Rotina |

### G3 — Tráfego pago
| Slug | Agente | Modos |
|---|---|---|
| traffic-manager | Paid Traffic Manager / Gestor de Tráfego | Rotina + Projeto |
| analytics-attribution-specialist | Analytics & Attribution Specialist | Rotina |
| seo-manager | SEO Manager | Projeto + Rotina |

### G4 — Conta aquecida
| Slug | Agente | Modos |
|---|---|---|
| performance-creative | Performance Creative | Rotina + Projeto |
| cro-specialist | CRO Specialist | Projeto + Rotina |

### G5 — Audiência em construção
| Slug | Agente | Modos |
|---|---|---|
| email-marketing-manager | Email Marketing Manager | Rotina + Projeto |
| content-strategist | Content Strategist / Copywriter de Marca | Rotina + Projeto |
| marketing-automation-specialist | Marketing Automation Specialist | Projeto + Rotina |
| community-manager | Community Manager | Rotina |

### G6 — Primeiros leads
| Slug | Agente | Modos |
|---|---|---|
| bdr | BDR — Business Development Representative | Rotina |
| cold-outreach-specialist | Cold Outreach Specialist | Rotina + Projeto |
| osint-specialist | OSINT Lead Intelligence Specialist | Projeto |
| outbound-performance-analyst | Outbound Performance Analyst | Rotina |
| sales-automation-specialist | Sales Automation Specialist | Projeto + Rotina |
| data-enrichment-specialist | Data Enrichment Specialist | Rotina |
| appointment-setter | Appointment Setter | Rotina |

### G7 — Primeira venda
| Slug | Agente | Modos |
|---|---|---|
| cro | CRO — First Sale Protocol owner | Estratégico + Projeto |
| support-specialist | Support Specialist | Rotina |
| automation-receptionist | Automation Receptionist | Rotina |
| account-executive | Account Executive | Rotina + Projeto |

### G8 — Funil validado
| Slug | Agente | Modos |
|---|---|---|
| sdr | SDR — Sales Development Representative | Rotina |
| revops-manager | RevOps Manager | Rotina + Projeto |
| sales-manager | Sales Manager | Rotina + Estratégico |
| sales-enablement-manager | Sales Enablement Manager | Projeto |

### G9 — PMF signals
| Slug | Agente | Modos |
|---|---|---|
| vp-sales | VP de Vendas | Estratégico + Rotina |
| vp-customer-success | VP de Customer Success | Estratégico + Rotina |
| vp-engineering | VP de Engenharia | Estratégico + Rotina |
| vp-product | VP de Produto | Estratégico + Projeto |
| customer-success-manager | Customer Success Manager | Rotina |
| onboarding-specialist | Onboarding Specialist (CS) | Projeto + Rotina |
| support-engineer | Support Engineer Técnico | Rotina |

### G10 — $10k MRR
| Slug | Agente | Modos |
|---|---|---|
| cfo | CFO | Estratégico + Rotina |
| clo | CLO / General Counsel | Estratégico + Rotina |
| fpa-analyst | FP&A Analyst | Rotina + Projeto |
| data-analyst | Data Analyst | Rotina |

### G11 — $100k ARR
| Slug | Agente | Modos |
|---|---|---|
| chro | CHRO / VP People | Estratégico + Rotina |
| vp-marketing | VP de Marketing / VP de Growth | Estratégico |
| vp-data | VP de Dados / CDO | Estratégico + Projeto |
| ciso | CISO | Estratégico + Rotina |
| technical-recruiter | Technical Recruiter | Rotina + Projeto |
| hr-business-partner | HR Business Partner | Rotina |
| data-engineer | Data Engineer | Projeto + Rotina |
| analytics-engineer | Analytics Engineer | Rotina + Projeto |
| security-engineer | Security Engineer | Rotina |
| compliance-analyst | Compliance Analyst | Rotina + Projeto |
| influencer-marketing-manager | Influencer Marketing Manager | Projeto + Rotina |
| affiliate-marketing-manager | Affiliate Marketing Manager | Projeto + Rotina |

### G12 — Expansão jurídica
| Slug | Agente | Modos |
|---|---|---|
| cdo | CDO / Chief Data Officer | Estratégico |
| penetration-tester | Penetration Tester | Projeto |
| red-team-operator | Red Team Operator | Projeto |
| soc-analyst | SOC Analyst (Tier 1 / 2 / 3) | Rotina |
| incident-responder | Incident Responder | Projeto |
| threat-intelligence-analyst | Threat Intelligence Analyst | Rotina + Projeto |
| malware-analyst | Malware Analyst | Projeto |
| digital-forensics-analyst | Digital Forensics Analyst | Projeto |
| vulnerability-analyst | Vulnerability Analyst | Rotina |

### Especialistas de Escala — ativados por necessidade técnica, não por gatilho fixo
| Slug | Agente | Contexto de ativação |
|---|---|---|
| staff-engineer | Staff Engineer / Principal Engineer | Time engineering > 15 pessoas |
| sre | Site Reliability Engineer | Primeiro SLA formal com cliente |
| platform-engineer | Platform Engineer | Time engineering > 20 pessoas |
| cloud-architect | Cloud Architect | Custo cloud > $10k/mês ou multi-region |
| solutions-architect | Solutions Architect | Primeiro deal enterprise |
| tpm | Technical Program Manager | 3+ squads com dependências cruzadas |
| appsec-engineer | Application Security Engineer | Compliance SOC2 / PCI / HIPAA iniciado |
| devsecops-engineer | DevSecOps Engineer | Pipeline com security gates requerido |
| dba | Database Administrator | Performance de banco como gargalo recorrente |
| llm-engineer | LLM Engineer | Fine-tuning de modelos próprios |
| sdet | SDET | QA não acompanha ritmo de releases |
| performance-tester | Performance Tester | SLA de performance ou requisito de escala |
| mobile-developer | React Native Developer | Mobile multiplataforma pré-product/market fit |
| ios-developer | iOS Developer | Features nativas iOS críticas |
| android-developer | Android Developer | Features nativas Android críticas |
| embedded-engineer | Embedded / Firmware Engineer | Produto com componente físico / hardware |
| vp-revops | VP de Revenue Operations | Revenue Ops team > 3 pessoas |
| controller | Controller / Diretor de Contabilidade | Auditoria externa ou fundraising Series A+ |
| legal-counsel | Legal Counsel / Attorney | Volume de contratos > capacidade do CLO |
| growth-engineer | Growth Engineer | Marketing requer scripts, APIs ou tracking custom |
| podcast-producer | Podcast Producer | Podcast como canal de aquisição / autoridade |
| it-manager | IT Manager | Time > 30 pessoas com escritório físico |
| sysadmin | SysAdmin | Time > 10 pessoas |
| network-engineer | Network Engineer | Escritório físico ou rede segura requerida |
| purple-team-lead | Purple Team Lead | Red + Blue Teams maduros (Series C+) |

---

## Resumo

| Categoria | Agentes |
|---|---|
| Já construídos | 11 |
| G0 — Projeto | 3 |
| G1 — Produto | 9 |
| G2 — Canal orgânico | 8 |
| G3 — Tráfego pago | 3 |
| G4 — Conta aquecida | 2 |
| G5 — Audiência | 4 |
| G6 — Primeiros leads | 7 |
| G7 — Primeira venda | 4 |
| G8 — Funil validado | 4 |
| G9 — PMF signals | 7 |
| G10 — $10k MRR | 4 |
| G11 — $100k ARR | 12 |
| G12 — Expansão jurídica | 9 |
| Especialistas de escala | 25 |
| **Total** | **133 agentes** |

**Fusões documentadas:** Gestor de Tráfego = Paid Traffic Manager; Cold Email Copywriter = LinkedIn Outreach Specialist = Cold Outreach Specialist; WhatsApp + Instagram DM + Chatbot = Automation Receptionist; SOC Analyst Tier 1/2/3 = soc-analyst (modos internos); Help Desk L1/L2/L3 = um agent com tiers.

**Processos embeds:** Lean Startup (Build-Measure-Learn) · Growth Hacking (AARRR) · 4HWW (Elimination/Automation/Delegation) · Aquecimento de conta · Construção de marca · Funil de vendas · Validação de produto · Observabilidade de métricas · Compliance jurídico por milestone.

---

## CONCLAVE SYSTEM — ARCHITECTURE REFERENCE

> Machine-readable. Canonical single-source for system design decisions.
> English. Structured for fast agent parsing. Last updated: 2026-05-03.
> Package: conclave-cc/ v1.0.0 — pnpm recommended, npm fallback supported
> Claude system docs installed to: ~/.claude/docs/ (CONCLAVE_SYSTEM.md, ARCHITECTURE.md, ORCHESTRATION.md)
> Codex compat layer isolated to: D:/conclave-codex-layer/ (experimental — not part of Claude Code MVP)

---

### Two Phases — Critical Distinction

**GENESIS BUILD** — developer/maintainer use only:
- Tool: `/immortal-genesis` + HR agent, powered by the **immortal-engine**
- Purpose: constructs the 133-agent library from scratch
- Sequence: `/immortal-genesis init` (populate queue from this file) → `/immortal-genesis` (continuous build loop)
- Output: `agents/[slug].md` files committed to the conclave-cc repo
- Who runs it: einstenthedeveloper, building the pre-built agent library that ships in the npm package
- End state: all 133 agents compiled and committed → pnpm publish → v1.0.0

**RUNTIME** — end-user use:
- Tool: `/conc` is the unified runtime entrypoint. In Claude Code it is a slash command; in Codex it is exposed by the local `conclave` plugin. `/conclave` is the Chairman bootstrap entrypoint, not an alias for `/conc`.
- Purpose: activates the pre-built system for a specific project
- Sequence: /conc -> queue check -> Chairman if no VISION.md -> CEO -> C-levels -> Specialists
- Users never run `/immortal-genesis` — the agents are already compiled in the package they installed
- End state: VC-ready document package (VISION, TECH, GTM, REVENUE, COMMERCIAL, etc.)

---

### Session Upgrade — 2026-05-01

Completed in this session:

- HR genesis library is closed locally: root `conclave-queue.json` now records **122/122** `agent-build` items as `done` (domain specialists). The 10 orchestrator agents were developed separately and committed as part of v1.0.0.
- The compiled library in `conclave-cc/agents/` contains **133** role files (122 domain specialists + 10 orchestrators + hr.md). `conclave-cc/ROLES/` contains matching research files plus `_SCHEMA.md` and `_HR_INDEX.md`.
- The packaged maintainer queue was reset to future review mode: `conclave-cc/conclave-queue.json` now contains **4 pending 90-day HR review items**.
- A root meta-package layer was added: `package.json` + `bin/conclave.js`. Purpose: detect/install the Claude adapter and the Codex adapter from one entrypoint.
- A shared strategic prompt layer was added in `conclave-core/prompts/`: `chairman.md`, `ceo.md`, `cto.md`, `cmo.md`, `cro.md`, `clo.md`, `ciso.md`, `design-cto.md`.
- A Codex bridge plugin was added at `plugins/conclave/.codex-plugin/plugin.json` with skill surfaces for `/conc`, `/conclave`, `/ceo`, `/cto`, `/cmo`, `/cro`, `/clo`, `/ciso`, and `/design-cto`.
- The existing `plugins/immortal-genesis` plugin remains the Codex maintainer bridge for HR queue work.
- `.agents/plugins/marketplace.json` now exposes both local plugins: `conclave` and `immortal-genesis`.
- The shared core prompt layer was installed into Claude home at `~/.claude/conclave-core/prompts/`.
- `conclave-cc` received git commit `fd0f051` with message `v1`.

Important distinction:

- The `conclave-cc` repository is versioned and now contains the `v1` commit.
- The workspace root `D:/conclave` is **not** a git repository yet, so the root-level cross-runtime adapter files (`bin/`, `conclave-core/`, `plugins/conclave/`, root `package.json`, root `README.md`) are not versioned by that commit.

---

### Workspace Tree

```
D:/conclave/conclave-cc/             # publishable npm package (nested git repo, commit fd0f051 — v1.0.0)
├── agents/                          # 133 compiled role files:
│                                    #   10 orchestrators (chairman, ceo, cto, cmo, cro, clo, ciso,
│                                    #                      design-cto, traffic-manager, social-media-manager)
│                                    #   5 functional C-levels (cfo, cdo, coo, chro, cpo)
│                                    #   118 domain specialists + hr.md
├── commands/                        # Claude slash-command layer
│   ├── conc.md                      # unified runtime entrypoint (/conc)
│   ├── conclave.md                  # Chairman bootstrap (/conclave)
│   ├── ceo.md
│   └── immortal-genesis*.md         # dev-only build commands
├── docs/                            # CONCLAVE_SYSTEM.md, ARCHITECTURE.md, ORCHESTRATION.md
├── knowledge/                       # INDEX.md + 111 knowledge corpus files
├── mcp/                             # in-house MCP servers (bundled — auto-registered on install)
│   ├── usage/                       # token budget awareness → feeds conclave-usage protocol
│   │   ├── package.json
│   │   └── src/index.js
│   ├── interface-controller/        # browser automation via Playwright
│   │   ├── server.py                # MCP server entry point
│   │   ├── browser.py               # navigate, click, type, upload, screenshot tools
│   │   ├── logger.py
│   │   ├── requirements.txt
│   │   └── README.md
│   └── README.md                    # MCP index + in-house roadmap (P0/P1/P2)
├── ROLES/                           # _SCHEMA.md, _HR_INDEX.md + 133 role research files
├── scripts/                         # dev-only tools (excluded from user install via .npmignore)
│   ├── immortal_genesis.py          # HR queue orchestrator (GENESIS BUILD only)
│   └── complete_hr_queue.py
├── templates/                       # doc templates: VISION, EXECUTION_PLAN, TECH, GTM,
│                                    # REVENUE, COMMERCIAL, SECURITY, PRODUCT
├── architecture.md                  # this file — single source of truth (renamed from organagram-research.md)
├── SECURITY.md                      # security policy: 6 principles + in-house MCP strategy
├── conclave-queue.json              # HR review queue: 4 pending 90-day review items
├── install.js                       # adapter installer + MCP auto-registration (non-destructive merge)
├── package.json                     # v1.0.0, pnpm-first
├── .npmrc                           # engine-strict=true, audit-level=moderate, strict-peer-dependencies=true
├── pnpm-lock.yaml
└── README.md

D:/conclave-codex-layer/             # Codex compat layer — isolated, experimental, NOT part of Claude Code MVP
├── bin/conclave.js                  # cross-runtime detector + adapter installer (1312 lines)
├── conclave-core/                   # shared C-suite strategic briefs
│   └── prompts/
│       ├── chairman.md, ceo.md, cto.md, cmo.md
│       ├── cro.md, clo.md, ciso.md, design-cto.md
├── plugins/
│   ├── conclave/                    # Codex bridge: /conc, /conclave, /ceo, /cto, /cmo, /cro, /clo, /ciso
│   └── immortal-genesis/            # Codex bridge: HR queue (maintainer only)
├── .agents/plugins/marketplace.json # Codex local marketplace: conclave + immortal-genesis
├── conclave-queue.json              # historical genesis build log: 122 done items
├── package.json                     # meta-package wrapper (package name: conclave)
└── README.md                        # purpose + how to resume this frente when needed

~/.claude/ after pnpm install conclave-cc:
├── agents/                          # 133 compiled role files
├── commands/                        # conc.md, conclave.md, ceo.md, immortal-genesis*.md + skills/
├── docs/                            # CONCLAVE_SYSTEM.md, ARCHITECTURE.md, ORCHESTRATION.md
├── knowledge/                       # INDEX.md + knowledge corpus
└── settings.json                    # mcpServers registered (non-destructive merge):
                                     #   conclave-usage:     node   mcp/usage/src/index.js
                                     #   conclave-interface: python mcp/interface-controller/server.py
```

---

### Genesis Build Sequence

```
1. /immortal-genesis init → reads this file (Agent Inventory table) → writes conclave-queue.json
                            → local historical queue currently shows 122 completed build items
2. Current maintainer path in Codex:
                            `immortal-genesis` plugin skill + `conclave-cc/scripts/immortal_genesis.py`
                            → select next role / inspect status / update queue state
                            → no native `ScheduleWakeup` auto-loop in Codex; resume is manual across turns
3. HR builds one role at a time
                            → Research Protocol (Steps 1–6) + checklist + compile
                            → writes: `conclave-cc/agents/[slug].md` + `conclave-cc/ROLES/[slug].md` + `conclave-cc/knowledge/` stubs
4. Current local state after this session
                            → 133 compiled roles present in `conclave-cc/agents/` (122 domain + 10 orchestrators + hr)
                            → matching research files in `conclave-cc/ROLES/`
                            → `conclave-cc/conclave-queue.json` reduced to 4 future 90-day review items
5. `conclave-cc` versioned state
                            → git commit `fd0f051` with message `v1`
```

---

### Layer Map

| Layer | Agent(s) | Activated by | Output | Periodization |
|---|---|---|---|---|
| **Board** | Chairman | Founder via /conclave | VISION.md | Initiation (new project) + Review (quarterly / FRAGILE / kill-pivot) |
| **Orchestration** | CEO | /conc after VISION.md exists | EXECUTION_PLAN.md | Every session |
| **C-levels** | CTO, CMO, CRO, CLO, CISO, Design CTO, CFO | CEO via activation matrix | Domain docs (TECH, GTM, REVENUE, COMMERCIAL, SECURITY, PRODUCT, FINANCE) | Per activation signal; re-activated on iteration trigger |
| **Specialists** | Traffic Manager, Social Media Manager, HR, future operational | Founder directly OR CEO delegation | TRAFFIC.md, content batches, ROLES/ | On-demand; ADVISORY MODE if parent C-level doc missing |

**Access rules:**
- Founder → C-levels: Q&A always allowed; full run always allowed
- Founder → Specialists: Q&A always allowed; output doc requires parent C-level doc (else ADVISORY MODE)
- CEO → Specialists: never direct activation (use CONSULTATION_PROTOCOL via C-levels)
- Chairman → never called by CEO; founder-only activation

---

### Agent Inventory

Note: all 133 agents are compiled and present in `conclave-cc/agents/` as of v1.0.0. The 10 orchestrators (chairman → social-media-manager) ship in the package for the first time in this release — previously they existed only in `~/.claude/agents/` locally. Status = `built` means the agent file is compiled, committed, and runtime-ready in Claude Code.

| Slug | Layer | Parent doc required | Output doc | CEO activation signal | Status |
|---|---|---|---|---|---|
| `chairman` | Board | none | VISION.md | /conclave (always first) | built |
| `ceo` | Orchestration | VISION.md | EXECUTION_PLAN.md | /conc (always second) | built |
| `cto` | C-level | VISION.md + EXECUTION_PLAN.md | TECH.md | product_exists = yes | built |
| `cmo` | C-level | VISION.md + EXECUTION_PLAN.md | GTM.md | distribution_defined = no | built |
| `cro` | C-level | VISION.md + EXECUTION_PLAN.md | REVENUE.md | revenue_model_defined = no | built |
| `clo` | C-level | VISION.md + EXECUTION_PLAN.md | COMMERCIAL.md | legal_commercial_complexity = medium or high | built |
| `ciso` | C-level | VISION.md + TECH.md | SECURITY.md | security_sensitive = yes AND TECH.md exists | built |
| `design-cto` | C-level | VISION.md + GTM.md | PRODUCT.md | ux_critical = yes AND GTM.md exists | built |
| `traffic-manager` | Specialist | GTM.md | TRAFFIC.md | traffic_strategy_needed = yes AND GTM.md exists | built |
| `social-media-manager` | Specialist | GTM.md | content_batch_YYYY-WW.md | organic channel in GTM.md AND GTM.md exists | built |
| `hr` | Specialist | none (meta-agent) | ROLES/[role].md + agents/[role].md | founder or CEO needs new role | built |
| `cfo` | C-level | all docs | FINANCE.md | funding_intent = yes AND stage = post_mvp | built |
| `cdo` `coo` `chro` `cpo` | C-level | varies | varies | CEO activation matrix signals | built |
| *(118 domain specialists)* | Specialist | varies | varies | context trigger (see G0-G12 manifest above) | built |

---

### Authority Constitution

| Domain | Authority holder | Overrides |
|---|---|---|
| GTM / channel strategy | CMO | Traffic Manager, Social Media Manager |
| Revenue model / pricing | CRO | CMO (on pricing), CEO (on revenue projections) |
| Technical feasibility | CTO | all agents |
| Legal / compliance | CLO | all agents |
| Product experience | Design CTO | Social Media Manager (on visual brand) |
| Security posture | CISO | CTO (on security-specific technical decisions) |
| Project kill / portfolio allocation | Chairman | CEO, all C-levels |
| Orchestration sequence | CEO | C-level activation order only |

Conflict resolution: CEO identifies conflict → determines domain → lower-priority agent revises → no dual values allowed.

---

### Document Registry

| Document | Owner | Depends on | Required for |
|---|---|---|---|
| VISION.md | Chairman | — | everything |
| EXECUTION_PLAN.md | CEO | VISION.md | all C-level activations |
| TECH.md | CTO | VISION.md, EXECUTION_PLAN.md | SECURITY.md |
| GTM.md | CMO | VISION.md, EXECUTION_PLAN.md | TRAFFIC.md, PRODUCT.md, content_batch |
| TRAFFIC.md | Traffic Manager | VISION.md, GTM.md | — |
| REVENUE.md | CRO | VISION.md, EXECUTION_PLAN.md | FINANCE.md |
| COMMERCIAL.md | CLO | VISION.md, EXECUTION_PLAN.md | FINANCE.md |
| SECURITY.md | CISO | VISION.md, TECH.md | FINANCE.md |
| PRODUCT.md | Design CTO | VISION.md, GTM.md | FINANCE.md |
| FINANCE.md | CFO | all above | — (post-MVP) |
| content_batch | Social Media Manager | GTM.md | — (operational) |
| ROLES/[role].md + agents/[role].md | HR | role name input | — (on-demand) |

---

### CEO Activation Matrix

| Signal in VISION.md | Condition | Agent activated |
|---|---|---|
| product_exists = yes | always | CTO |
| distribution_defined = no | always | CMO |
| revenue_model_defined = no | always | CRO |
| legal_commercial_complexity = medium or high | always | CLO |
| security_sensitive = yes | TECH.md exists | CISO |
| ux_critical = yes | GTM.md exists OR CMO active | Design CTO |
| traffic_strategy_needed = yes | GTM.md exists AND TRAFFIC.md not present | Traffic Manager |
| funding_intent = yes | stage = post_mvp | CFO |

**Parallel eligibility** (requires percent_used < 50 AND no dependency overlap):
- CMO + CRO: eligible
- CTO + CLO: eligible
- All other pairs: ineligible (dependency overlap)

---

### Chairman Periodization

**INITIATION MODE** — new project:
- Trigger: /conclave on project with no VISION.md, or founder requests new session
- Protocol: Layer A (raw intent, max 3 Q/turn, binary/constrained) → Layer B (Pre-Mortem + Assumption Mapping + Sovereignty Filter) → 3-Strategy fork if HIGH consequence → Chairman Scoring Matrix (7 dimensions, 35 pts max) → write VISION.md

**REVIEW MODE** — triggered by any of:
- (a) 90 days since VISION.md session date (surfaced by /conc Step 2)
- (b) CEO reports system_status = FRAGILE
- (c) Founder requests kill or pivot decision
- (d) First sale failed + core assumption invalidated

**Review protocol:** read existing VISION.md → re-challenge changed signals only → re-run Sovereignty Filter if dependencies changed → re-score Matrix → update Change Log + status → brief CEO on what changed.

**Never:** called by CEO. Never rewrites full VISION.md in Review mode. Never updates VISION.md during CEO iteration loops.

**Score thresholds:** < 21 = BLOCKED (kill recommendation); 21–27 = WATCHLIST; ≥ 28 = ACTIVE.

---

### Specialist Access Rules

| Scenario | Allowed action |
|---|---|
| Founder asks specialist a question (no parent doc) | ADVISORY MODE: answer freely, explain frameworks |
| Founder asks specialist to produce output doc (no parent doc) | ADVISORY MODE: refuse output doc, recommend /conclave |
| Founder asks specialist to produce output doc (parent doc exists) | Full execution |
| C-level consults specialist (CONSULTATION_PROTOCOL) | Validate only, < 200 tokens, CLEAR or BLOCKER |
| CEO activates specialist directly | Not allowed — must go through C-level or founder |

**Parent doc requirements:**
- Traffic Manager → GTM.md
- Social Media Manager → GTM.md
- All future operational specialists → defined at compilation time in their agent file

---

### Token Budget Protocol

| percent_used | Recommendation | CEO action |
|---|---|---|
| < 50 | parallel | eligible for parallel activation if dependency_overlap = none |
| 50–70 | sequential | sequential always |
| 70–85 | sequential_warn | sequential + notify founder |
| > 85 | pause | write Execution State to EXECUTION_PLAN.md, instruct /conc new session |

Fallback if conclave-usage-mcp not installed: default sequential.

---

### Forbidden Actions

- Agent writing another agent's document
- Agent asking open-ended question (binary/constrained only, max 3)
- Agent leaving a field empty (use UNRESOLVED_HYPOTHESIS)
- CEO activating an agent before its dependencies exist
- Parallel execution with dependency overlap
- Parallel execution when percent_used ≥ 50
- System continuing after BLOCKED without founder resolution
- VISION.md updated outside a Chairman session
- CFO activation before post_mvp stage
- Dual values on any field after conflict resolution
- Agent applying a framework from memory — load the skill file
- CEO activating agents without including skill routing in the brief
- More than 1 STRATEGY_FORK per session
- Consultation exchange exceeding 3 rounds — escalate to UNRESOLVED_HYPOTHESIS
- Chairman called by CEO
- Specialist writing output doc without parent C-level document

---

### immortal-genesis status — 2026-05-03

**GENESIS BUILD is complete.** All 133 agents are compiled and committed to `conclave-cc/agents/`. The queue in `conclave-cc/conclave-queue.json` contains only 4 pending 90-day HR review items.

**Codex layer isolated:** The `/immortal-genesis` Codex plugin skill and its bridge files (`bin/conclave.js`, `plugins/immortal-genesis/`, `.agents/`) have been moved to `D:/conclave-codex-layer/` and are no longer part of the Claude Code MVP package. The Python queue runner (`conclave-cc/scripts/immortal_genesis.py`) is dev-only and excluded from the user install.

**Claude Code implementation** (active, in-package):
- `/immortal-genesis` slash command in `conclave-cc/commands/` — for future maintenance use inside Claude Code
- `conclave-cc/scripts/immortal_genesis.py` — queue runner (dev-only, not installed to `~/.claude/`)
- `conclave-cc/conclave-queue.json` — 4 pending 90-day review items

**Codex layer** (isolated to `D:/conclave-codex-layer/`, paused):
- `/immortal-genesis` as a Codex-local plugin-backed skill
- `init`, `status`, `next`, and `set-status` queue operations through the Python runner
- Historical build log: root `conclave-queue.json` — 122 items, all `done`

**To resume Codex frente:** `cd D:/conclave-codex-layer/` and restore the plugin with `codex plugin install ./.agents/plugins/marketplace.json`.

Session outcome that produced this state:
- `conclave-cc/agents/`: 123 compiled roles (122 + hr.md) — 10 orchestrators added → 133 total at v1.0.0
- `conclave-cc` committed as `fd0f051` (`v1`) — bump to v1.0.0 in progress

---

### immortal-engine + /immortal-genesis

**Scope:** GENESIS BUILD only — developer tool for constructing the agent library. Not shipped for end-user use.

**immortal-engine** — the pacing mechanism:
```
ScheduleWakeup (timer) + conclave-usage-mcp (budget sensor) + conclave-queue.json (state)
```
Pauses at 95% session budget. Checks every 30 min whether budget has reset. Resumes automatically when a new session starts. Cannot be killed by context limits.

**Command:** `/immortal-genesis` — starts continuous build loop via immortal-engine
**Subcommands:** `/immortal-genesis init` · `/immortal-genesis status` · `/immortal-genesis [slug]`
**State file:** `conclave-queue.json` (survives compaction and session restarts)
**Builder:** HR agent (sole builder — /immortal-genesis is scheduler and state manager only)

**Queue priority:**
- P0: Board + C-level core (Chairman, CEO, CTO, CMO, CRO, CLO, CISO, Design CTO)
- P1: Operational specialists activated at G0-G4 triggers
- P2: Specialists activated at G5-G9 triggers
- P3: Enterprise/context-specific specialists (G10-G12)

**Budget thresholds:**
- ≥ 95%: PAUSE — ScheduleWakeup(1800s) to check if session reset
- 70–94%: THROTTLE — one agent per iteration + 180s wakeup
- < 70%: FULL SPEED — continuous, 90s wakeup

**After all agents built:** commit agents/ + ROLES/ + knowledge/ → bump version → `git tag v1.0.0 --push` → GitHub Actions publishes to npm.

---

### Security Model

Based on `sec-search.md` analysis. Full policy in `conclave-cc/SECURITY.md`.

| Principle | Application in Conclave |
|---|---|
| **Least Privilege** | Each `agents/[slug].md` declares `tools:` in frontmatter. CFO has no access to social posting; Social Media Manager has no access to financial data. |
| **Sandboxing** | Agents run via Task subagent (isolated context). Skills touching ads spend, posting, or contracts require interactive HITL confirmation before writing. |
| **Strong Auth (JIT tokens)** | No secrets in agent files or ROLES/. All tokens via env vars (`.env` gitignored). Short-lived tokens recommended for API integrations (ads, social). |
| **PII Masking** | Before sending customer data to LLM: mask CPF, email, phone. Future `conclave-pii-scrubber` MCP (P0 roadmap) will automate this at the tool boundary. |
| **Audit + HITL** | Every agent write logs to `conclave-audit.log` (timestamp, slug, file, hash). High-risk actions (ad spend, live posting, contract signing) require human approval. |
| **Prompt-Injection Defense** | All slash command inputs validated structurally before becoming prompts. Agent outputs validated before being passed to next agent in chain. |
| **Package Manager** | **pnpm** as default (content-addressable store, no phantom dependencies, supply chain protection). npm fallback documented. `engine-strict=true` in `.npmrc`. |

---

### In-House MCP Strategy

**Principle:** every MCP that touches sensitive data (ads, social, finance, PII) is built and owned internally. This reduces the ongoing security audit surface to a fixed, self-controlled set — no third-party upgrade cycles reopening the analysis.

#### Current in-house MCPs (bundled in `mcp/`)

| MCP | Path | Status | Function |
|---|---|---|---|
| **conclave-usage** | `mcp/usage/` | Functional | Token budget awareness — feeds `percent_used` to CEO activation protocol |
| **interface-controller** | `mcp/interface-controller/` | In development | Browser automation via Playwright: navigate, click, type, upload, screenshot |

#### MCP roadmap

| Priority | MCP | Function | Replaces external dependency |
|---|---|---|---|
| P0 | **conclave-audit** | Centralized audit log — all agent reads/writes with timestamp, slug, hash | Datadog Audit, Splunk |
| P0 | **conclave-pii-scrubber** | Masks PII (CPF, email, phone) before data reaches LLM | AWS Comprehend, Microsoft Presidio |
| P1 | **conclave-parallel-dispatch** | Parallel subagent dispatch (Claude `claude -p` pattern) | /octo parallel skills |
| P1 | **conclave-ads-connector** | Least-privilege, JIT-token access to Google Ads / Meta Ads | Third-party ad plugins |
| P2 | **conclave-social-poster** | Posts to social media with mandatory HITL approval gate | Buffer, Hootsuite plugins |
| P2 | **conclave-git-vault** | Versions strategic docs (VISION, EXECUTION_PLAN) with encryption | GitHub MCP |

**External plugins as architectural inspiration only** — `/octo`, GitHub MCP, Filesystem MCP etc. were researched during development and inform patterns (subprocess dispatch, tool boundary scoping, path validation) but are NOT runtime dependencies of Conclave.

#### install.js auto-registration

On `pnpm install conclave-cc`, `install.js` merges MCPs into `~/.claude/settings.json` non-destructively:

```json
{
  "mcpServers": {
    "conclave-usage": { "command": "node", "args": ["<package>/mcp/usage/src/index.js"] },
    "conclave-interface": { "command": "python", "args": ["<package>/mcp/interface-controller/server.py"] }
  }
}
```

Existing user `mcpServers` entries are preserved. Each MCP exposes a `--diagnose` flag for post-install health check.
