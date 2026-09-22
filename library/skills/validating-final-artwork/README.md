# Validação de Artes Finais

## Propósito

`validating-final-artwork` ajuda o GPT a validar uma nova arte final contra a versão anterior, as alterações pedidas e a FDE — Ficha de Desenvolvimento de Embalagem — aprovada. Confirma os pedidos, faz uma revisão obrigatória de linguagem e qualidade global, deteta alterações inesperadas e verifica requisitos FDE de conteúdo, nutrição, packaging e produção que sejam comprováveis.

## Plataforma suportada

- GPT/OpenAI

## Estrutura

```text
validating-final-artwork/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── artwork-review-checklist.md
│   └── fde-validation-checklist.md
└── tests/
    ├── should-trigger.md
    ├── should-not-trigger.md
    └── edge-cases.md
```

`references/` contém as checklists necessárias para a revisão linguística, informativa e visual e para extrair e validar requisitos da FDE. Não são necessários scripts nem assets: a inspeção e a mensurabilidade dependem dos dados efetivamente acessíveis nos ficheiros enviados.

## Instalação

1. Rever o conteúdo da pasta da Skill.
2. Copiar a pasta `validating-final-artwork` para o repositório privado de Skills GPT/OpenAI.
3. Disponibilizar a Skill no ambiente GPT/OpenAI segundo o processo interno aplicável.
4. Testar com duas artes de controlo, uma lista conhecida de alterações e a FDE aprovada antes do uso em produção.

## Exemplos de prompts

1. `Valida a arte NOVA contra a ANTIGA, estas alterações pedidas e a FDE. Revê também a linguagem e confirma que nada mais mudou.`
2. `Verifica se esta nova embalagem cumpre a FDE, incluindo ingredientes, tabela nutricional, EAN e requisitos gráficos mensuráveis.`
3. `Faz o controlo final destes ficheiros. Mesmo que a arte antiga e a nova coincidam, reporta qualquer desvio da nova arte face à FDE.`

## Dependências

- Um GPT com capacidade para abrir e inspecionar visualmente ficheiros PDF e PNG.
- Arte nova, arte anterior, lista de alterações pedidas e FDE aprovada.
- Se a origem estiver noutro formato, uma exportação visual fiel para PDF ou PNG antes da validação.

Não existem dependências de código nem conectores externos.

## Limitações conhecidas

- A comparação visual não certifica por si só propriedades técnicas de pré-impressão, como perfis ICC, separações, sobreimpressão, sangria, fontes incorporadas ou resolução efetiva.
- Dimensões, margens, códigos e requisitos técnicos só são considerados conformes quando forem realmente mensuráveis ou testáveis nos ficheiros e ferramentas disponíveis.
- Ficheiros desfocados, incompletos ou com escalas muito diferentes podem impedir uma conclusão segura.
- A equivalência colorimétrica não pode ser garantida apenas pela visualização no ecrã.
- A Skill assinala incerteza em nomes próprios, marcas ou linguagem técnica que não consiga validar com segurança.

## Versão

- Versão atual: `0.2.0`
- Última atualização: `2026-09-22`
