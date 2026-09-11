# QA, metadados e preparação para IA

Consultar este ficheiro depois da conversão ou quando o destino for uma biblioteca documental, RAG, agentes ou análise.

## Checklist de controlo de qualidade

| Área | Pergunta de validação |
|---|---|
| Cobertura | Todo o conteúdo relevante foi extraído? |
| Estrutura | Títulos, secções e listas mantêm uma hierarquia lógica? |
| Ordem de leitura | O texto segue uma sequência compreensível? |
| Tabelas | Colunas, linhas, unidades e cabeçalhos foram preservados? |
| Números | Preços, percentagens, datas, quantidades e unidades estão corretos? |
| Fontes | Origem, data, autor e referência estão registados? |
| Visual | Existe informação crítica em gráficos, imagens ou diagramas? |
| Rastreabilidade | É possível localizar página, slide, folha ou secção de origem? |
| Confidencialidade | Método e destino respeitam o nível de sigilo? |

Classificar falhas como:

- **Crítica:** altera conclusões, números, decisões, compliance ou significado.
- **Alta:** reduz substancialmente a utilidade do documento.
- **Média:** requer revisão, mas permite uso exploratório controlado.
- **Baixa:** afeta sobretudo apresentação ou conveniência.

Usar este formato:

| Área | Estado | Severidade | Evidência | Ação recomendada |
|---|---|---|---|---|
| Hierarquia de títulos | OK | Baixa | Secções seguem o original | Manter |
| Tabela de preços | Rever | Alta | Duas colunas ficaram desalinhadas | Comparar com a fonte |
| Gráfico de segmentação | Não extraído | Alta | Só aparece a legenda | Aplicar extração visual autorizada |

Não marcar um documento como validado só porque passou verificações automáticas.

## Frontmatter YAML

Usar delimitadores YAML válidos e omitir valores que não possam ser confirmados:

```yaml
---
title: "Título do documento"
document_type: "report"
source_organization: "Nome da organização"
author: "não identificado"
publication_date: "2026-09-11"
conversion_date: "2026-09-11"
source_file: "nome-do-ficheiro-original.pdf"
source_format: "pdf"
language: "pt-PT"
geography:
  - "Portugal"
category:
  - "Consumer Insights"
tags:
  - "FMCG"
  - "innovation"
confidentiality: "internal"
processing_method: "markitdown_local"
quality_status: "reviewed"
quality_notes: "Tabela da página 14 requer validação."
---
```

Valores recomendados, quando aplicáveis:

- `document_type`: `report`, `interview`, `presentation`, `benchmark`, `article`, `meeting_notes`, `source`.
- `confidentiality`: `public`, `internal`, `confidential`, `restricted`.
- `processing_method`: `markitdown_local`, `markitdown_ocr`, `manual_review`.
- `quality_status`: `draft`, `reviewed`, `validated`.

Não forçar taxonomias quando o repositório já tiver um esquema próprio.

## Arquitetura e naming

Estrutura de referência, a adaptar ao contexto:

```text
knowledge-base/
├── 00_inbox/
├── 01_sources/
├── 02_consumer-insights/
├── 03_market-and-category/
├── 04_competitors-and-benchmarks/
├── 05_product-concepts/
├── 06_strategy-and-positioning/
├── 07_meeting-notes/
├── 08_outputs/
└── 99_archive/
```

Convenção:

```text
YYYY-MM-DD_tipo_geografia_tema_organizacao_v01.ext
```

Usar hífen, versões explícitas e nomes descritivos. Evitar `final`, `novo`, `versao-final` ou `documento-2`.

## Preparação para RAG

1. Manter o original ao lado do Markdown ou através de uma referência estável.
2. Adicionar metadados consistentes e controlo de acesso.
3. Preservar páginas, slides, folhas, citações e contexto metodológico.
4. Separar factos, interpretações, hipóteses e recomendações.
5. Criar chunks por secção semanticamente coerente; usar 400 a 1 000 palavras apenas como ponto de partida, ajustando ao sistema.
6. Não cortar tabelas, citações, definições, conclusões, metodologia ou listas de recomendações.
7. Repetir no chunk o cabeçalho necessário para interpretar uma tabela.
8. Marcar OCR e conteúdo visual inferido.
9. Incluir uma secção `Fontes e limitações`.
10. Testar recuperação com perguntas reais antes de considerar a coleção pronta.

## Estruturas FMCG e consumer insights

### Ficha de produto

```markdown
## Produto
- Marca:
- Categoria e subcategoria:
- País/mercado:
- Formato e peso/volume:
- Preço e preço por 100 g/ml:
- Canal e data de observação:

## Proposta de valor
- Benefício principal:
- Público-alvo e ocasião:
- Tensões ou jobs to be done:
- Claims:

## Produto e formulação
- Ingredientes relevantes:
- Perfil nutricional e alergénios:
- Diferenciadores:
- Sustentabilidade/embalagem:

## Avaliação
- Pontos fortes:
- Limitações:
- Espaço de oportunidade:
- Fonte e qualidade da evidência:
```

### Síntese de entrevista

```markdown
## Contexto
- Perfil, mercado, categoria, data e método:

## Jobs e necessidades
## Barreiras
## Gatilhos de compra
## Linguagem do consumidor
## Citações relevantes
## Implicações para inovação
## Limitações da evidência
```

### Leitura de tendência

```markdown
## Sinal
## Evidência
## Consumidor/segmento
## Comportamento emergente
## Marcas ou exemplos
## Relevância para a categoria
## Grau de maturidade
## Implicações e hipóteses
```
