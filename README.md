# archivist

Opinionated minimal Python project template.

## Stack

- **[uv](https://docs.astral.sh/uv/)** — package & environment management
- **[ruff](https://docs.astral.sh/ruff/)** — lint + format (strict ruleset)
- **[ty](https://github.com/astral-sh/ty)** — type checker (strict, preview)
- **pytest + pytest-cov** — tests with branch coverage
- **pre-commit** — local hooks (ruff, ty, pytest on push)
- **hatchling** — build backend
- Python **3.12+**, `src/` layout, `tests/` mirrors `src/`

## Use as a GitHub template

Click **Use this template → Create a new repository** on the `archivist`
GitHub page, then clone your new repo and follow *Rename the package* below.

## Use via clone + rename

```bash
git clone https://github.com/<your-user>/archivist.git <new-project>
cd <new-project>
rm -rf .git
git init -b main
```

### Rename the package

Replace `archivist` with your new package name (use snake_case, no dashes):

```bash
NEW=<new_package>
mv src/archivist src/$NEW
# macOS sed
sed -i '' "s/archivist/$NEW/g" pyproject.toml README.md CLAUDE.md tests/core/test_example.py
```

### Install, verify, commit

```bash
uv sync
uv run pre-commit install
uv run pytest
uv run ruff check .
uv run ty check
git add .
git commit -m "chore: initial commit from archivist template"
```

### Push to a fresh GitHub repo

With the GitHub CLI:

```bash
gh repo create <new-project> --private --source=. --remote=origin --push
```

Or manually:

```bash
git remote add origin git@github.com:<your-user>/<new-project>.git
git push -u origin main
```

## Daily commands

```bash
uv sync                            # install / update deps
uv run pytest                      # tests + branch coverage
uv run ruff check .                # lint
uv run ruff format .               # format
uv run ty check                    # type check
uv run pre-commit run --all-files  # full hook suite
```

## Layout

```
archivist/
├── pyproject.toml
├── .pre-commit-config.yaml
├── .gitignore
├── README.md
├── CLAUDE.md
├── src/
│   └── archivist/
│       ├── __init__.py
│       └── core/
│           ├── __init__.py
│           └── example.py
└── tests/
    ├── CLAUDE.md
    ├── conftest.py
    └── core/
        └── test_example.py
```

## Conventions

See `CLAUDE.md` for project-level conventions and `tests/CLAUDE.md` for
testing guidelines. Both defer to `~/.claude/CLAUDE.md` for global rules.
