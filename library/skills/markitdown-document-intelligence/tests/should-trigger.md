# Casos em que deve ativar

## Caso 1: PDF para RAG

- **Prompt:** `Converte este relatório PDF interno para Markdown e prepara-o para RAG, preservando referências às páginas.`
- **Ativação esperada:** Sim.
- **Comportamento esperado:** Inspecionar o PDF, confirmar se é digital ou scan, propor conversão local, avaliar confidencialidade, converter, executar QA, acrescentar metadados e preparar chunks rastreáveis.
- **Critérios de qualidade:** Não usar cloud sem autorização; identificar conteúdo visual; validar números e tabelas; manter ligação ao original.

## Caso 2: QA de apresentação

- **Prompt:** `Revê este Markdown extraído de um PPTX e diz-me se há informação em gráficos ou notas que se perdeu.`
- **Ativação esperada:** Sim.
- **Comportamento esperado:** Comparar Markdown e apresentação, verificar ordem de slides, notas, imagens, gráficos e hierarquia, e produzir tabela de QA por severidade.
- **Critérios de qualidade:** Associar achados a slides; separar conteúdo extraído de conteúdo visual; não inventar texto ausente.

## Caso 3: Normalização de Excel

- **Prompt:** `Preciso de transformar estes XLSX de benchmark de preços numa base Markdown pesquisável para análise FMCG.`
- **Ativação esperada:** Sim.
- **Comportamento esperado:** Inventariar folhas e tabelas, recomendar o extra `xlsx`, verificar células fundidas, fórmulas e unidades, normalizar tabelas e aplicar metadata/naming.
- **Critérios de qualidade:** Preservar cabeçalhos, moedas, unidades e fontes; assinalar pivots/gráficos; exigir verificação de preços.

## Caso 4: Conversão simples por comando

- **Prompt:** `Dá-me o comando PowerShell para converter o ficheiro C:\Projetos\Entrevista 04.docx para Markdown.`
- **Ativação esperada:** Sim.
- **Comportamento esperado:** Fornecer comando curto com caminhos entre aspas e uma nota de validação proporcional ao risco.
- **Critérios de qualidade:** Não alterar o path; não introduzir cloud; sintaxe clara e executável.
