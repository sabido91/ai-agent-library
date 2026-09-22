# Changelog

## [0.2.0] - 2026-09-22

### Added

- FDE como input obrigatório e fonte independente de requisitos explicitamente definidos.
- Extração da FDE para uma checklist rastreável de conteúdo, nutrição, packaging e requisitos gráfico-técnicos.
- Comparação independente `FDE ↔ NOVA`, capaz de detetar erros históricos preservados da arte antiga.
- Estado de conformidade FDE e tabela própria no relatório.
- Regras de mensurabilidade para dimensões, margens, códigos, cores e limitações de impressão.
- Tratamento de conflitos entre FDE, alterações pedidas e múltiplas versões da especificação.

### Changed

- Fluxo de recolha atualizado para `NOVA → ANTIGA → alterações pedidas → FDE → validação`.
- Aprovação condicionada à conformidade com todos os requisitos FDE aplicáveis e verificáveis.

## [0.1.1] - 2026-09-18

### Changed

- Restringidos os inputs suportados a PDF e PNG.
- Clarificado que as duas versões podem combinar PDF e PNG quando a correspondência entre conteúdos for inequívoca.
- Passou a ser exigida uma exportação para PDF ou PNG quando o ficheiro de origem estiver noutro formato.

## [0.1.0] - 2026-09-18

### Added

- Versão inicial da Skill para comparar artes finais antigas e novas.
- Validação individual das alterações pedidas.
- Revisão obrigatória de linguagem, ortografia, informação, cores aparentes e composição visual.
- Deteção de alterações inesperadas fora do âmbito do pedido.
- Estados globais `APROVADO`, `REPROVADO` e `NÃO VERIFICÁVEL`.
- Checklist de revisão, metadata GPT/OpenAI e testes comportamentais.
