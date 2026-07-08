from common import (
    extract_frontmatter,
    iter_markdown_files,
    print_error,
    print_ok,
)


REQUIRED_FIELDS = {
    "id",
    "tipo",
    "titulo",
    "version",
    "ultima_revision",
}


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
            print_error(path, "Front Matter ausente")
            errors += 1
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