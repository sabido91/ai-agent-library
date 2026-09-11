# Playbook MarkItDown

Consultar este ficheiro ao escolher dependências, comandos, API ou método de extração. Confirmar opções com `markitdown --help` na versão instalada.

## Instalação local

O MarkItDown requer Python 3.10 ou superior. Num ambiente Windows PowerShell:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook]"
```

No Prompt de Comando, ativar com:

```cmd
.venv\Scripts\activate.bat
```

Instalar apenas os extras necessários. `markitdown[all]` é apropriado apenas quando vários formatos justificarem as dependências adicionais.

## Conversão CLI

Usar caminhos entre aspas. Os caminhos seguintes são exemplos:

```powershell
markitdown "C:\Documentos\relatorio.docx" -o "C:\Documentos\relatorio.md"
markitdown "C:\Documentos\apresentacao.pptx" -o "C:\Documentos\apresentacao.md"
markitdown "C:\Documentos\benchmark.xlsx" -o "C:\Documentos\benchmark.md"
markitdown "C:\Documentos\relatorio.pdf" -o "C:\Documentos\relatorio.md"
```

Também é possível redirecionar stdout:

```powershell
markitdown "C:\Documentos\relatorio.pdf" > "C:\Documentos\relatorio.md"
```

Não reutilizar estes nomes como se fossem caminhos fornecidos pelo utilizador.

## API Python local

Para inputs locais, preferir a função mais restrita:

```python
from markitdown import MarkItDown

converter = MarkItDown(enable_plugins=False)
result = converter.convert_local("C:/Documentos/relatorio.pdf")
print(result.markdown)
```

Ativar plugins apenas quando tiverem sido identificados, instalados e aprovados. Não presumir endpoints, chaves ou clientes de modelos.

## Escolha por formato

| Formato | Adequado para | Riscos principais | Validação prioritária |
|---|---|---|---|
| DOCX | Relatórios, entrevistas, briefings, listas, tabelas simples | Caixas de texto, diagramas, imagens com texto, tabelas complexas | Hierarquia, caixas de texto e tabelas |
| PPTX | Títulos, bullets, texto editorial, notas disponíveis | Gráficos como imagem, diagramas, builds, texto visual | Ordem dos slides, notas e mensagens visuais |
| XLSX/XLS | Benchmarks, produtos, preços, claims, scorecards | Células fundidas, várias tabelas, fórmulas, pivots, gráficos | Folhas, cabeçalhos, fórmulas, unidades e totais |
| PDF digital | Relatórios, artigos, white papers | Colunas, ordem de leitura, rodapés, fontes e tabelas | Páginas, parágrafos, números e referências |
| PDF scan/imagem | Arquivo visual e texto fotografado | Texto ausente ou incorreto sem OCR | OCR, números, legendas e revisão humana |
| CSV/JSON/XML | Dados tabulares ou estruturados | Encoding, delimitadores, nesting, tipos e campos vazios | Contagens, esquema, encoding e valores nulos |
| HTML | Conteúdo web guardado | Navegação, menus, scripts e texto repetido | Conteúdo principal, links e duplicação |
| MSG | E-mails Outlook e anexos | Cabeçalhos, threads, anexos e confidencialidade | Remetentes, datas, sequência e anexos |
| Áudio | Entrevistas, reuniões e notas faladas | Transcrição, idiomas, nomes e ruído | Oradores, timestamps, citações e consentimento |

## OCR e conteúdo visual

1. Confirmar se o conteúdo essencial está em scans, imagens, gráficos ou diagramas.
2. Explicar que a conversão normal pode não o recuperar.
3. Preferir OCR local quando a confidencialidade for prioritária.
4. Pedir autorização antes de usar serviços cloud ou modelos externos.
5. Marcar no output o conteúdo proveniente de OCR ou interpretação visual.
6. Validar manualmente números, tabelas, citações, ingredientes, valores nutricionais, preços, claims e resultados de investigação.

Não apresentar OCR ou descrição visual como totalmente fiável.

## Resolução de problemas

- **Formato não reconhecido:** confirmar extensão, integridade do ficheiro, extra instalado e formatos suportados pela versão local.
- **Saída vazia ou curta:** verificar se é scan, se o texto está embebido em imagens ou se existem permissões/proteções.
- **Ordem incorreta:** comparar por página/slide/secção e reconstruir apenas com evidência da fonte.
- **Tabela deformada:** exportar a tabela separadamente ou rever a folha original; preservar cabeçalhos e unidades.
- **Caracteres incorretos:** verificar encoding e idioma, sobretudo em CSV, HTML, XML e texto.
- **Conteúdo confidencial:** manter processamento local e impedir acesso remoto até existir autorização.

## Referência oficial

- Repositório e documentação: <https://github.com/microsoft/markitdown>
- Metadata do pacote e extras: <https://github.com/microsoft/markitdown/blob/main/packages/markitdown/pyproject.toml>

Estas ligações servem para verificar capacidades atuais; não implicam uma integração automática.
