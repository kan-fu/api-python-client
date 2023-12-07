# Contributing

All contributions are welcome! We value and appreciate any feedback. Credits will be given in the changelog file.

## Types of Contributions

### Report Bugs

Bugs can come from Oceans 3.0 API (backend) or the onc library. When reporting an issue, please include some descriptions (code snippet, expected behavior, actual behavior, etc.) to help us reproduce the bug.

Bugs from the backend can also be reported at [Oceans 3.0 Data Portal](https://data.oceannetworks.ca/DataPreview) from the request support form located in the top-right corner.

### Fix Bugs / Implement Features

These are issues labeled with "bug" / "enhancement". Any issue that has no assignee is open to whoever wants to implement it.

### Write Documentation

Documentations are important for users to understand the library. You are welcome to raise an issue if you find something that is outdated or can be improved.

For docstring, [numpy style](https://numpydoc.readthedocs.io/en/latest/format.html) is used.

### Commit

We use [conventional commits](https://www.conventionalcommits.org/) for commit messages. Most of the time it is as simple as adding a type before the message.

The general format is as follows:

```text
<type>[optional scope]: short description

[optional body: long description]

[optional footer]
```

Types can be _fix, feat (short for feature), refactor, style, docs, test, etc_. Some examples are:

```text
feat: allow users to cancel a running data product

test: add tests for cancelling a running data product

docs: add docstrings for discovery methods
```

Check [py-pkgs open source book](https://py-pkgs.org/07-releasing-versioning#automatic-version-bumping) for an introduction.

---

## Set up a development environment

Here is a setup for the local development.

### Creating a virtual environment

Make sure the python version meets the minimum version requirement defined in pyproject.toml. This step can be simplified if you are using [VS Code](https://code.visualstudio.com/docs/python/environments) or [PyCharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env).

```shell
# Create a virtual environment
$ python -m venv .venv

# Activate the venv
$ source .venv/bin/activate
# For Windows, use .venv\Scripts\activate.ps1 for powershell or .venv\Scripts\activate.bat for cmd.exe

# Install onc library in editable mode
$ pip install -e .

# Install dependencies (TODO: Change it to use pyproject optional dependencies)
$ pip install -r requirements-dev.txt
```

### Running the test

See README.md in the tests folder.

Or use tox

```shell
$ tox -e py310 # py38, py39, py311, py312. Make sure the specified python version is installed.
```

### Formatter

Code is formatted using [black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/).

```shell
$ black onc tests
$ isort onc tests
```

Or use tox

```shell
$ tox -e format
```

### Linter

[Ruff](https://docs.astral.sh/ruff/) is used for linting.

```shell
$ ruff check onc
```

Or use tox

```shell
$ tox -e lint
```

## Set up a development environment for documentation

WIP.
