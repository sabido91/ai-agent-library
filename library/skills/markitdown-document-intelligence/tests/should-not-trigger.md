# Casos em que não deve ativar

## Caso 1: Edição de design PowerPoint

- **Prompt:** `Redesenha estes slides e aplica a nossa identidade visual.`
- **Não ativação esperada:** Sim.
- **Motivo:** O pedido é de design/edição da apresentação, não de conversão e inteligência documental.
- **Comportamento alternativo preferível:** Usar uma Skill de apresentações ou design de slides.

## Caso 2: Escrita sem documento-fonte

- **Prompt:** `Escreve um artigo de opinião sobre tendências de bebidas funcionais.`
- **Não ativação esperada:** Sim.
- **Motivo:** Não existe conversão, validação documental ou preparação de conhecimento.
- **Comportamento alternativo preferível:** Usar um workflow de investigação e redação, pedindo fontes quando necessário.

## Caso 3: Programação genérica em Python

- **Prompt:** `Ajuda-me a corrigir um erro de autenticação na minha API Flask.`
- **Não ativação esperada:** Sim.
- **Motivo:** O problema não envolve MarkItDown nem documentos.
- **Comportamento alternativo preferível:** Diagnosticar a aplicação com uma Skill de engenharia de software.

## Caso 4: Preservação visual fiel

- **Prompt:** `Converte este catálogo para Markdown mantendo exatamente o layout, as fontes e a paginação.`
- **Não ativação esperada:** Sim para a promessa de fidelidade; a Skill só pode ser usada se o objetivo for reformulado.
- **Motivo:** Markdown não preserva fielmente o design pedido.
- **Comportamento alternativo preferível:** Explicar a limitação e sugerir PDF/HTML ou reconstrução visual por ferramenta adequada.
