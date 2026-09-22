# Develop Consumer Brand Copy

Skill para transformar briefings de marcas de consumo em estratégia criativa e copy pronta a desenvolver para packaging, campanhas, key visuals, social, POS, e-commerce e vídeo.

## Plataforma suportada

- GPT/OpenAI

## Estrutura

```text
develop-consumer-brand-copy/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml
└── tests/
    ├── should-trigger.md
    ├── should-not-trigger.md
    └── edge-cases.md
```

Não existem `scripts/`, `references/` ou `assets/`: a capacidade depende de instruções editoriais e do material fornecido em cada briefing, sem operações determinísticas ou recursos estáticos adicionais.

## Instalação

1. Rever o conteúdo e os testes.
2. Copiar a pasta `develop-consumer-brand-copy` para a localização de Skills do repositório GPT/OpenAI adotada pela equipa.
3. Validar a Skill no ambiente de destino antes de a disponibilizar aos utilizadores.

## Exemplos de prompts

1. `Cria três territórios criativos e a copy de frente e verso para uma nova bebida de aveia. O mercado é Portugal e só podemos usar os claims presentes neste briefing.`
2. `Refina esta headline e adapta-a para OOH, Instagram e ponto de venda, mantendo um tom premium mas próximo.`
3. `Analisa estes claims de embalagem, separa factos de linguagem criativa e assinala o que precisa de validação legal.`

## Dependências

Sem dependências externas ou conectores obrigatórios. Os guias de marca, provas de produto e restrições legais devem ser fornecidos pelo utilizador quando forem relevantes.

## Limitações conhecidas

- Não confirma conformidade jurídica ou regulatória.
- Não valida claims sem evidência fornecida.
- Não substitui investigação de consumidor, testes de mercado ou arte-final de design.
- A qualidade e especificidade da resposta dependem da informação disponível no briefing.

## Versão

`0.1.0`

Última atualização: 2026-09-22
