# Casos em que a Skill não deve ser ativada

## Caso 1 — Criação de uma arte

**Prompt:** `Cria uma nova embalagem para este produto com um estilo minimalista.`

**Não ativação esperada:** Não ativar.

**Motivo:** O pedido é de criação e design, não de comparação e validação entre versões.

**Comportamento alternativo preferível:** Usar uma capacidade de design ou criação de imagem e recolher o briefing visual.

## Caso 2 — Revisão de texto isolado

**Prompt:** `Corrige a ortografia deste comunicado em texto.`

**Não ativação esperada:** Não ativar.

**Motivo:** Não existem artes antiga e nova nem um pedido de comparação visual.

**Comportamento alternativo preferível:** Fazer revisão linguística direta do texto.

## Caso 3 — Edição do ficheiro

**Prompt:** `Abre este PSD e muda o preço para 19,99 €.`

**Não ativação esperada:** Não ativar.

**Motivo:** O pedido é para editar um ficheiro, enquanto a Skill apenas avalia versões.

**Comportamento alternativo preferível:** Usar uma ferramenta ou workflow de edição compatível com PSD.

## Caso 4 — Certificação técnica sem comparação

**Prompt:** `Certifica que este PDF está tecnicamente pronto para impressão offset, incluindo separações, sobreimpressão e perfis ICC.`

**Não ativação esperada:** Não ativar.

**Motivo:** O pedido exige pré-impressão técnica especializada e não uma comparação visual entre duas versões.

**Comportamento alternativo preferível:** Usar uma ferramenta de preflight e validação técnica de impressão com acesso aos dados internos do PDF.

## Caso 5 — Resumo isolado da FDE

**Prompt:** `Resume esta FDE e cria uma lista dos principais campos.`

**Não ativação esperada:** Não ativar.

**Motivo:** O pedido é de resumo documental e não de validação de uma nova arte final.

**Comportamento alternativo preferível:** Resumir o documento diretamente, sem executar o workflow de comparação de artes.
