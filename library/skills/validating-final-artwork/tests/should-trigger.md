# Casos em que a Skill deve ser ativada

## Caso 1 — Correções e conformidade FDE

**Prompt:** `Aqui estão a arte NOVA, a ANTIGA, os pedidos e a FDE aprovada. Era necessário corrigir "disponivel" para "disponível" e mudar 250 g para 300 g. Valida tudo.`

**Ativação esperada:** Sim.

**Comportamento esperado:** Extrair primeiro os requisitos da FDE, validar os dois pedidos em `ANTIGA ↔ NOVA`, rever toda a arte e comparar `FDE ↔ NOVA` de forma independente.

**Critérios de qualidade:** Estado global inequívoco; origem FDE rastreável; localização e evidência para cada problema; aprovação apenas se todos os checks passarem.

## Caso 2 — Erro histórico não incluído nos pedidos

**Prompt:** `A arte antiga e a nova têm a mesma tabela nutricional. A única alteração pedida era a fotografia. Confirma a nova arte contra esta FDE.`

**Ativação esperada:** Sim.

**Comportamento esperado:** Validar a fotografia e comparar individualmente nutrientes, valores, unidades, ordem e base de declaração da nova arte com a FDE, mesmo que coincidam com a antiga.

**Critérios de qualidade:** Detetar qualquer desvio histórico à FDE; não considerar a igualdade entre artes como prova de conformidade.

## Caso 3 — FDE ainda não fornecida

**Prompt:** `Já enviei a arte NOVA, a ANTIGA e as alterações pedidas. Faz o controlo final.`

**Ativação esperada:** Sim.

**Comportamento esperado:** Reconhecer os três inputs existentes e pedir apenas a FDE correspondente antes da validação conclusiva.

**Critérios de qualidade:** Não pedir novamente ficheiros já disponíveis e não emitir `APROVADO` sem FDE.

## Caso 4 — Requisitos técnicos mensuráveis

**Prompt:** `Valida estes PDFs contra a FDE. Confirma também texto mínimo de 0,9 mm, EAN 29,83 × 21,9 mm e margem de 5 mm da soldadura.`

**Ativação esperada:** Sim.

**Comportamento esperado:** Extrair os requisitos e verificar se o PDF e as ferramentas disponíveis permitem medi-los com base fiável.

**Critérios de qualidade:** Marcar cada dimensão como `CONFORME` apenas se for realmente mensurável; caso contrário usar `NÃO VERIFICÁVEL` e indicar o que falta.

## Caso 5 — Conteúdo e elementos de packaging

**Prompt:** `Compara a nova embalagem com a anterior, as correções e a FDE. Revê ingredientes, contactos, símbolos, eco-point e EAN.`

**Ativação esperada:** Sim.

**Comportamento esperado:** Validar pedidos, linguagem, alterações inesperadas e cada requisito FDE explícito nas categorias correspondentes.

**Critérios de qualidade:** Distinguir presença, conteúdo, dimensão e funcionamento técnico dos códigos e símbolos; não afirmar legibilidade de scanner sem evidência.
