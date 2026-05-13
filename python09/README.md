*This project has been created as part of the 42 curriculum by adadra.*

## Description

Module 09 explores **data validation with Pydantic**, a powerful library for defining data models with automatic type checking and custom validation rules. The exercises use a space-themed scenario to practice model constraints, custom validators, and nested model validation.

Each exercise covers a different level of complexity:

- **ex0** – Defines a `SpaceStation` Pydantic model with field constraints (min/max length, numeric ranges) and demonstrates both valid and invalid data creation.
- **ex1** – Builds an `AlienContact` model with enum-based contact types and custom `model_validator` rules (e.g., physical contacts must be verified, telepathic contacts need 3+ witnesses).
- **ex2** – Creates nested models (`CrewMember` and `SpaceMission`) with cross-field validation to ensure mission rules (e.g., crew must include a Captain or Commander, long missions require experienced crew).

## Instructions

### Requirements

- Python 3.12+
- `pydantic` (v2+)

```bash
pip install pydantic
```

### Running

```bash
# ex0 – Space Station validation
cd ex0 && python space_station.py

# ex1 – Alien Contact validation
cd ../ex1 && python alien_contact.py

# ex2 – Space Crew / Mission validation
cd ../ex2 && python space_crew.py
```

### Linting

```bash
flake8 --max-line-length=79 --exclude=__pycache__ .
```

## Resources

- [Pydantic v2 documentation](https://docs.pydantic.dev/latest/)
- [Pydantic Field validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
- [Python Enum documentation](https://docs.python.org/3/library/enum.html)

### AI Usage

AI (GitHub Copilot) was used to assist with:

- Ensuring flake8 compliance across all source files.
- Adding type hints and docstrings to all functions and methods.
