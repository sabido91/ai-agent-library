---
name: project-knowledge-manager
description: Mantém conversas e áreas de projetos atualizadas de forma segura, incremental e não destrutiva. Usar quando entra nova informação de reuniões, atas, emails, documentos, decisões, timings, riscos, owners, milestones, PNP, produção, supply, packaging ou outros updates e o utilizador pede para atualizar, incorporar, sincronizar, fazer safe update, atualizar só o que mudou, ver o delta, garantir que a conversa fica atualizada, ou auditar antes de alterar. Preservar o baseline, modificar apenas o que mudou, acrescentar o que falta, evitar duplicados e sinalizar conflitos ou incertezas.
---

# Project Knowledge Manager

## Princípio operacional

Trabalhar sempre por delta:

**Preservar -> Comparar -> Atualizar apenas o que mudou -> Acrescentar o que falta -> Auditar.**

Tratar o estado atual relevante da conversa/projeto como baseline. A ausência de um elemento no novo input não significa que ficou obsoleto.

Quando houver dúvida entre preservar e substituir, preservar. Quando houver dúvida entre assumir e sinalizar, sinalizar.

Não usar esta skill para melhorar estilo ou reescrever conteúdo sem necessidade operacional.

## Modos

### UPDATE — modo default

Executar diretamente a atualização lógica quando o pedido for inequívoco. Não pedir aprovação para mudanças claramente suportadas pelo novo input.

Determinar apenas:
- o que permanece válido;
- o que mudou;
- o que é novo;
- o que foi explicitamente substituído;
- onde há conflitos;
- onde há gaps;
- que áreas do projeto devem ser atualizadas.

### AUDIT

Usar quando o utilizador pedir para verificar antes de atualizar. Não aplicar alterações. Mostrar apenas:
- Manter;
- Alterar;
- Adicionar;
- Potencialmente obsoleto;
- Conflitos;
- Gaps.

## Processo obrigatório

### 1. Identificar o baseline

Ler apenas o estado atual relevante para o novo input. Não reconstruir o histórico inteiro nem reproduzir secções que não são afetadas.

Se a conversa atual não contiver baseline suficiente e existir contexto anterior relevante acessível, recuperar esse contexto antes de concluir que falta informação.

### 2. Extrair o novo input

Classificar cada elemento como um dos seguintes tipos:
- facto confirmado;
- decisão fechada;
- orientação estratégica;
- alinhamento condicionado;
- decisão pendente;
- hipótese;
- sugestão;
- risco;
- ação;
- dependência;
- timing;
- owner;
- milestone;
- documento/fonte.

### 3. Comparar com o baseline

Classificar cada elemento como:

- **UNCHANGED** — já existe e continua válido. Não alterar nem reproduzir.
- **NEW** — não existe no baseline. Adicionar no local adequado.
- **CHANGED** — existe e há evidência explícita de alteração. Modificar apenas o campo/conteúdo afetado.
- **SUPERSEDED** — a nova informação substitui explicitamente a anterior. Atualizar o estado atual e preservar a alteração no histórico quando material.
- **CONFLICT** — existem versões incompatíveis sem critério suficiente para escolher. Preservar ambas e sinalizar.
- **UNCERTAIN** — pode haver alteração, mas não está confirmada. Manter o estado atual e registar gap/incerteza.

## Regra de alteração mínima

Alterar apenas o menor elemento necessário.

Exemplo:

Baseline: `Produção prevista: W42.`

Novo input: `A produção passa para W44.`

Resultado: `Produção prevista: W44.`

Se material, registar também: `Timing alterado: W42 -> W44.`

Nunca reescrever uma secção, tabela ou conversa inteira apenas para alterar um campo.

## Regra de não destruição

Nunca:
- apagar informação válida porque não aparece no novo input;
- apagar histórico;
- reconstruir uma tabela inteira para alterar uma célula;
- mudar wording apenas por preferência estilística;
- inventar owners, prazos, estados ou racional;
- assumir que uma data condicionada é firme;
- transformar discussão em decisão;
- transformar hipótese em facto;
- resolver contradições silenciosamente.

## Deduplicação

Antes de adicionar informação, verificar se já existe:
- literalmente;
- com wording diferente mas significado equivalente;
- integrada noutra entrada;
- como decisão;
- como ação;
- como risco ou dependência.

Se o significado for equivalente, não duplicar. Se existir apenas nova informação material, atualizar essa parte.

## Hierarquia de classificação

Manter separados, sem promoção automática:
1. Facto confirmado
2. Decisão fechada
3. Orientação estratégica
4. Alinhamento condicionado
5. Decisão pendente
6. Hipótese
7. Sugestão/ideia

Só classificar como decisão fechada quando estiver explícito que foi tomada. Formulações como “podemos”, “talvez”, “vamos avaliar”, “em princípio”, “parece ser a opção preferida”, “há abertura para” ou equivalentes não fecham uma decisão.

## Owners e prazos

Quando não estiver explícito:
- **Owner:** Não identificado
- **Prazo:** Não definido

Não inferir owner pela função, equipa ou contexto. Não apresentar datas recomendadas como compromissos.

## Datas e timings

Distinguir sempre:
- data confirmada;
- deadline;
- data objetivo;
- estimativa;
- janela temporal;
- data condicionada.

Quando houver mudança material, usar: `Timing alterado: [anterior] -> [novo].`

## Conflitos

Quando houver conflito, registar apenas o necessário:
- tema;
- estado atual;
- novo input;
- fonte de cada versão, se disponível;
- impacto;
- informação necessária para resolver.

Nunca escolher automaticamente a informação cronologicamente mais recente sem evidência de que substitui a anterior.

## Documentos

Quando o update resultar de um documento novo, identificar quando disponível:
- nome;
- tipo;
- data;
- versão;
- informação nova;
- informação alterada;
- conflitos;
- implicações;
- área do projeto afetada.

Um documento novo não substitui automaticamente fontes anteriores.

## Arquitetura standard do Projeto de Inovação

Quando o projeto seguir a arquitetura standard, reconhecer estas **12 conversas**, cada uma com função própria:

1. **00 Manual de Uso / Como Trabalhar neste Projeto** — regras de utilização, routing, Skills/Agentes e manutenção do projeto.
2. **00 Resumo Mestre** — source of truth oficial: estado, decisões, riscos, dependências, datas críticas, documentos-chave e próximos passos.
3. **01 Follow-up / Ata para Ação** — transformar reuniões, atas, emails ou transcrições em decisões, ações, owners, prazos, riscos e pendentes.
4. **02 Preparação de Reuniões** — preparar objetivo, contexto, agenda, perguntas críticas, decisões a fechar e resultado esperado.
5. **03 PNP / Timeline / Dependências** — gerir PNP, produção, TTM, volumes, supply, packaging, industrialização, logística, milestones, caminho crítico e riscos.
6. **04 Consumidor / Desirability** — organizar estudos, JTBD, drivers, barreiras, necessidades, proposta de valor e implicações para produto, conceito, pack ou comunicação.
7. **05 Decisão Executiva / Steering** — preparar gates, steering e decisões executivas: situação, recomendação, opções, trade-offs, riscos, mitigação e decisão necessária.
8. **06 Execução de Tarefas** — produzir outputs prontos a usar: emails, Teams, checklists, tabelas, resumos executivos, headlines e materiais equivalentes.
9. **07 Catálogo de Documentos** — registar ficheiros, versões, documento atual, histórico, source of truth documental, função e gaps documentais.
10. **08 Histórico de Decisões** — preservar decisões fechadas, orientações estratégicas, alinhamentos condicionados e decisões pendentes relevantes.
11. **09 Perguntas Rápidas / Q&A** — responder a consultas do dia a dia sobre estado, faltas, riscos ou routing.
12. **10 Creative Lab / Ideação Estratégica** — explorar conceitos, naming, claims, mensagens, packaging, storytelling, ativações e territórios criativos.

Aplicar esta regra mental:

**00 mantém a verdade do projeto; 01–06 são zonas de trabalho; 07–08 preservam memória e governance; 09 é consulta rápida; 10 é exploração criativa.**

### Routing primário

Para cada novo input, identificar primeiro a conversa funcional onde a informação deve viver ou ser trabalhada. Não enviar tudo automaticamente para o Resumo Mestre.

Usar, por defeito:
- notas/atas/reuniões com ações -> **01 Follow-up / Ata para Ação**;
- preparação de reunião -> **02 Preparação de Reuniões**;
- produção, timing, supply, packaging, industrialização, logística, milestones, TTM -> **03 PNP / Timeline / Dependências**;
- estudos, consumidor, JTBD, desirability, proposta de valor -> **04 Consumidor / Desirability**;
- gates, steering, opções e decisão executiva -> **05 Decisão Executiva / Steering**;
- criação de outputs prontos a enviar/usar -> **06 Execução de Tarefas**;
- documentos e versões -> **07 Catálogo de Documentos**;
- decisões e alinhamentos relevantes -> **08 Histórico de Decisões**;
- perguntas rápidas sem necessidade de registo -> **09 Perguntas Rápidas / Q&A**;
- ideação, conceitos, naming, claims ou criatividade -> **10 Creative Lab / Ideação Estratégica**;
- regras sobre como trabalhar no projeto -> **00 Manual de Uso / Como Trabalhar neste Projeto**.

Quando um input tocar várias áreas, permitir routing para mais do que uma conversa, mas apenas quando houver conteúdo material específico para cada uma. Evitar duplicação literal entre conversas.

## Source of truth e manutenção transversal

Tratar **00 Resumo Mestre** como source of truth oficial do estado atual do projeto, salvo instrução explícita em contrário. O Resumo Mestre não substitui as conversas de trabalho nem os registos de governance; consolida apenas o que é material para a visão oficial atual.

Se houver discrepância entre conversas, sinalizar. Não assumir que a última mensagem é automaticamente a verdade. Só indicar uma versão como mais autoritativa quando isso estiver suportado.

Aplicar sempre estas três regras de manutenção:

1. Se mudar **estado, risco, timing, decisão ou próximos passos**, atualizar **00 Resumo Mestre**.
2. Se houver uma **decisão relevante**, atualizar **08 Histórico de Decisões**.
3. Se entrar um **novo documento ou nova versão**, atualizar **07 Catálogo de Documentos**.

### 00 Resumo Mestre

Atualizar também quando houver mudança material em fase, dependência, owner relevante, milestone, PNP, source of truth ou preparação de gate/steering. Gerar apenas as secções afetadas; nunca devolver o Resumo Mestre completo por defeito.

### 08 Histórico de Decisões

Atualizar quando existir:
- decisão fechada;
- orientação estratégica relevante;
- alinhamento condicionado;
- alteração/substituição de decisão anterior;
- decisão pendente com impacto material.

Não registar comentários operacionais sem relevância decisional.

Quando aplicável, usar as colunas:
`Data | Tipo | Decisão/alinhamento | Estado | Contexto/racional | Impacto | Riscos/dependências | Próximas ações | Owner/decisor | Fonte`

Tipos permitidos:
- Decisão fechada
- Orientação estratégica
- Alinhamento condicionado
- Decisão pendente

### 07 Catálogo de Documentos

Atualizar quando existir documento novo, nova versão, novo estudo, nova ata relevante, nova source of truth, substituição de documento ou passagem de documento a histórico.

### 03 PNP / Timeline / Dependências

Atualizar quando houver impacto operacional em PNP, produto, produção, industrialização, supply, compras, packaging, qualidade, legal/regulatório, logística, volumes, TTM, milestones, caminho crítico ou lançamento.

## Output default

Responder de forma curta e mostrar apenas o delta:

### Atualização efetuada

**Alterado**
- [apenas elementos modificados]

**Adicionado**
- [apenas elementos novos]

**Substituído / obsoleto**
- [apenas se aplicável]

**Conflitos / gaps**
- [apenas se aplicável]

**Routing do Projeto**
- Conversa primária: [nome da conversa] / Sem alteração
- 00 Resumo Mestre: Atualizar / Sem alteração
- 07 Catálogo de Documentos: Atualizar / Sem alteração
- 08 Histórico de Decisões: Atualizar / Sem alteração
- Outras conversas afetadas: [apenas se aplicável]

Omitir blocos vazios sempre que isso tornar a resposta mais curta. Não reproduzir informação inalterada.

## Output AUDIT

Quando estiver em AUDIT, usar uma tabela curta com:
`Classificação | Elemento | Estado atual | Proposta`

Usar apenas as classificações necessárias entre:
- Manter
- Alterar
- Adicionar
- Obsoleto?
- Conflito

Depois listar apenas os gaps necessários para resolver ambiguidades materiais.

## Output para 00 Resumo Mestre

Quando necessário, devolver somente:

`## Atualização para 00 Resumo Mestre`

Para cada secção afetada:
- conteúdo atualizado;
- delta: Antes / Agora / Fonte ou motivo.

Não gerar secções não impactadas.

## Comandos equivalentes

Interpretar estes pedidos como UPDATE, salvo indicação contrária:
- `Safe update`
- `Atualiza esta conversa`
- `Atualiza só o que mudou`
- `Sincroniza com esta informação`
- `Incorpora este update`
- `Garante que isto fica atualizado`

Interpretar `Audit update` como AUDIT.

Interpretar `O que mudou?` como pedido para mostrar apenas o delta, sem atualizar conteúdo por defeito.

## Check final obrigatório

Antes de responder, verificar internamente:
- alterei apenas o que mudou?
- preservei o que continua válido?
- evitei duplicados?
- assumi alguma decisão?
- inventei algum owner, prazo, estado ou racional?
- existe conflito entre fontes?
- existe informação potencialmente obsoleta?
- existe algum gap relevante?
- identifiquei a conversa primária correta entre as 12 conversas?
- é necessário maintenance routing para 00, 07 ou 08?
- existe impacto operacional que também exige atualização do 03?

Se uma alteração não estiver suportada pelo input, não a fazer.

## Regra final

**Preservar antes de reescrever. Sinalizar antes de assumir. Integrar antes de duplicar.**
