# Testing Guidelines

## Structure

- Mirror `src/` structure exactly.
- Use `test_*.py` naming.
- No `__init__.py` in test directories.
- One test class per source class when classes are used.

## Fixtures

- Shared fixtures live in `tests/conftest.py`.
- Domain-specific fixtures live in nested `conftest.py` files, co-located
  with the tests that use them.
- Prefer pytest fixtures over setup/teardown methods.

## Naming

Descriptive test names in the form:

```
test_should_<verb>_when_<condition>
```

e.g. `test_should_raise_error_when_input_is_negative`.

## Coverage & quality

- Target: >85% branch coverage.
- Test both success and failure paths.
- Prefer one assertion per behavior, not per test.

## Running

```bash
uv run pytest                            # all tests + coverage
uv run pytest tests/<subpkg>/            # subset
uv run pytest --cov-report=html          # html coverage report
```
