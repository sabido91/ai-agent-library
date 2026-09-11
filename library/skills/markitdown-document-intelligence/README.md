# MarkItDown Document Intelligence

Skill para orientar a conversão de documentos em Markdown com MarkItDown, validar a qualidade da extração e preparar os resultados para arquivo, pesquisa, RAG, agentes e análise estratégica.

## Plataforma suportada

- GPT/OpenAI

## Estrutura

```text
markitdown-document-intelligence/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── markitdown-playbook.md
│   └── qa-metadata.md
├── scripts/
│   └── validate_markdown.py
└── tests/
    ├── should-trigger.md
    ├── should-not-trigger.md
    └── edge-cases.md
```

`references/` separa instruções técnicas e modelos detalhados do workflow principal. `scripts/` contém uma pré-validação estrutural repetível; não substitui a comparação com o documento original. Não existem assets porque a Skill não necessita de templates binários ou recursos estáticos.

## Instalação

Copiar a pasta `markitdown-document-intelligence` para a localização de Skills do repositório ou carregar o ZIP na plataforma compatível. Rever primeiro as políticas internas de tratamento de documentos e instalar o MarkItDown apenas no ambiente em que a conversão será executada.

## Exemplos de prompts

1. `Converte este relatório PDF para Markdown e prepara-o para uma base RAG. O documento é interno e contém tabelas.`
2. `Revê este Markdown convertido de uma apresentação e identifica conteúdo visual ou notas que possam ter ficado por extrair.`
3. `Cria um processo em lote para converter estes ficheiros XLSX e DOCX localmente, normalizar metadados e produzir um relatório de QA.`

## Dependências

- A Skill, por si só, não requer dependências.
- A conversão requer Python 3.10 ou superior e o pacote `markitdown` com os extras correspondentes aos formatos usados.
- `scripts/validate_markdown.py` usa apenas a biblioteca standard do Python.
- OCR, descrição visual, transcrição e serviços cloud são opcionais e requerem decisão explícita, dependências próprias e, quando aplicável, credenciais fornecidas pelo utilizador.

## Limitações conhecidas

- Não preserva fielmente design, paginação, tipografia, animações ou composição visual.
- A qualidade depende do formato, da versão instalada e da complexidade do documento.
- OCR, gráficos, diagramas, fórmulas e tabelas complexas exigem validação humana.
- O validador incluído verifica estrutura e metadados, mas não mede fidelidade ao original.
- Não inclui integrações automáticas com Notion, GitHub, NotebookLM, bases vectoriais ou APIs externas.

## Versão

- Versão atual: `0.1.0`
- Última atualização: `2026-09-11`

## Fontes técnicas

As instruções técnicas foram verificadas contra o repositório oficial Microsoft MarkItDown: <https://github.com/microsoft/markitdown>. Confirmar a documentação da versão instalada antes de automatizações de produção.
