# Contributing

Thanks for taking the time to contribute! Here's how to work with this repo.

## Getting set up

​```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
​```

## Branch naming

Use a short, descriptive branch name prefixed by type:

​```
feature/short-description
fix/short-description
docs/short-description
chore/short-description
refactor/short-description
​```

Example: `feature/user-authentication`, `fix/null-pointer-on-login`

## Commit messages (Conventional Commits)

We follow [Conventional Commits](https://www.conventionalcommits.org/):

​```
<type>(<optional scope>): <short summary>

<optional body>

<optional footer>
​```

**Types:**

| Type       | Use for                                              |
|------------|-------------------------------------------------------|
| `feat`     | A new feature                                          |
| `fix`      | A bug fix                                              |
| `docs`     | Documentation only changes                             |
| `style`    | Formatting, missing semicolons, no code change         |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf`     | Performance improvement                                |
| `test`     | Adding or correcting tests                             |
| `build`    | Build system or dependency changes                     |
| `ci`       | CI configuration changes                                |
| `chore`    | Other changes that don't modify src or test files      |

**Examples:**

​```
feat(auth): add JWT-based login endpoint
fix(parser): handle empty input without crashing
docs(readme): clarify installation steps
test(main): add coverage for edge cases in greet()
​```

Rules of thumb:
- Use the imperative mood ("add", not "added" or "adds")
- Keep the summary line under 72 characters
- Reference issues in the footer, e.g. `Closes #42`

## Pull requests

1. Fork the repo and create your branch from `main`.
2. Make your changes, with tests for any new behavior.
3. Ensure `pytest`, `ruff check .`, and `mypy src` all pass.
4. Fill out the PR template completely.
5. Request review. A maintainer will merge once approved and CI is green.

## Code style

- Formatting/linting is handled by `ruff`.
- Type hints are required on public functions; checked with `mypy`.
- Write a docstring for any non-trivial function, class, or module.

## Reporting bugs / requesting features

Please use the issue templates under `.github/ISSUE_TEMPLATE/`.