from validate_frontmatter import validate_frontmatter
from validate_ids import validate_ids
from validate_links import validate_links


VALIDATIONS = [
    ("Front Matter", validate_frontmatter),
    ("Identificadores únicos", validate_ids),
    ("Enlaces internos", validate_links),
]


def main():
    errors = 0

    print()
    print("NovaCoquinaria - Validación")
    print("---------------------------")

    for name, validation in VALIDATIONS:
        print()
        print(f"== {name} ==")
        result = validation()

        if result != 0:
            errors += 1

    print()
    print("---------------------------")

    if errors:
        print(f"Estado: ERROR ({errors} validación/es fallida/s)")
        return 1

    print("Estado: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())