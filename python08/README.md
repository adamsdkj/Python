*This project has been created as part of the 42 curriculum by adadra.*

## Description

Module 08 focuses on **Python packaging, virtual environments, and dependency management**. The goal is to understand how to isolate project dependencies, manage packages with pip and Poetry, and load configuration from environment variables.

Each exercise covers a different aspect:

- **ex0** – Demonstrates virtual environment creation and activation using `venv`. The `construct.py` script checks whether you are running inside a virtual environment.
- **ex1** – Showcases dependency management with `pip` (via `requirements.txt`) and Poetry (via `pyproject.toml`). The `loading.py` script verifies that `pandas`, `numpy`, `matplotlib`, and `requests` are installed and functional.
- **ex2** – Uses `python-dotenv` to load configuration from `.env` files. The `oracle.py` script demonstrates environment-based configuration with validation and security checks.

## Instructions

### ex0 – Virtual Environment

```bash
cd ex0
python -m venv matrix_env
source matrix_env/bin/activate
python construct.py
```

### ex1 – Dependency Management

```bash
cd ex1

# Using pip
pip install -r requirements.txt
python loading.py

# Or using Poetry
poetry install
python loading.py
```

### ex2 – Environment Configuration

```bash
cd ex2
# Create a .env.example file with required variables:
# MATRIX_MODE, DATABASE_URL, API_KEY, LOG_LEVEL, ZION_ENDPOINT
pip install python-dotenv
python oracle.py
```

### Linting

```bash
flake8 --max-line-length=79 --exclude=__pycache__,matrix_env .
```

## Resources

- [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [pip documentation](https://pip.pypa.io/en/stable/)
- [Poetry documentation](https://python-poetry.org/docs/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [12-Factor App – Config](https://12factor.net/config)

### AI Usage

AI (GitHub Copilot) was used to assist with:

- Ensuring flake8 compliance across all source files.
- Adding type hints and docstrings to all functions and methods.
