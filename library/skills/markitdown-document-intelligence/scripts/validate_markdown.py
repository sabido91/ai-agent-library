#!/usr/bin/env python3
"""Pré-validar Markdown convertido sem alterar ficheiros.

Uso:
    python scripts/validate_markdown.py documento.md
    python scripts/validate_markdown.py documento.md --profile knowledge --json

Exit codes: 0 sem erros; 1 com erros de validação; 2 erro de utilização/leitura.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


KNOWLEDGE_FIELDS = {
    "title",
    "conversion_date",
    "source_file",
    "source_format",
    "confidentiality",
    "processing_method",
    "quality_status",
}
ALLOWED_CONFIDENTIALITY = {"public", "internal", "confidential", "restricted"}
ALLOWED_QUALITY = {"draft", "reviewed", "validated"}


def extract_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, lines
    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {"__unclosed__": "true"}, lines

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if match:
            fields[match.group(1)] = (match.group(2) or "").strip().strip('"\'')
    return fields, lines[end + 1 :]


def validate(path: Path, profile: str) -> dict[str, object]:
    text = path.read_text(encoding="utf-8-sig")
    errors: list[str] = []
    warnings: list[str] = []

    if not text.strip():
        errors.append("O ficheiro está vazio.")
        return {"file": str(path), "profile": profile, "errors": errors, "warnings": warnings}

    fields, body_lines = extract_frontmatter(text)
    body = "\n".join(body_lines).strip()
    if fields.get("__unclosed__"):
        errors.append("O frontmatter começa com '---' mas não tem delimitador de fecho.")
        fields = {}
    if not body:
        errors.append("Não existe conteúdo Markdown depois do frontmatter.")

    headings = [line for line in body_lines if re.match(r"^#{1,6}\s+\S", line)]
    if not headings:
        warnings.append("Não foram encontrados títulos Markdown.")
    else:
        levels = [len(re.match(r"^(#+)", line).group(1)) for line in headings]
        for previous, current in zip(levels, levels[1:]):
            if current > previous + 1:
                warnings.append(
                    f"A hierarquia de títulos salta de H{previous} para H{current}."
                )
                break

    table_rows = [line for line in body_lines if line.lstrip().startswith("|")]
    for number, line in enumerate(body_lines, start=1):
        if line.lstrip().startswith("|") and line.count("|") < 2:
            warnings.append(f"Possível linha de tabela incompleta na linha {number}.")
    if table_rows and not any(re.match(r"^\s*\|?\s*:?-{3,}", line) for line in table_rows):
        warnings.append("Existem linhas de tabela, mas não foi detetado um separador de cabeçalho.")

    if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", body, flags=re.IGNORECASE):
        warnings.append("Foram encontrados marcadores de conteúdo por completar.")

    if profile == "knowledge":
        if not fields:
            errors.append("O perfil knowledge exige frontmatter YAML.")
        else:
            missing = sorted(field for field in KNOWLEDGE_FIELDS if not fields.get(field))
            if missing:
                errors.append("Metadados obrigatórios em falta: " + ", ".join(missing) + ".")
            confidentiality = fields.get("confidentiality")
            if confidentiality and confidentiality not in ALLOWED_CONFIDENTIALITY:
                errors.append("Valor de confidentiality não reconhecido.")
            quality = fields.get("quality_status")
            if quality and quality not in ALLOWED_QUALITY:
                errors.append("Valor de quality_status não reconhecido.")

    return {
        "file": str(path),
        "profile": profile,
        "errors": errors,
        "warnings": warnings,
        "summary": {
            "characters": len(text),
            "headings": len(headings),
            "table_rows": len(table_rows),
            "frontmatter_fields": len(fields),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Pré-validar estrutura de Markdown convertido.")
    parser.add_argument("file", type=Path, help="Ficheiro .md a validar")
    parser.add_argument(
        "--profile", choices=("basic", "knowledge"), default="basic",
        help="knowledge exige metadados mínimos para base documental",
    )
    parser.add_argument("--json", action="store_true", help="Emitir resultado em JSON")
    args = parser.parse_args()

    if not args.file.is_file():
        print(f"Erro: ficheiro não encontrado: {args.file}", file=sys.stderr)
        return 2
    if args.file.suffix.lower() != ".md":
        print("Erro: o input deve ter extensão .md", file=sys.stderr)
        return 2

    try:
        result = validate(args.file, args.profile)
    except (OSError, UnicodeError) as exc:
        print(f"Erro ao ler o ficheiro: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Ficheiro: {result['file']}")
        print(f"Perfil: {result['profile']}")
        for error in result["errors"]:
            print(f"ERRO: {error}")
        for warning in result["warnings"]:
            print(f"AVISO: {warning}")
        if not result["errors"] and not result["warnings"]:
            print("OK: sem problemas estruturais detetados.")
        print("Nota: esta verificação não compara o Markdown com o documento original.")

    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
