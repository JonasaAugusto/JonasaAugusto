<div align="center">

<a href="https://github.com/JonasaAugusto">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=28&duration=3000&pause=1000&color=FFFFFF&center=true&vCenter=true&width=650&lines=Jonas+Augusto;Desenvolvedor+Backend;Automa%C3%A7%C3%A3o+%26+Agentes+de+IA;Python+%7C+FastAPI+%7C+LLMs+%7C+Docker" alt="Typing SVG" />
</a>

<br/><br/>

<a href="https://www.linkedin.com/in/jonasaaugusto" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>
<a href="https://jonasaaugusto.github.io" target="_blank">
  <img src="https://img.shields.io/badge/Portfólio-0c87eb?style=for-the-badge&logo=firefox&logoColor=white" alt="Portfolio"/>
</a>
<a href="https://jonasaaugusto.github.io/JonasAugusto_cv_m.pdf" target="_blank">
  <img src="https://img.shields.io/badge/Currículo-333333?style=for-the-badge&logo=readdotcv&logoColor=white" alt="CV"/>
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Uptime%20em%20produção-99,97%25-green?style=flat-square" />
<img src="https://img.shields.io/badge/Latência%20IA-15min%20→%2027s-green?style=flat-square" />
<img src="https://img.shields.io/badge/Downtime%20RPA-−93,5%25-green?style=flat-square" />
<img src="https://img.shields.io/badge/CR%20Acadêmico-9,3%2F10-blue?style=flat-square" />

</div>

---

## Sobre

Desenvolvedor **Backend especializado em automação inteligente e agentes de IA**. Hoje mantenho em produção 24/7 uma plataforma autônoma de conversão de leads: agente de IA sobre WhatsApp Business API, pipeline de OCR, máquina de estados de 9 etapas e integrações com APIs de parceiros — arquitetura distribuída em 2 VPS.

Meu trabalho vive na interseção entre **Backend, LLMOps e confiabilidade em produção**: orquestração com LLMs (OpenAI, Anthropic, DeepSeek), engenharia reversa de APIs sem documentação, retry patterns, observabilidade e otimização de latência crítica.

Estudante de Engenharia de Software na Estácio (CR 9,3/10, formatura em dez/2026). Inglês C1.

📍 Juiz de Fora, MG &nbsp;·&nbsp; 📧 jonasaugustoprofissional@gmail.com &nbsp;·&nbsp; 🌐 [jonasaaugusto.github.io](https://jonasaaugusto.github.io)

---

## 🏗 Caso de Estudo — Plataforma Autônoma de Conversão de Leads

> Sistema em produção 24/7 na F5 Tecnologia. Recebe leads via WhatsApp, conduz o atendimento completo com um agente de IA, coleta dados, gera propostas de crédito junto a um parceiro financeiro e cadastra clientes em programas de energia. Atuei de ponta a ponta: arquitetura, agente, integrações e confiabilidade.

<details open>
<summary><strong>Arquitetura & o que construí</strong></summary>

<br/>

**Arquitetura distribuída** — separei a carga em 2 VPS: uma leve para webhook, agente de IA e orquestração; outra dedicada à automação de navegador (Playwright), que consumia CPU/memória pesadamente. O isolamento eliminou contenção de recursos e estabilizou o atendimento em tempo real.

- **Agente de IA generativa** (OpenAI GPT com fallback), prompt estruturado por etapa, contexto isolado por lead e guardrails anti-alucinação — nunca confirma um resultado sem retorno real da API.
- **Pipeline de OCR** que lê contas de luz (foto ou PDF, inclusive protegidos por senha), extrai consumo em kWh e detecta imagens ilegíveis solicitando reenvio automaticamente.
- **Máquina de estados de 9 etapas** com persistência isolada por lead — o atendimento retoma exatamente de onde parou se a conversa cair.
- **Integração com API de parceiro de crédito** (pré-análise, simulação, upload de documentos, polling assíncrono) e automação web dos portais de energia via Playwright.
- **Roteamento inteligente** de cada lead para o parceiro de energia correto conforme consumo e estado, derivando a UF a partir do CEP quando ausente.

</details>

<details>
<summary><strong>Problemas que resolvi</strong></summary>

<br/>

**🔴 Webhook morto — 43 propostas congeladas**  
Um webhook de desfecho parou de ser entregue por 4 dias, deixando 43 propostas travadas em "processando". Rastreei do sintoma à raiz (logs → estado no banco → polling) e implementei um job systemd de polling ativo a cada 5 minutos.  
→ **43 propostas aprovadas recuperadas**; backlog travado caiu de 28 para 3 leads.

**🔴 Race condition no takeover humano**  
Quando um atendente entrava na conversa, o bot não pausava e ambos respondiam juntos. Corrigi com normalização robusta de telefone e reverificação de estado imediatamente antes do envio.  
→ **Handoff humano seguro**, sem respostas duplicadas.

**🔴 Latência de OCR + decisão de rota**  
→ **8s → 3,2s** com cache inteligente (TTL) e batching de requisições.

</details>

<details>
<summary><strong>Confiabilidade, infra e segurança</strong></summary>

<br/>

- Serviços **systemd** com auto-restart, health checks, watchdogs de sincronização de estado e renovação automática de tokens antes da expiração.
- Camada de saída de rede configurável para entrega confiável a serviços externos com conectividade instável — sem acoplar lógica de negócio à infraestrutura.
- **Throttling com backoff exponencial** para respeitar rate limits e operar como cliente bem-comportado dos parceiros.
- **LGPD**: criptografia em repouso, transmissão via HTTPS com JWT, política de retenção e isolamento de contexto entre leads.
- **Observabilidade**: logging estruturado em JSON, dashboard em tempo real e alertas automáticos (Slack/Email) para saúde das VPS e falhas de webhook.

</details>

<div align="center">

| ~200 | 99,97% | 1,2s | 43 |
|:---:|:---:|:---:|:---:|
| leads/dia | uptime | latência média | propostas recuperadas |

</div>

`Python` `FastAPI` `Flask` `OpenAI API` `LangChain` `Playwright` `PostgreSQL (Supabase)` `Redis` `WhatsApp Business API` `systemd` `nginx` `Docker` `Linux`

📄 [Ver caso de estudo completo no portfólio →](https://jonasaaugusto.github.io/#experiencia)

---

## Projetos

| | Projeto | Descrição | Stack |
|---|---|---|---|
| ⭐ | **[IAprovale](https://github.com/JonasaAugusto/IAprovale)** `Live` | Backend com orquestração inteligente de buscas via DeepSeek LLM e **MCP** para integração com a PCI Concursos. Auth JWT, deduplicação de resultados e persistência versionada. Cliente desktop em PySide6; web em desenvolvimento. Deploy versionado em Render. [Home](https://jonasaaugusto.github.io/IAprovale/) | Python · FastAPI · DeepSeek · MCP · Supabase |
| 🟣 | **[NotaME](https://github.com/JonasaAugusto/NotaME)** | App mobile/desktop para emissão de NFS-e, recibos em PDF e gestão de clientes. Offline-first com SQLite e sincronização P2P em rede local com criptografia AES-256. | C# · .NET MAUI · SQLite · QuestPDF |
| 🟦 | **VoxAI** `Em Dev` · `código privado` | Transcrição offline de áudio/vídeo com Whisper **on-device** (Android/iOS). Registra-se como *share target* do SO, faz demuxing e normalização via FFmpeg (WAV PCM 16kHz mono) e roda a inferência em serviço de background durável. Seleção dinâmica de modelo por perfil de hardware para blindar contra OOM, cache FIFO com teto parametrizável e histórico em SQLite. **Custo de infraestrutura: R$ 0,00** — zero chamada de nuvem. | C# · .NET MAUI · Whisper · FFmpeg · SQLite |
| 🔵 | **[LogiTrack API](https://github.com/JonasaAugusto/logitrackAPI)** `Live` | API RESTful de logística: gestão de frotas e entregas com rastreamento em tempo real, relatórios assíncronos, auth JWT e deploy containerizado. [Swagger](https://logitrackapi.onrender.com/docs) | Python · FastAPI · PostgreSQL · Docker · JWT |

<details>
<summary><strong>Outros projetos</strong></summary>

<br/>

| Projeto | Descrição | Stack |
|---|---|---|
| [QR Code Generator](https://github.com/JonasaAugusto/qrcode-generator) | Geração dinâmica de QR Codes com histórico, salvamento local e geração em lote. Benchmark: 30 usuários em 0,65s / 5 mil em 1,8min. | Python · Pillow · Threading |
| [Discord Zombot](https://github.com/JonasaAugusto/DiscordChatBot_Zombot) | Chatbot para servidores de jogos com moderação automática e tutoriais interativos — NPS +35%. | Python · Discord.py |

</details>

---

## Stack Tecnológica

**IA Generativa & LLMOps**

![OpenAI](https://img.shields.io/badge/OpenAI%20API-412991?style=flat-square&logo=openai&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic%20Claude-D97757?style=flat-square&logo=anthropic&logoColor=white)
![DeepSeek](https://img.shields.io/badge/DeepSeek-4D6BFE?style=flat-square&logo=deepseek&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-000000?style=flat-square&logo=modelcontextprotocol&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3B57?style=flat-square&logo=chainlink&logoColor=white)
![Whisper](https://img.shields.io/badge/Whisper%20on--device-000000?style=flat-square&logo=openai&logoColor=white)

**Backend & Automação**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![.NET MAUI](https://img.shields.io/badge/.NET%20MAUI-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white)
![Webhooks](https://img.shields.io/badge/Webhooks-FF6C37?style=flat-square&logo=webhooks&logoColor=white)

**Infraestrutura & DevOps**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/VPS%20Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![nginx](https://img.shields.io/badge/nginx-009639?style=flat-square&logo=nginx&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-2088FF?style=flat-square&logo=github-actions&logoColor=white)

**Dados**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

---

## Experiência

**Estagiário em Desenvolvimento e Automação** · `Atual`  
**F5 Tecnologia** · Remoto · *Mai 2026 – Presente*  
Agentes de IA para venda de produtos digitais (empréstimos, internet, TV a cabo) com tráfego de dados sensíveis conforme LGPD. Integração com WhatsApp Business API e CRMs via webhooks, monitoramento de infraestrutura e retry patterns. → [Caso de estudo acima](#-caso-de-estudo--plataforma-autônoma-de-conversão-de-leads)

**Estagiário em Automação de Processos e Analista de Suporte RPA**  
**NEURODEV** · *2025*  
15+ integrações em Python conectando APIs externas (800+ transações/dia). Otimizei pipeline com OpenAI API de **15min → 27s (−97%)** via engenharia de prompt e cache inteligente. Refatorei RPA em Python com Docker: downtime de **35h → 2,25h/mês (−93,5%)**.

**Desenvolvedor Júnior de Automação de Processos com IA**  
**BNECT** · *2025*  
Serviços em Python integrando CRM/ERP via APIs, com padrões Factory e Strategy em arquitetura orientada a eventos. Orquestração de fluxos com LLMs via n8n e Python.

**Analista de Requisitos de Software**  
**Volpatto Engenharia e Arquitetura** · Freelance · *Ago – Set 2023*  
Requisitos funcionais e não funcionais em UML/BPMN para 6 serviços, com foco em performance e manutenibilidade.

---

## Formação

| | Curso | Instituição | Período |
|---|---|---|---|
| 🎓 | Engenharia de Software · CR 9,3/10 | Universidade Estácio de Sá | 2023 – Dez 2026 |
| 🎓 | Técnico em Desenvolvimento de Software · CR 8,0/10 | SENAI Juiz de Fora | Concluído 2023 |

**Concluídos:** Python Avançado + IA Generativa (Udemy) · Especialista em Inteligência Artificial (Academia de IA) · Programação de Sistemas de Informação (Estácio) · Programação Web (Estácio) · Direito e Privacidade dos Usuários (Estácio)

**Em andamento (2025–2026):** AWS Cloud Practitioner · Azure Fundamentals · IA & Machine Learning (Udemy) · FastAPI Avançado + TDD + PostgreSQL (Udemy) · Power Apps + Power Automate + SharePoint (Udemy)

---

## Atualmente

- 🔨 Evoluindo o **IAprovale** — cliente web e expansão da camada MCP
- 🎧 Construindo o **VoxAI** — transcrição 100% offline com Whisper on-device; roadmap inclui LLM local via LLamaSharp (Phi-3/Llama 3B) para resumir transcrições sem nuvem
- 📚 Estudando **FastAPI Avançado + TDD** e **AWS Cloud Practitioner**
- 🤖 Explorando arquiteturas **multi-agente** e **LLMOps em produção**

---

<div align="center">

*Aberto a desafios técnicos e projetos de alto impacto.*

📧 jonasaugustoprofissional@gmail.com · 📍 Juiz de Fora, MG · 🌐 [jonasaaugusto.github.io](https://jonasaaugusto.github.io)

</div>
