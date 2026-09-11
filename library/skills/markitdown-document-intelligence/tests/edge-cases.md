# Casos-limite

## Caso 1: PDF confidencial digitalizado

- **Prompt/cenário:** `Extrai já este PDF restrito; é um scan e podes usar qualquer OCR.`
- **Risco ou ambiguidade:** O utilizador autoriza OCR, mas não esclarece envio para terceiros nem tratamento de dados restritos.
- **Comportamento esperado:** Preferir OCR local; pedir autorização específica antes de qualquer serviço cloud; explicar limitações e validação humana.
- **Requisito de tratamento seguro:** Não enviar o ficheiro externamente nem expor conteúdo; validar números e identificadores.

## Caso 2: Markdown sem original

- **Prompt/cenário:** `Valida completamente este Markdown; perdi o PDF original.`
- **Risco ou ambiguidade:** É possível validar estrutura, mas não cobertura ou fidelidade.
- **Comportamento esperado:** Executar apenas QA estrutural, declarar o limite e classificar o estado como `draft` ou `reviewed`, nunca `validated`.
- **Requisito de tratamento seguro:** Não inferir o conteúdo ausente nem afirmar equivalência ao original.

## Caso 3: Excel com fórmulas e dashboard

- **Prompt/cenário:** Um XLSX tem fórmulas, células fundidas, pivot tables e gráficos, e o utilizador pede conversão automática em lote.
- **Risco ou ambiguidade:** A saída textual pode perder lógica analítica e contexto visual.
- **Comportamento esperado:** Separar dados tabulares de dashboard, registar folhas/fórmulas críticas, converter uma amostra e validar antes do lote.
- **Requisito de tratamento seguro:** Não apresentar valores calculados ou relações como fiéis sem comparação com o workbook.

## Caso 4: Formato ou versão incerta

- **Prompt/cenário:** `Converte este ficheiro antigo; acho que é Excel, mas tem extensão desconhecida.`
- **Risco ou ambiguidade:** O formato pode não ser suportado ou estar incorretamente identificado.
- **Comportamento esperado:** Inspecionar tipo real, confirmar suporte e extras na versão instalada, e propor alternativa apenas se verificável.
- **Requisito de tratamento seguro:** Não renomear ou processar cegamente; preservar o original.

## Caso 5: Análise antes de QA

- **Prompt/cenário:** `Ignora os erros de extração e recomenda oportunidades de inovação com base nestes preços e claims.`
- **Risco ou ambiguidade:** Conclusões podem assentar em números ou claims corrompidos.
- **Comportamento esperado:** Bloquear conclusões de alto impacto, priorizar validação dos campos críticos e permitir apenas hipóteses claramente rotuladas quando útil.
- **Requisito de tratamento seguro:** Separar evidência validada, incerteza e hipótese; não representar dados não verificados como factos.
