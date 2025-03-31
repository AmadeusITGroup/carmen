# python-project-starter

This is a template repo to act as a reference when starting up a new project in python. It consolidates best practices in regards to minimal level of documentation as well as the CI aspects.

Local installation can be done using [`uv`](https://github.com/astral-sh/uv):

```bash
$ uv venv -p python3.11
$ uv pip install -e .
$ source .venv/bin/activate
$ python
>>> from package import square
>>> square(3)
9
```

After installation a command-line tool is also available:

```bash
$ square 4
Square of 4 is 16
```

Running the tests can be done using [`tox`](https://tox.wiki/):

```bash
$ tox -p
```

Building the packages can also be done using `tox`:

```bash
$ tox -e packages
$ ls dist/
```

Packaging uses [`setuptools-scm`](https://github.com/pypa/setuptools-scm), so the version of the software is based on git tags.

To run the linting, we recommend `ruff`, a standard configuration is in the repo in `pyproject.toml`.

# Pre-commit Hooks

This project uses [`pre-commit`](https://pre-commit.com/) to ensure code quality and consistency before committing changes. Pre-commit hooks automatically run checks such as linting and formatting on staged files.

## Setting up Pre-commit Hooks

To set up pre-commit hooks for this repository, follow these steps:

1. Install `pre-commit` if you haven't already:

```bash
   pip install pre-commit
```

2. Install the pre-commit hooks defined in the `.pre-commit-config.yaml` file:

```bash
pre-commit install
```

3. You can manually run the pre-commit hooks on all files in the repository using:

```bash
pre-commit run --all-files
```

## How it Works
Once installed, the pre-commit hooks will automatically run on staged files whenever you attempt to make a commit. If any of the hooks fail, the commit will be blocked until the issues are resolved.

## Updating Hooks
To update the pre-commit hooks to their latest versions, run:
```bash
pre-commit autoupdate
```
## Available Hooks

Some examples of the pre-commit:

- **black**: Automatically formats Python code to conform to the Black code style.
- **isort**: Sorts imports in Python files according to PEP 8 guidelines.
- **flake8**: Checks Python code for style guide enforcement.
- **mypy**: Performs static type checking on Python code.
- **ruff**: A fast Python linter and code quality tool.
- **bandit**: A security linter for Python code.
- **check-yaml**: Validates YAML files for syntax errors.
- **check-added-large-files**: Prevents large files from being added to the repository.
- **check-merge-conflict**: Checks for merge conflict markers in files.
- **end-of-file-fixer**: Ensures that files end with a newline character.
- **trailing-whitespace**: Removes trailing whitespace from lines in files.
- **detect-private-key**: Detects private keys in files to prevent accidental exposure.
- **check-json**: Validates JSON files for syntax errors.
- **check-ast**: Checks Python files for syntax errors and other issues.
- **check-toml**: Validates TOML files for syntax errors.
- **check-merge-conflict**: Checks for merge conflict markers in files.
- **check-symlinks**: Checks for broken symbolic links in the repository.
- **check-xml**: Validates XML files for syntax errors.
- **check-docs**: Checks for documentation issues in Python files.
- **check-urls**: Checks for broken URLs in files.
- **check-binary-files**: Checks for binary files in the repository.
- **check-merge-conflict**: Checks for merge conflict markers in files.

.. and many more!

## Disabling Hooks Temporarily
If you need to skip the pre-commit hooks for a specific commit, you can use the --no-verify flag:

## Configuration
The hooks are configured in the .pre-commit-config.yaml file located in the root of the repository. You can customize the hooks as needed by editing this file. For more information, refer to the pre-commit documentation.



# Releasing
To release a new version of the package, you can create a pre-release from the main branch using GitHub UI, which will then trigger the release workflow. Alternatively, you can use the `gh` command line tool to create a release:

```bash
gh release create v[a.b.c] --prerelease --title "Kick starting the release"  --target main
```

# Contributing
We welcome contributions to this project! If you have an idea for a new feature, bug fix, or improvement, please open an issue or submit a pull request. Before contributing, please read our [contributing guidelines](./CONTRIBUTING.md).