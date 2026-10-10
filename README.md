<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="Jonas Augusto, Backend, Automação e Agentes de IA">
</picture>

Desenvolvedor backend focado em automação inteligente e agentes de IA.

## Sobre

Trabalho com backend e agentes de IA com LLMs (OpenAI, Anthropic, DeepSeek), integrando APIs complexas e otimizando latência crítica.
Meu foco é confiabilidade em produção: retry patterns, fallback, monitoramento e observabilidade.
Engenharia de Software na Estácio (CR 9,3, formatura em dez/2026) · inglês C1.

[Portfólio](https://jonasaaugusto.github.io) · [LinkedIn](https://www.linkedin.com/in/jonasaaugusto) · [Currículo (PDF)](https://jonasaaugusto.github.io/JonasAugusto_cv_m.pdf) · [E-mail](mailto:jonasaugustoprofissional@gmail.com) · Augustus AI Solutions <!-- TODO: link -->

## Em produção

**97%** menos latência (15 min → 27 s) · **93,5%** menos downtime · **99,97%** de uptime · **170+** clientes recuperados

## Caso de estudo · F5 Tecnologia

Plataforma autônoma de conversão de leads com IA, em produção 24/7. Recebe leads pelo WhatsApp, conduz o atendimento com um agente de IA, coleta dados, gera propostas com um parceiro financeiro e cadastra clientes em programas do setor de energia. Atuei de ponta a ponta: arquitetura, agente, integrações e confiabilidade.

- Agente de IA com fallback, prompts por etapa, contexto isolado por lead e guardrails anti-alucinação.
- Pipeline de OCR para documentos e máquina de estados de 9 etapas com persistência por lead.
- Arquitetura distribuída: automação de navegador (Playwright) isolada do agente e da orquestração.
- Servidor MCP criado do zero: o funil vira ferramentas que o agente chama no próprio turno, e a finalização só executa com confirmação explícita validada no código.

[Ver o caso completo no portfólio](https://jonasaaugusto.github.io/#experiencia)

## Projetos

- [IAprovale](https://github.com/JonasaAugusto/IAprovale): buscador de concursos com IA; traduz a busca em linguagem natural via DeepSeek e consulta a fonte oficial por MCP. `Python` `FastAPI` `DeepSeek` `MCP` `PostgreSQL`
- [LogiTrack API](https://github.com/JonasaAugusto/logitrackAPI): API RESTful de logística com rastreamento em tempo real, relatórios assíncronos e JWT. `Python` `FastAPI` `PostgreSQL` `Docker` `JWT`
- [NotaME](https://github.com/JonasaAugusto/NotaME): app mobile/desktop para recibos em PDF, NFS-e e gestão de clientes; offline-first com sincronização P2P e AES-256. `C#` `.NET MAUI` `SQLite` `QuestPDF`
- [Fabula Coop](https://github.com/JonasaAugusto/FabulaCoop): RPG de texto cooperativo em tempo real em que uma IA atua como mestre da campanha. `Python` `LLM` `Agent` `Realtime`
- [Pocket Infra](https://github.com/JonasaAugusto/pocket-infra): liga um PC Windows remotamente (Wake-on-LAN) e inicia sessões de Claude Code via adesivo NFC. `Wake-on-LAN` `Tailscale` `iOS Shortcuts` `NFC`
- VoxAI (privado): transcrição offline de áudio e vídeo com Whisper on-device, sem custo de servidor. `C#` `.NET MAUI` `Whisper` `FFmpeg` `SQLite`

**Freelance e Augustus AI Solutions:** agente de IA no WhatsApp (DuTony Hotburguers) e landing pages (Monobloco, Dário Fretes).

## Stack

- **IA:** `OpenAI API` `Anthropic Claude` `DeepSeek` `LangChain` `MCP` `Whisper`
- **Backend:** `Python` `FastAPI` `C#` `Playwright` `n8n` `Webhooks`
- **Infra:** `Docker` `Docker Compose` `Linux` `systemd` `nginx` `Git` `CI/CD`
- **Dados:** `PostgreSQL` `Supabase` `Redis` `SQLite` `MySQL`
- **Front:** `HTML5` `CSS3` `JavaScript` `React` `Tailwind CSS`

## Experiência

- Estagiário em Desenvolvimento e Automação · F5 Tecnologia · mai/2026 – atual. Agentes de IA para venda de produtos digitais (crédito e energia), com dados sensíveis conforme a LGPD.
- Estagiário de Automação de Processos e Suporte RPA · NeuroDev · set–nov/2025
- Desenvolvedor Júnior de Automação de Processos com IA · BNECT · ago–set/2025
- Analista de Requisitos de Software · Volpatto Engenharia e Arquitetura (freelance) · ago–set/2023

## Formação

- Engenharia de Software · Universidade Estácio de Sá · 2023 – dez/2026 · CR 9,3
- Técnico em Desenvolvimento de Software · SENAI Juiz de Fora · concluído em 2023 · CR 8,0

## Atualmente

- Evoluindo o IAprovale: cliente web e expansão da camada MCP.
- Construindo o VoxAI: transcrição 100% offline com Whisper on-device.
- Estudando FastAPI Avançado + TDD e AWS Cloud Practitioner.

---

Juiz de Fora, MG · [jonasaugustoprofissional@gmail.com](mailto:jonasaugustoprofissional@gmail.com)

*Backend developer focused on AI agents and automation. Portfolio and case study in English at [jonasaaugusto.github.io](https://jonasaaugusto.github.io).*
