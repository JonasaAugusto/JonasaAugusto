<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" alt="Jonas Augusto, Backend, Automação e Agentes de IA">
</picture>

<div align="center">

**Fundador da Augustus AI Solutions · Agentes de IA, Automação e Web B2B**

[Portfólio](https://jonasaaugusto.github.io) · [LinkedIn](https://www.linkedin.com/in/jonasaaugusto) · [Currículo (PDF)](https://jonasaaugusto.github.io/JonasAugusto_cv_m.pdf) · [E-mail](mailto:jonasaugustoprofissional@gmail.com) · Augustus AI Solutions

</div>

## Sobre

Sou fundador da **Augustus AI Solutions**, onde atuo como CEO e desenvolvedor principal desde jun/2026, de forma remota. A empresa constrói agentes de IA, automações e soluções web para negócios (B2B).
Tenho pouco mais de 1 ano de experiência profissional, e hoje entrego bots de atendimento e vendas no WhatsApp e as ferramentas internas que os sustentam.
Engenharia de Software na Estácio (CR 9,3, formatura em dez/2026) · inglês C1.

## Projetos profissionais

| Projeto | O que faz | Stack |
| :-- | :-- | :-- |
| **Raízes & Escamas** (cliente) | Bot de atendimento e vendas no WhatsApp para uma loja de aquarismo: RAG com 430 entradas, cadastro em lote pelo grupo do dono (texto, áudio e foto), guarda de quantidades no orçamento, PIX e pós-venda com triagem. Roda como serviço na VPS própria. | `TypeScript` `Baileys` `DeepSeek` `RAG` `systemd` |
| **F5 Tecnologia** (caso abaixo) | Plataforma autônoma de conversão de leads com IA pelo WhatsApp. | `MCP` `Playwright` `WhatsApp` |

## Caso de estudo · F5 Tecnologia

> [!NOTE]
> Plataforma autônoma de conversão de leads com IA, em produção 24/7. Recebe leads pelo WhatsApp, conduz o atendimento com um agente de IA, coleta dados, gera propostas com um parceiro financeiro e cadastra clientes em programas do setor de energia. Atuei de ponta a ponta: arquitetura, agente, integrações e confiabilidade.

- Agente de IA com fallback, prompts por etapa, contexto isolado por lead e guardrails anti-alucinação.
- Pipeline de OCR para documentos e máquina de estados de 9 etapas com persistência por lead.
- Arquitetura distribuída: automação de navegador (Playwright) isolada do agente e da orquestração.
- Servidor MCP criado do zero: o funil vira ferramentas que o agente chama no próprio turno, e a finalização só executa com confirmação explícita validada no código.

[Ver o caso completo no portfólio →](https://jonasaaugusto.github.io/#experiencia)

## Projeto principal

**AugustusApp** · app interno da empresa (repositório privado). Reúne em um só lugar:

- transcrição local de reuniões com WhisperX large-v3 e diarização, com resumo por LLM local (Ollama);
- terminal SSH interno da VPS;
- conector de WhatsApp modular e gestão dos bots na VPS;
- administração de backup da VPS com restic para o Backblaze B2;
- publicação versionada do app.

`C#` `.NET 10` `MAUI` `CommunityToolkit.Mvvm` `Python` `WhisperX` `Ollama` `SSH.NET` `xterm.js`

## Mais projetos

| Projeto | O que faz | Stack |
| :-- | :-- | :-- |
| [**IAprovale**](https://github.com/JonasaAugusto/IAprovale) | Buscador de concursos com IA: traduz a busca em linguagem natural via DeepSeek e consulta a fonte oficial por MCP. | `Python` `FastAPI` `DeepSeek` `MCP` |
| [**Conector WhatsApp modular**](https://github.com/JonasaAugusto/whatsappmoduleconnector) · Produto B2B | Serviço que conecta e desconecta bots de WhatsApp por QR Code, cada bot de forma independente. Construído em vez de usar o OpenClaw, que gera rastro de automação para a Meta. | `Python` `FastAPI` `Baileys` |

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img src="assets/stack-light.svg" alt="Stack. App: C#, .NET 10, MAUI, CommunityToolkit.Mvvm, SSH.NET, xterm.js. IA: WhisperX, pyannote, Ollama, DeepSeek, RAG, MCP. Backend: Python, FastAPI, TypeScript, Node.js, Baileys. Dados: PostgreSQL, SQLite. Infra: Linux, systemd, restic, Backblaze B2, SSH">
</picture>

## Linguagens

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/langs-dark.svg">
  <img src="assets/langs-light.svg" alt="Linguagens mais usadas nos meus repositórios, públicos e privados: Python 51,9%, C# 16,7%, TypeScript 11,9%, JavaScript 8,0%, HTML 6,3% e outras 5,3%">
</picture>

<sub>Soma dos bytes de código dos meus repositórios, públicos e privados.</sub>

## Experiência

| Período | Cargo · Empresa |
| :-- | :-- |
| jun/2026 – atual | **Fundador, CEO e Desenvolvedor Principal** · Augustus AI Solutions (remoto). Agentes de IA, automação e web B2B. |
| mai/2026 – atual | **Estagiário em Desenvolvimento e Automação** · F5 Tecnologia. Agentes de IA para venda de produtos digitais (crédito e energia), com dados sensíveis conforme a LGPD. |
| set–nov/2025 | **Estagiário de Automação de Processos e Suporte RPA** · NeuroDev |
| ago–set/2025 | **Desenvolvedor Júnior de Automação de Processos com IA** · BNECT |
| ago–set/2023 | **Analista de Requisitos de Software** · Volpatto Engenharia e Arquitetura (freelance) |

## Formação

- **Engenharia de Software** · Universidade Estácio de Sá · 2023 – dez/2026 · CR 9,3
- **Técnico em Desenvolvimento de Software** · SENAI Juiz de Fora · concluído em 2023 · CR 8,0

## Atualmente

- Evoluindo o AugustusApp e os bots de WhatsApp em produção na VPS.
- Mantendo o IAprovale e o Conector WhatsApp modular.

---

<div align="center">

Juiz de Fora, MG · [jonasaugustoprofissional@gmail.com](mailto:jonasaugustoprofissional@gmail.com)

*Founder of Augustus AI Solutions, building AI agents, automation and B2B web. Portfolio and case study in English at [jonasaaugusto.github.io](https://jonasaaugusto.github.io).*

</div>
