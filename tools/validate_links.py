import re
from pathlib import Path

from common import (
    LINK_VALIDATION_EXCLUDED_DIRS,
    ROOT_DIR,
    iter_markdown_files,
    print_error,
    print_ok,
    relative_path,
)


LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def is_external_link(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:"))


def is_anchor_link(target: str) -> bool:
    return target.startswith("#")


def clean_target(target: str) -> str:
    return target.split("#")[0].strip()


def validate_links():
    errors = 0
    checked_links = 0

  
    for path in iter_markdown_files():

        content = path.read_text(encoding="utf-8")
    
        relative = relative_path(path)

        if any(
            relative == directory or relative.startswith(f"{directory}/")
            for directory in LINK_VALIDATION_EXCLUDED_DIRS
        ):
            continue

        for match in LINK_PATTERN.finditer(content):
            raw_target = match.group(1).strip()

            if (
                not raw_target
                or is_external_link(raw_target)
                or is_anchor_link(raw_target)
            ):
                continue

            target = clean_target(raw_target)

            if not target:
                continue

            checked_links += 1

            target_path = (path.parent / target).resolve()

            try:
                target_path.relative_to(ROOT_DIR)
            except ValueError:
                print_error(path, f"Enlace fuera del repositorio: {raw_target}")
                errors += 1
                continue

            if not target_path.exists():
                print_error(path, f"Enlace interno roto: {raw_target}")
                errors += 1

    if errors:
        print(f"\nValidación finalizada con {errors} enlace(s) roto(s).")
        return 1

    print_ok(f"{checked_links} enlace(s) interno(s) verificados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate_links())