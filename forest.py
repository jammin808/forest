"""Utilities for working with Forest version numbers."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class ForestVersion:
    """A semantic version representation for Forest releases."""

    name: str
    major: int
    minor: int
    patch: int

    def __post_init__(self) -> None:
        if any(number < 0 for number in (self.major, self.minor, self.patch)):
            raise ValueError("Version components cannot be negative")

    @property
    def identifier(self) -> str:
        """Return a human-friendly identifier like ``Forest 1.2.3``."""

        return f"{self.name} {self.major}.{self.minor}.{self.patch}"

    def bump_patch(self) -> "ForestVersion":
        """Return a new instance with the patch number incremented."""

        return ForestVersion(self.name, self.major, self.minor, self.patch + 1)

    def bump_minor(self) -> "ForestVersion":
        """Return a new instance with the minor number incremented and patch reset."""

        return ForestVersion(self.name, self.major, self.minor + 1, 0)

    def bump_major(self) -> "ForestVersion":
        """Return a new instance with the major number incremented and minor/patch reset."""

        return ForestVersion(self.name, self.major + 1, 0, 0)


def parse_version(name: str, version: str) -> ForestVersion:
    """Create a :class:`ForestVersion` from a dotted version string.

    Args:
        name: Release train or product name.
        version: Dotted semantic version string (``MAJOR.MINOR.PATCH``).

    Raises:
        ValueError: If the version string cannot be parsed or contains negative parts.
    """

    parts = version.split(".")
    if len(parts) != 3:
        raise ValueError("Version must have three components")

    try:
        major, minor, patch = (int(part) for part in parts)
    except ValueError as exc:  # pragma: no cover - explicit message below
        raise ValueError("Version components must be integers") from exc

    return ForestVersion(name, major, minor, patch)


def latest_version(versions: Iterable[ForestVersion]) -> ForestVersion:
    """Return the latest version by comparing major, minor, then patch numbers."""

    version_list: List[ForestVersion] = list(versions)
    if not version_list:
        raise ValueError("No versions provided")

    return max(
        version_list,
        key=lambda v: (v.major, v.minor, v.patch),
    )
