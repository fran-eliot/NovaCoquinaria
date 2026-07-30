from common import (
    ADR_DIR,
    extract_frontmatter,
    iter_markdown_files,
    print_error,
    print_ok,
    relative_path,
    requires_frontmatter,
)


REQUIRED_FIELDS = {
    "id",
    "tipo",
    "titulo",
    "version",
    "ultima_revision",
}


def is_adr(relative_path: str) -> bool:
    return (
        relative_path == ADR_DIR
        or relative_path.startswith(f"{ADR_DIR}/")
    )


def validate_frontmatter():
    errors = 0
    checked = 0

    for path in iter_markdown_files():
        checked += 1

        try:
            frontmatter = extract_frontmatter(path)
        except ValueError as exc:
            print_error(path, str(exc))
            errors += 1
            continue

        if frontmatter is None:
            if requires_frontmatter(path):
                print_error(path, "Front Matter ausente")
                errors += 1
            continue

        relative = relative_path(path)

        if is_adr(relative):
            # Los ADR utilizan un esquema propio de Front Matter.
            continue

        missing_fields = REQUIRED_FIELDS - set(frontmatter.keys())

        for field in sorted(missing_fields):
            print_error(path, f"Campo obligatorio ausente: {field}")
            errors += 1

    if errors:
        print(f"\nValidación finalizada con {errors} error(es) en {checked} documento(s).")
        return 1

    print_ok(f"Front Matter válido en {checked} documento(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate_frontmatter())