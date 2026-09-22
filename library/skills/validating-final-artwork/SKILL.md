---
name: validating-final-artwork
description: Valida uma nova arte final de embalagem, em PDF ou PNG, contra a versão anterior, as alterações pedidas e a FDE — Ficha de Desenvolvimento de Embalagem — como especificação aprovada independente. Confirma pedidos, conformidade FDE, linguagem, ortografia, informação, cores e consistência visual, e deteta alterações inesperadas. Usar em pedidos como "valida esta nova arte final", "confirma se as correções e a FDE foram cumpridas" ou "compara estas versões e verifica se nada mais mudou". Não usar para criar ou editar artes, aceitar outros formatos sem exportação para PDF ou PNG, certificar requisitos técnicos não mensuráveis, nem validar sem acesso visual suficiente aos ficheiros.
---

# Validating Final Artwork

## Objetivo

Avaliar uma nova arte final contra a versão anterior, as alterações pedidas e a FDE aprovada. Só aprovar quando os pedidos estiverem corretamente implementados, a nova versão cumprir todos os requisitos FDE verificáveis, passar a revisão global e não apresentar alterações inesperadas.

## Quando usar

- Comparar uma arte final antiga com uma nova.
- Validar uma lista de correções ou alterações solicitadas.
- Validar uma arte de embalagem contra a FDE correspondente.
- Fazer controlo final de conteúdo, linguagem e consistência visual.
- Confirmar que elementos fora do âmbito do pedido permaneceram inalterados.

## Quando não usar

- Criar, redesenhar ou editar a arte final.
- Comparar apenas descrições textuais sem acesso às duas versões visuais.
- Resumir ou rever uma FDE sem existir um pedido de validação de arte final.
- Certificar requisitos técnicos de impressão que não estejam visíveis ou disponíveis em metadata verificável, como separações, tintas diretas, perfis ICC, fontes incorporadas, sangria ou resolução efetiva.
- Substituir revisão legal, regulamentar ou de marca especializada.

## Inputs esperados

Exigir:

1. Nova arte final, identificada como `NOVA`.
2. Arte final anterior, identificada como `ANTIGA`.
3. Lista das alterações pedidas, mesmo que indique explicitamente que não houve pedidos.
4. FDE — Ficha de Desenvolvimento de Embalagem — correspondente e aprovada, identificada como `FDE`.

Recolher os inputs pela ordem `NOVA → ANTIGA → alterações pedidas → FDE`, sem pedir novamente um elemento que já esteja disponível na conversa. Se faltar a FDE, pedi-la antes da validação conclusiva. Sem FDE, não emitir `APROVADO`.

Aceitar exclusivamente PDF ou PNG. As artes e a FDE podem usar formatos diferentes entre estas duas opções, desde que sejam legíveis e seja possível estabelecer a correspondência inequívoca. Para qualquer outro formato, pedir uma exportação visual fiel em PDF ou PNG antes de validar. Pedir apenas a informação em falta que impeça uma conclusão fiável, como versão da FDE, correspondência entre páginas, idioma pretendido ou texto ilegível.

## Workflow

1. **Validar os inputs.** Confirmar que existem `NOVA`, `ANTIGA`, alterações pedidas e `FDE`, sem voltar a pedir o que já estiver na conversa. Identificar páginas, faces, variantes, idiomas, versão/data da FDE e diferenças de dimensão ou orientação. Não iniciar uma validação conclusiva se a correspondência ou a especificação aplicável forem ambíguas.
2. **Avaliar a legibilidade e mensurabilidade.** Verificar se texto, detalhes, cores, escalas, dimensões e metadata necessários são acessíveis. Assinalar como `NÃO VERIFICÁVEL` qualquer requisito que não possa ser inspecionado ou medido com confiança; nunca adivinhar conteúdo, dimensões ou propriedades técnicas.
3. **Transformar a FDE numa checklist.** Antes de analisar a arte, extrair apenas requisitos explicitamente definidos na FDE, seguindo a [checklist de conformidade FDE](references/fde-validation-checklist.md). Registar categoria, requisito exato, valor/unidade, origem por página/secção, método de verificação e condição de aceitação.
4. **Criar a matriz de alterações pedidas.** Separar cada pedido num item verificável e registar o resultado como `IMPLEMENTADO`, `PARCIAL`, `NÃO IMPLEMENTADO` ou `NÃO VERIFICÁVEL`.
5. **Validar as alterações pedidas.** Comparar `ANTIGA ↔ NOVA`, localizar cada elemento, confirmar a alteração concreta e verificar se a implementação introduziu erros colaterais.
6. **Rever obrigatoriamente a linguagem da nova arte.** Ler todo o texto visível, incluindo títulos, corpo, rodapés, legendas, chamadas, datas, preços, unidades, contactos, avisos e texto legal. Verificar ortografia, gramática, concordância, pontuação, capitalização, acentuação, espaços, quebras, hifenização, duplicações e texto truncado. Respeitar nomes próprios, marcas, códigos e grafias deliberadas; quando houver dúvida, reportar como possível erro e indicar a incerteza.
7. **Rever a nova arte globalmente.** Aplicar a [checklist de revisão de arte final](references/artwork-review-checklist.md). Verificar informação, coerência interna, cores aparentes, contraste, alinhamento, hierarquia, consistência, elementos em falta, sobreposições, cortes e legibilidade. Distinguir inspeção visual de validação técnica de pré-impressão.
8. **Detetar alterações inesperadas.** Comparar todos os elementos visíveis que não constam dos pedidos: texto, números, imagens, logótipos, ícones, cores, posições, tamanhos, espaçamentos, fundos, margens e composição. Ignorar apenas diferenças de renderização sem efeito no conteúdo, como compressão ou antialiasing; indicar essa interpretação quando relevante.
9. **Validar a conformidade FDE.** Comparar `FDE ↔ NOVA` de forma independente da arte antiga e das alterações pedidas. Classificar cada requisito como `CONFORME`, `NÃO CONFORME` ou `NÃO VERIFICÁVEL`, citando a origem na FDE e a evidência na nova arte. Um erro que já existia na arte antiga continua a ser uma não conformidade.
10. **Resolver conflitos.** Se a FDE e as alterações pedidas entrarem em conflito, não presumir que o pedido atualiza a especificação. Reportar o conflito e pedir uma FDE atualizada ou confirmação autorizada; não emitir `APROVADO` enquanto a fonte aplicável não estiver esclarecida.
11. **Determinar o estado final.** Usar `REPROVADO` se existir qualquer problema confirmado, incluindo desvio à FDE. Na ausência de problemas confirmados, usar `NÃO VERIFICÁVEL` se faltar a FDE ou se um requisito obrigatório não puder ser validado. Usar `APROVADO` apenas quando todos os pedidos estiverem implementados, todos os requisitos FDE aplicáveis estiverem conformes, a revisão global não encontrar problemas e não houver alterações inesperadas.
12. **Emitir o check.** Ser conciso quando estiver tudo correto. Se houver problemas ou limitações, listar cada um com localização, requisito e evidência suficientes para permitir correção ou nova verificação.

## Formato de output

Começar sempre pelo estado global:

```markdown
# Resultado: APROVADO | REPROVADO | NÃO VERIFICÁVEL

## Check
- Alterações pedidas: OK | PROBLEMA | NÃO VERIFICÁVEL
- Linguagem e ortografia: OK | PROBLEMA | NÃO VERIFICÁVEL
- Informação e consistência visual: OK | PROBLEMA | NÃO VERIFICÁVEL
- Alterações inesperadas: NÃO DETETADAS | DETETADAS | NÃO VERIFICÁVEL
- Conformidade com FDE: OK | PROBLEMA | NÃO VERIFICÁVEL
```

Se o resultado for `APROVADO`, acrescentar apenas uma conclusão curta. Se for `REPROVADO` ou `NÃO VERIFICÁVEL`, acrescentar:

```markdown
## Problemas encontrados

| # | Categoria | Localização | Problema | Evidência | Correção esperada |
|---|-----------|-------------|----------|----------|-------------------|
| 1 | Alteração pedida / Linguagem / Informação / Visual / Alteração inesperada | Página, face ou zona | Descrição objetiva | Antiga, nova e/ou pedido relevante | Ação concreta |

## Alterações pedidas

| Pedido | Estado | Evidência |
|--------|--------|----------|
| ... | IMPLEMENTADO / PARCIAL / NÃO IMPLEMENTADO / NÃO VERIFICÁVEL | ... |

## Conformidade com FDE

| # | Categoria | Requisito FDE | Arte nova | Estado | Correção esperada |
|---|-----------|---------------|-----------|--------|-------------------|
| 1 | Conteúdo / Nutrição / Packaging / Gráfico-técnico | Requisito e origem na FDE | Evidência e localização | CONFORME / NÃO CONFORME / NÃO VERIFICÁVEL | Ação concreta ou forma de verificar |

## Limitações
- Indicar apenas limitações que afetem a conclusão.
```

Não declarar que um problema não existe quando a zona correspondente não foi verificável.

## Regras de qualidade

- Basear cada conclusão em conteúdo observável nas duas versões, no pedido e na FDE.
- Tratar a FDE como fonte de verdade apenas para os requisitos que nela estejam explicitamente definidos.
- Manter rastreabilidade entre cada requisito FDE, a página/secção de origem e a evidência na nova arte.
- Rever sempre a linguagem, mesmo que o utilizador não a mencione.
- Fazer a comparação nos dois sentidos: confirmar o que devia mudar e confirmar o que devia permanecer.
- Fazer a comparação `FDE ↔ NOVA` mesmo quando `ANTIGA` e `NOVA` forem iguais.
- Dar localização específica por página, face, painel ou zona visual.
- Separar erros confirmados de suspeitas e limitações.
- Não reprovar por diferenças puramente técnicas de renderização sem impacto visual ou informativo.
- Não suavizar o estado final: qualquer problema confirmado implica `REPROVADO`.
- Manter o relatório curto, acionável e sem reescrever todo o conteúdo correto.

## Gestão de incerteza

- Pedir nova exportação ou imagem de maior resolução quando a leitura não for fiável.
- Marcar dimensões mínimas, margens, zonas, orientação, número de cores e limitações de impressão como `NÃO VERIFICÁVEL` quando não existirem escala, geometria, metadata ou ferramentas adequadas para as comprovar.
- Distinguir presença e conteúdo de um código da sua legibilidade técnica: não declarar um EAN legível por scanner sem teste ou evidência apropriada.
- Se o idioma ou variante linguística não estiverem definidos, inferir apenas quando houver evidência clara; caso contrário, pedir confirmação ou declarar a assunção.
- Classificar como `NÃO VERIFICÁVEL` apenas o ponto afetado e elevar o resultado global para `NÃO VERIFICÁVEL` quando esse ponto for necessário para aprovar.
- Usar expressões como `possível erro` quando uma grafia possa ser nome próprio, marca, termo técnico ou escolha editorial.

## Limites e segurança

- Não inventar texto, requisitos, especificações de marca ou critérios de impressão.
- Não inferir requisitos FDE a partir de práticas habituais quando não estiverem escritos na FDE fornecida.
- Não expor informação sensível presente nos ficheiros além do necessário para identificar o problema.
- Não afirmar equivalência colorimétrica a partir de uma simples visualização no ecrã.
- Não afirmar aprovação técnica para produção quando não forem verificáveis ficheiro, resolução, sangria, perfis, separações, fontes e restantes requisitos de pré-impressão.
- Não alterar nem publicar os ficheiros recebidos.

## Referências e recursos

- Consultar [references/artwork-review-checklist.md](references/artwork-review-checklist.md) durante a revisão global e a deteção de alterações inesperadas.
- Consultar [references/fde-validation-checklist.md](references/fde-validation-checklist.md) antes de comparar a FDE com a nova arte.
