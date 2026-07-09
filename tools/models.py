from dataclasses import dataclass
from pathlib import Path
import re

LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
@dataclass(slots=True)
class Document:
    """
    Representa un documento Markdown del SGCC.
    """


    path: Path
    frontmatter: dict
    content: str

    @property
    def id(self) -> str | None:
        return self.frontmatter.get("id")

    @property
    def tipo(self) -> str | None:
        return self.frontmatter.get("tipo")

    @property
    def titulo(self) -> str | None:
        return self.frontmatter.get("titulo")

    @property
    def version(self) -> str | None:
        return self.frontmatter.get("version")

    @property
    def ultima_revision(self) -> str | None:
        return self.frontmatter.get("ultima_revision")
    
    @property
    def filename(self) -> str:
        return self.path.name

    @property
    def directory(self) -> str:
        return self.path.parent.name

    @property
    def relative_path(self) -> str:
        return self.path.as_posix()

    @property
    def links(self) -> list[str]:
        """
        Devuelve todos los enlaces Markdown del documento.
        """

        links = []

        for match in LINK_PATTERN.finditer(self.content):
            target = match.group(1).split("#")[0].strip()

            if (
                target
                and not target.startswith("http")
                and not target.startswith("mailto:")
            ):
                links.append(target)

        return links