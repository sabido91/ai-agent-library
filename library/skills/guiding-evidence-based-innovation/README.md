# Guiding Evidence-Based Innovation

Skill para orientar projetos de inovação com decisões fundamentadas em evidência, desde a identificação da oportunidade até à avaliação pós-lançamento.

## Plataforma suportada

- GPT/OpenAI

## Capacidades

- acompanhamento interativo de equipas de projeto;
- preparação de reuniões de aceleradores e gates;
- diagnóstico por fase e dimensão de risco;
- Innovation Scorecard fundamentado e rastreável;
- identificação de lacunas e pressupostos críticos;
- criação de test cards e learning cards;
- recomendação `Pivot`, `Persevere`, `Pause`, `Kill`, `Scale` ou `GO condicionado`;
- estrutura executiva de apresentação.

## Estrutura

```text
guiding-evidence-based-innovation/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── case-patterns.md
│   ├── evidence-and-scorecard.md
│   ├── output-templates.md
│   └── process-and-gates.md
└── tests/
    ├── edge-cases.md
    ├── should-not-trigger.md
    └── should-trigger.md
```

## Instalação

1. Rever o conteúdo e adaptar terminologia ou governance interna, se necessário.
2. Copiar a pasta completa para o diretório de Skills do repositório GPT/OpenAI.
3. Manter `SKILL.md` na raiz e `agents/openai.yaml` no caminho indicado.
4. Testar com os casos em `tests/` antes de disponibilizar à equipa.

## Exemplos de prompts

1. `Analisa este deck da fase 2B. Fundamenta o scorecard, identifica as três lacunas mais críticas e recomenda os próximos testes.`
2. `Com base nestes resultados e notas, prepara learning cards e uma recomendação para a reunião de aceleradores.`
3. `Estamos em 3B. Diagnostica por que razão temos boa distribuição mas rotação abaixo do target e propõe a estrutura da apresentação executiva.`

## Dependências

Não existem dependências de código nem conectores. A Skill requer apenas capacidade para ler os ficheiros fornecidos pelo utilizador.

## Limitações conhecidas

- Não acede a Monday, Miro, Click, Microsoft 365 ou outras fontes externas.
- A qualidade da recomendação depende da qualidade, atualidade e cobertura dos materiais fornecidos.
- Não substitui decisões de governance nem validações financeira, legal, regulatória, de qualidade ou segurança.
- Os casos externos são analogias; não funcionam como benchmarks universais.
- A Skill prepara uma estrutura de apresentação, mas não gera obrigatoriamente um ficheiro PowerPoint.

## Versão

`0.1.0`

## Última atualização

2026-09-03
