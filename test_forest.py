import pytest

from forest import ForestVersion, latest_version, parse_version


def test_parse_version_valid():
    version = parse_version("Cedar", "1.2.3")
    assert version.name == "Cedar"
    assert version.major == 1
    assert version.minor == 2
    assert version.patch == 3
    assert version.identifier == "Cedar 1.2.3"


def test_parse_version_invalid_format():
    with pytest.raises(ValueError):
        parse_version("Cedar", "1.2")


def test_parse_version_non_numeric():
    with pytest.raises(ValueError):
        parse_version("Cedar", "1.two.3")


def test_version_bumps():
    version = ForestVersion("Cedar", 1, 0, 0)
    assert version.bump_patch().identifier == "Cedar 1.0.1"
    assert version.bump_minor().identifier == "Cedar 1.1.0"
    assert version.bump_major().identifier == "Cedar 2.0.0"


def test_latest_version():
    versions = [
        ForestVersion("Cedar", 1, 0, 0),
        ForestVersion("Cedar", 1, 2, 0),
        ForestVersion("Cedar", 1, 2, 5),
    ]
    assert latest_version(versions).identifier == "Cedar 1.2.5"


def test_latest_version_empty():
    with pytest.raises(ValueError):
        latest_version([])


def test_negative_components_rejected():
    with pytest.raises(ValueError):
        ForestVersion("Cedar", -1, 0, 0)
