# Templates de output

## Regra de utilização

Selecionar e adaptar módulos; não devolver todos por defeito. Preencher lacunas com `Não fornecido` ou `Não demonstrado`.

## Síntese executiva

```markdown
## Síntese executiva

- Projeto e fase:
- Decisão a suportar:
- Leitura principal:
- Evidência mais forte:
- Risco crítico:
- Recomendação:
- Condição ou próximo passo decisivo:
```

## Diagnóstico

```markdown
## Diagnóstico

| Dimensão | Estado | Evidência principal | Lacuna crítica | Implicação |
| --- | --- | --- | --- | --- |

### Hipóteses alternativas
1. ...

### O que os dados ainda não permitem concluir
- ...
```

## Scorecard fundamentado

```markdown
## Innovation Scorecard

| Dimensão | Critério | Score | Nível de evidência | Fundamentação | Fonte | Confiança | Risco aberto |
| --- | --- | ---: | --- | --- | --- | --- | --- |

### Leitura do scorecard
- Força principal:
- Fragilidade bloqueadora:
- Alteração desde a revisão anterior:
```

## Registo de lacunas

```markdown
## Lacunas prioritárias

| Prioridade | Lacuna | Tipo | Impacto na decisão | Evidência mínima necessária | Owner/prazo |
| ---: | --- | --- | --- | --- | --- |
```

Usar `Tipo` = documentação, evidência, capacidade, decisão ou métrica.

## Perguntas críticas

```markdown
## Perguntas que podem mudar a decisão

1. **Pergunta:** ...
   **Porque importa agora:** ...
   **Resposta/evidência necessária:** ...
```

Limitar a perguntas materiais; não reproduzir a checklist inteira do gate.

## Test card

```markdown
## Test card — [nome]

- **Pressuposto crítico:** Acreditamos que...
- **Dimensão:** Desirability / Feasibility / Viability / Adaptability / Strategic Fit / Opportunity
- **Para verificar, faremos:** ...
- **População e contexto:** ...
- **Mediremos:** ...
- **Estaremos certos se:** ...
- **Critério de interrupção:** ...
- **Decisão associada:** Se..., então...
- **Owner, prazo e custo:** ...
- **Vieses e limites:** ...
```

## Learning card

```markdown
## Learning card — [nome]

- **Acreditávamos que:** ...
- **Observámos:** ...
- **Fonte:** ...
- **Aprendemos que:** ...
- **Força e limites:** ...
- **Assim sendo, vamos:** ...
- **Impacto no scorecard/modelo:** ...
```

## Recomendação de gate

```markdown
## Recomendação

**[PERSEVERE / PIVOT / PAUSE / KILL / SCALE / GO CONDICIONADO]**

### Porque
- Evidência favorável:
- Evidência contrária:
- Risco crítico remanescente:

### Condições
| Condição | Evidência de fecho | Owner | Prazo | Consequência se falhar |
| --- | --- | --- | --- | --- |

### Próxima revisão
- Data ou evento:
- Decisor responsável:
```

## Estrutura de apresentação

Adaptar o número de slides à decisão. Estrutura recomendada para uma revisão completa:

1. **The Ask** — decisão pedida e recomendação numa frase.
2. **Projeto e fase** — proposta, consumidor, contexto e decisão herdada.
3. **O que mudou** — factos e evidência desde a última revisão.
4. **Scorecard** — forças, fragilidades e evolução.
5. **Evidência crítica** — resultados que sustentam ou desafiam a direção.
6. **Lacunas e riscos** — o que ainda pode invalidar o projeto.
7. **Plano de aprendizagem** — testes, thresholds, owners e prazo.
8. **Recursos e milestones** — orçamento, equipa e dependências relevantes.
9. **Recomendação** — decisão, condições e data de revisão.

Para cada slide indicar:

```markdown
### Slide X — [título conclusivo]
- **Mensagem principal:** ...
- **Evidência/visual:** ...
- **Fonte:** ...
- **Decisão ou conversa pretendida:** ...
```

Os títulos devem comunicar a conclusão, não apenas o tema.
