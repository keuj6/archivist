# archivist — project instructions

This project defers to `~/.claude/CLAUDE.md` for all global rules (tooling,
code style, scope discipline, commits, testing). Only project-specific
additions live here.

## Package name

The package is named `archivist` as a placeholder. When forking this template,
rename:

- `src/archivist/` → `src/<your_package>/`
- All `archivist` references in `pyproject.toml`, `README.md`, and this file.

## Test layout

- `tests/` mirrors `src/<package>/` structure exactly.
- Test files are prefixed `test_` (e.g. `src/pkg/core/foo.py` →
  `tests/core/test_foo.py`).
- No `__init__.py` in `tests/`.
- See `tests/CLAUDE.md` for detailed testing conventions.

## Strict Red/Green TDD

This project follows strict Red/Green TDD:

1. **Red** — write a failing test for the next behavior. Run it; observe
   it fail. A test that has never been red is not trusted.
2. **Green** — write the minimum production code to make the test pass.
3. **Refactor** — only on green. Never mix refactoring with making a test
   pass.

Rules:
- Never write production code without a failing test that requires it.
- One failing test at a time.
- Bug fixes start by reproducing the bug as a failing test.

## Daily commands

```bash
uv sync                           # install / update deps
uv run pytest                     # tests + branch coverage
uv run ruff check .               # lint
uv run ruff format .              # format
uv run ty check                   # type check (strict)
uv run pre-commit run --all-files # full hook suite
```
