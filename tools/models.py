from dataclasses import dataclass
from pathlib import Path


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