# forest

Utilities for working with Forest version numbers.

## Usage

```python
from forest import ForestVersion, parse_version, latest_version

release = parse_version("Cedar", "1.2.3")
print(release.identifier)  # Cedar 1.2.3
print(release.bump_patch().identifier)  # Cedar 1.2.4

versions = [
    release,
    ForestVersion("Cedar", 1, 4, 0),
    ForestVersion("Cedar", 2, 0, 0),
]
print(latest_version(versions).identifier)  # Cedar 2.0.0
```

Run the test suite with:

```bash
pytest
```
