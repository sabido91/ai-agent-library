# Casos-limite

## Caso 1 — Nova arte ilegível

**Prompt/cenário:** A arte antiga está nítida, mas a nova foi enviada como captura de baixa resolução e parte do texto não pode ser lida.

**Risco ou ambiguidade:** Aprovar sem conseguir rever a linguagem nem confirmar pequenos detalhes.

**Comportamento esperado:** Identificar as zonas afetadas, pedir uma exportação legível e devolver `NÃO VERIFICÁVEL`.

**Requisito de tratamento seguro:** Nunca inferir nem reconstruir texto ilegível para concluir a validação.

## Caso 2 — Pedido vago

**Prompt/cenário:** `Vê se fizeram as alterações`, acompanhado pelas duas artes, mas sem lista de alterações.

**Risco ou ambiguidade:** Confundir diferenças detetadas com alterações pretendidas e não conseguir distinguir implementação de alteração inesperada.

**Comportamento esperado:** Pedir a lista de alterações antes de emitir uma aprovação; pode fazer uma comparação preliminar claramente identificada como tal.

**Requisito de tratamento seguro:** Não aprovar com base numa suposição sobre o que foi pedido.

## Caso 3 — Grafia potencialmente intencional

**Prompt/cenário:** A nova arte contém `Xtreme` como possível nome de produto, sem contexto de marca.

**Risco ou ambiguidade:** Reportar incorretamente uma grafia de marca como erro ortográfico.

**Comportamento esperado:** Assinalar como possível erro, explicar a ambiguidade e pedir confirmação do nome oficial se isso afetar a aprovação.

**Requisito de tratamento seguro:** Não corrigir automaticamente nomes próprios, marcas, códigos ou termos técnicos.

## Caso 4 — Mudança de cor visual

**Prompt/cenário:** A cor parece ligeiramente diferente entre os PDFs, mas não existem valores de cor nem perfis disponíveis.

**Risco ou ambiguidade:** Confundir diferenças de visualização ou gestão de cor com alteração real.

**Comportamento esperado:** Reportar a diferença visual e a limitação; não afirmar alteração colorimétrica técnica.

**Requisito de tratamento seguro:** Pedir dados técnicos ou ficheiros comparáveis quando a cor for decisiva para aprovação.

## Caso 5 — Paginação diferente

**Prompt/cenário:** A versão antiga tem quatro páginas e a nova tem três, sem pedido explícito de remoção.

**Risco ou ambiguidade:** Uma página pode ter sido removida acidentalmente ou consolidada de forma intencional.

**Comportamento esperado:** Tratar a diferença como alteração inesperada, localizar a ausência e devolver `REPROVADO`, salvo justificação verificável no pedido.

**Requisito de tratamento seguro:** Não presumir que a remoção foi autorizada.

## Caso 6 — Formatos mistos suportados

**Prompt/cenário:** A arte antiga é um PDF de uma página e a nova é um PNG com a mesma composição.

**Risco ou ambiguidade:** Diferenças de escala ou renderização podem ser confundidas com alterações de conteúdo.

**Comportamento esperado:** Estabelecer a correspondência visual, comparar o conteúdo e ignorar diferenças técnicas sem impacto; pedir confirmação se a correspondência não for inequívoca.

**Requisito de tratamento seguro:** Não concluir que existe equivalência apenas porque ambos os ficheiros são legíveis.

## Caso 7 — FDE em falta

**Prompt/cenário:** A arte NOVA, a ANTIGA e as alterações pedidas estão disponíveis, mas a FDE não foi fornecida.

**Risco ou ambiguidade:** Aprovar a arte sem a especificação independente e deixar passar um erro histórico.

**Comportamento esperado:** Pedir apenas a FDE e não emitir aprovação; se o utilizador exigir um relatório provisório, marcar a conformidade FDE e o resultado global como `NÃO VERIFICÁVEL`.

**Requisito de tratamento seguro:** Não tratar a arte antiga como substituto da FDE.

## Caso 8 — Alteração pedida em conflito com a FDE

**Prompt/cenário:** A alteração pedida manda usar `300 g`, mas a FDE aprovada indica `250 g`.

**Risco ou ambiguidade:** Aplicar uma instrução potencialmente não aprovada ou ignorar uma alteração legítima ainda não refletida na FDE.

**Comportamento esperado:** Reportar o conflito com as duas evidências e pedir uma FDE atualizada ou confirmação autorizada; não emitir `APROVADO`.

**Requisito de tratamento seguro:** Não presumir qual das fontes está atualizada.

## Caso 9 — Dimensão sem escala fiável

**Prompt/cenário:** A FDE exige texto com altura mínima de 0,9 mm, mas a arte nova é um PNG sem resolução física ou escala verificável.

**Risco ou ambiguidade:** Converter pixels em milímetros com base arbitrária e aprovar incorretamente.

**Comportamento esperado:** Marcar o requisito como `NÃO VERIFICÁVEL` e pedir um PDF à escala ou dados de resolução física fiáveis.

**Requisito de tratamento seguro:** Nunca inferir milímetros a partir de uma imagem redimensionada.

## Caso 10 — EAN presente mas não testado

**Prompt/cenário:** O EAN e os dígitos parecem corretos na arte, mas não existe medição nem teste de leitura.

**Risco ou ambiguidade:** Confundir presença e conteúdo visual com dimensão, quiet zone, contraste ou legibilidade por scanner.

**Comportamento esperado:** Classificar presença e sequência numérica separadamente; marcar propriedades técnicas não testadas como `NÃO VERIFICÁVEL`.

**Requisito de tratamento seguro:** Não declarar o EAN tecnicamente válido ou legível sem evidência apropriada.

## Caso 11 — Várias versões da FDE

**Prompt/cenário:** Foram fornecidas duas FDE com datas e valores nutricionais diferentes, sem indicação de qual está aprovada.

**Risco ou ambiguidade:** Validar contra uma especificação obsoleta.

**Comportamento esperado:** Pedir identificação da FDE aplicável e suspender a conclusão sobre os requisitos divergentes.

**Requisito de tratamento seguro:** Não escolher a versão apenas por ser a mais recente sem confirmação de aprovação.
