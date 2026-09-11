---
name: markitdown-document-intelligence
description: Orienta a conversão de DOCX, PPTX, XLSX, XLS, PDF, CSV, HTML, JSON, XML, MSG, imagens e áudio para Markdown com MarkItDown; valida cobertura, estrutura, tabelas, números, rastreabilidade e confidencialidade; acrescenta metadados e prepara conteúdo para GitHub, Notion, RAG, NotebookLM, agentes e análise. Usar em pedidos como "converte este relatório", "valida o Markdown extraído" ou "prepara estes documentos para RAG". Não usar para preservar fielmente layout visual, editar o ficheiro original, executar OCR/cloud sem autorização, nem analisar conclusões antes de validar a extração.
---

# MarkItDown Document Intelligence

## Objetivo

Transformar documentos de trabalho em Markdown pesquisável, rastreável e adequado a IA, orientando a conversão com MarkItDown e aplicando controlo de qualidade antes de qualquer análise substantiva.

## Quando usar

- Converter formatos suportados pelo MarkItDown para Markdown.
- Preparar documentos para GitHub, Notion, bases de conhecimento, RAG, NotebookLM ou agentes.
- Consolidar investigação, entrevistas, relatórios, apresentações, benchmarks ou tabelas.
- Rever, limpar, classificar e enriquecer Markdown já convertido.
- Identificar necessidade de OCR, extração visual ou revisão humana.
- Estruturar informação de FMCG, consumer insights, tendências, marcas, claims, preços ou segmentos.

## Quando não usar

- Para prometer preservação fiel de design, paginação, tipografia, animações ou elementos decorativos.
- Para editar diretamente o documento original ou reconstruir o seu layout.
- Para inventar texto, números, tabelas, fontes ou metadados ausentes.
- Para enviar conteúdo confidencial a serviços externos sem autorização explícita.
- Para produzir conclusões de alto impacto antes de validar a extração contra a fonte.
- Para ficheiros não suportados sem confirmar um conversor, plugin ou método alternativo real.

## Inputs esperados

Recolher ou inferir, sem bloquear desnecessariamente:

- ficheiro, conjunto de ficheiros, excerto ou Markdown convertido;
- objetivo: arquivo, pesquisa, RAG, resumo, benchmark, tabelas, briefing ou análise;
- origem e nível de confidencialidade;
- formato, incluindo se um PDF é digital ou digitalizado;
- presença de tabelas, gráficos, imagens, diagramas, fórmulas, notas ou áudio;
- destino e preferência por processo manual, em lote ou integrado.

Se faltarem dados que mudem o método, fazer até três perguntas objetivas. Caso contrário, avançar com pressupostos explícitos.

## Workflow

1. **Inspecionar antes de recomendar.** Ler os ficheiros ou excertos disponíveis. Inventariar formato, origem, data, dimensão, confidencialidade, duplicados e elementos visuais.
2. **Classificar a complexidade.** Distinguir documento digital simples, layout complexo, scan/imagem, dados tabulares, áudio e dados estruturados. Registar o que pode perder significado na conversão.
3. **Escolher o método.** Preferir conversão local e o conjunto mínimo de extras. Consultar [references/markitdown-playbook.md](references/markitdown-playbook.md) para instalação, comandos, API e riscos por formato. Confirmar suporte na versão instalada com `markitdown --help` quando houver dúvida.
4. **Proteger os dados.** Não usar OCR cloud, modelos externos, URIs remotos ou APIs sem autorização explícita quando existirem dados pessoais, internos, confidenciais ou restritos. Sanitizar inputs não confiáveis e limitar o acesso a ficheiros/URIs.
5. **Converter.** Usar caminhos entre aspas, manter o original e guardar a saída separadamente. Não afirmar que a conversão preserva o design. Em integração Python local, preferir `convert_local()` ao método permissivo `convert()`.
6. **Validar contra a fonte.** Comparar cobertura, ordem de leitura, hierarquia, tabelas, números, unidades, datas, citações, notas e conteúdo visual. Classificar cada falha como crítica, alta, média ou baixa.
7. **Normalizar sem alterar significado.** Corrigir títulos, listas, espaços, datas e tabelas apenas quando verificável. Marcar estrutura inferida e lacunas; não preencher conteúdo ausente.
8. **Adicionar metadados e rastreabilidade.** Aplicar o esquema de [references/qa-metadata.md](references/qa-metadata.md) quando o destino for arquivo, pesquisa, RAG ou base de conhecimento. Omitir campos desconhecidos ou assinalá-los como não identificados, sem adivinhar.
9. **Preparar para o destino.** Organizar ficheiros, naming conventions e secções. Para RAG, criar chunks semanticamente coerentes sem separar cabeçalhos das respetivas tabelas, citações, definições ou conclusões.
10. **Analisar só depois do QA.** Produzir sínteses, comparações, insights ou briefings apenas quando o nível de qualidade for adequado. Separar factos, interpretações, hipóteses e recomendações.
11. **Fechar com validação humana.** Exigir revisão da fonte para números, preços, percentagens, claims regulados, citações, ingredientes, valores nutricionais e conclusões de alto impacto.

## Formato de output

Adaptar a extensão, mantendo esta ordem:

1. **Diagnóstico rápido**: formato, objetivo, confidencialidade, complexidade e pressupostos.
2. **Abordagem recomendada**: método local/cloud, dependências e justificação.
3. **Comandos ou instruções práticas**: comandos completos com caminhos entre aspas ou placeholders declarados.
4. **Limitações e riscos**: conteúdo visual, OCR, tabelas, fórmulas e rastreabilidade.
5. **Relatório de QA**: tabela com `Área | Estado | Severidade | Evidência | Ação recomendada`.
6. **Entregáveis preparados**: Markdown normalizado, metadados, classificação, naming e/ou chunks, conforme pedido.
7. **Próximo passo**: ação concreta de validação ou utilização.

Quando o utilizador pedir apenas um comando, responder de forma breve e acrescentar uma nota de validação se houver risco de tabelas, scans, imagens ou conteúdo sensível.

## Regras de qualidade

- Preservar significado e rastreabilidade acima da aparência.
- Distinguir texto extraído, estrutura inferida, conteúdo visual não extraído e itens a validar.
- Associar cada problema de QA a evidência observável e a uma ação.
- Não declarar `validated` sem comparação suficiente com o original.
- Não fragmentar uma tabela sem repetir o cabeçalho e a referência à fonte.
- Manter original e Markdown lado a lado quando o destino exigir auditabilidade.
- Usar `scripts/validate_markdown.py` como pré-verificação estrutural; explicar que não substitui comparação visual/humana.
- Consultar os guias em `references/` apenas quando a etapa correspondente for necessária.

## Gestão de incerteza

- Declarar pressupostos quando faltarem formato, destino, confidencialidade ou características do documento.
- Usar `não identificado`, `desconhecida` ou campo vazio apenas quando apropriado; nunca inferir factos sem base.
- Se o texto estiver ilegível ou a ordem for ambígua, parar a análise substantiva e recomendar nova extração ou revisão.
- Se uma capacidade variar por versão, pedir a versão instalada ou indicar como verificar localmente.
- Apresentar OCR e interpretação visual com nível de confiança e itens de verificação.

## Limites e segurança

- Nunca expor credenciais, tokens, dados pessoais ou conteúdo restrito.
- Nunca presumir acesso a APIs, endpoints, conectores ou plugins.
- Pedir autorização antes de enviar conteúdo para cloud, OCR externo ou modelos multimodais.
- Preferir o método local mais restrito para documentos confidenciais.
- Tratar ficheiros e URIs não confiáveis como inputs potencialmente perigosos; restringir paths e destinos de rede.
- Não dar garantias de exatidão para OCR, tabelas complexas, gráficos, diagramas, fórmulas ou layout.
- Não substituir revisão jurídica, regulatória, científica ou financeira especializada.

## Referências e recursos

- [references/markitdown-playbook.md](references/markitdown-playbook.md): instalação, conversão, escolha por formato e resolução de problemas.
- [references/qa-metadata.md](references/qa-metadata.md): checklist, severidades, frontmatter, organização, RAG e estruturas FMCG.
- `scripts/validate_markdown.py`: verificação local e determinística de estrutura e metadados.
