# Checklist de conformidade com a FDE

Usar esta referência para transformar a FDE — Ficha de Desenvolvimento de Embalagem — numa checklist rastreável antes de analisar a arte nova. Extrair apenas requisitos explicitamente presentes na FDE fornecida; não completar lacunas com conhecimento geral.

## Registo de cada requisito

Para cada requisito, registar:

- Categoria.
- Formulação exata ou resumo fiel do requisito.
- Valor, unidade, tolerância ou condição, quando existirem.
- Página, secção, tabela ou campo de origem na FDE.
- Elemento e localização esperados na arte nova.
- Método de verificação possível.
- Estado: `CONFORME`, `NÃO CONFORME` ou `NÃO VERIFICÁVEL`.

## 1. Conteúdo obrigatório

Extrair quando definidos:

- Denominação do alimento.
- Lista de ingredientes e formulação.
- Alergénios e destaques exigidos.
- Alegações e menções obrigatórias.
- Condições de conservação e utilização.
- Operador responsável.
- Data ou indicação de validade.
- Quantidade líquida.
- Contactos.
- País/origem, lote e restantes menções previstas na FDE.

Comparar texto, presença, ordem, destaque e localização apenas na medida em que a FDE os especifique.

## 2. Informação nutricional

Extrair e comparar individualmente:

- Nutrientes e respetiva ordem.
- Valores e casas decimais.
- Unidades.
- Base de declaração, como `por 100 g`, `por 100 ml` ou porção.
- Tamanho e número de porções, quando aplicável.
- Percentagens, notas e formulação dos cabeçalhos.

Não considerar a tabela conforme apenas por semelhança visual. Comparar cada rótulo, valor, unidade e base de declaração.

## 3. Elementos de packaging

Extrair quando definidos:

- EAN e respetiva sequência numérica.
- Símbolos obrigatórios.
- Códigos internos, de lote ou certificação.
- Eco-point ou elementos ambientais.
- Elementos que devam aparecer conjuntamente.
- Regras explícitas de posição, proximidade ou agrupamento.

Distinguir quatro verificações: presença, conteúdo, dimensão e funcionamento técnico. A presença visual de um EAN não comprova dimensão, quiet zone, contraste ou leitura por scanner.

## 4. Requisitos gráficos e técnicos

Extrair quando definidos:

- Zonas onde não pode existir informação.
- Zonas reservadas ou áreas de segurança.
- Dimensões mínimas de texto, símbolos, códigos ou outros elementos.
- Distâncias mínimas a cortes, dobras ou soldaduras.
- Orientação e sentido de leitura.
- Número de cores.
- Cores ou referências técnicas declaradas.
- Limitações do processo de impressão.
- Outras condições mensuráveis de produção.

## Regras de mensurabilidade

- Validar uma dimensão apenas quando o ficheiro conservar escala/geometria fiável ou existir uma ferramenta de medição adequada.
- Não converter pixels em milímetros sem resolução física ou escala verificável.
- Não medir a partir de uma captura de ecrã redimensionada.
- Não marcar como conforme um requisito como `texto ≥ 0,9 mm`, `EAN 29,83 × 21,9 mm` ou `margem de 5 mm` apenas por parecer visualmente correto.
- Classificar como `NÃO VERIFICÁVEL` quando faltar base de medição e indicar o dado ou ficheiro necessário.
- Não confirmar número de cores, separações, sobreimpressão, perfis ou limitações do processo apenas pela aparência do PDF/PNG.

## Conflitos e omissões

- Se a FDE contiver requisitos contraditórios, indicar as duas origens e pedir esclarecimento.
- Se a alteração pedida contrariar a FDE, não assumir que a alteração atualiza a especificação.
- Se um campo esperado estiver vazio na FDE, não inventar o requisito; registar a omissão apenas quando ela impedir a validação.
- Se houver várias versões da FDE, pedir identificação da versão aprovada aplicável.

## Regra de independência

Comparar sempre `FDE ↔ NOVA` de forma independente. Uma coincidência entre `ANTIGA` e `NOVA` não prova conformidade com a FDE e não neutraliza um desvio histórico.
