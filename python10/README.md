*This project has been created as part of the 42 curriculum by adadra.*

## Description

Module 10 dives into **functional programming in Python**, covering lambda expressions, higher-order functions, closures, scope, `functools` utilities, and decorators. The exercises use a magical theme to make functional programming concepts engaging.

Each exercise focuses on a specific functional programming topic:

- **ex0 – Lambda Spells** – Practices `lambda`, `sorted()`, `filter()`, and `map()` for artifact sorting, mage filtering, spell transformation, and statistics.
- **ex1 – Higher Magic** – Implements higher-order functions: `spell_combiner`, `power_amplifier`, `conditional_caster`, and `spell_sequence` that compose and transform functions.
- **ex2 – Scope Mysteries** – Explores closures and `nonlocal` with a `mage_counter`, `spell_accumulator`, `enchantment_factory`, and `memory_vault`.
- **ex3 – Functools Artifacts** – Uses `functools.reduce`, `functools.partial`, `functools.lru_cache`, and `functools.singledispatch` for spell reduction, partial enchantments, memoized Fibonacci, and type-based dispatch.
- **ex4 – Decorator Mastery** – Builds custom decorators: `spell_timer` (timing), `power_validator` (argument validation), `retry_spell` (retry logic), and a `MageGuild` class with `@staticmethod`.

## Instructions

### Requirements

- Python 3.10+
- No external dependencies (standard library only)

### Running

```bash
# ex0 – Lambda Spells
cd ex0 && python lambda_spells.py

# ex1 – Higher-Order Functions
cd ../ex1 && python higher_magic.py

# ex2 – Closures and Scope
cd ../ex2 && python scope_mysteries.py

# ex3 – Functools Utilities
cd ../ex3 && python functools_artifacts.py

# ex4 – Decorators
cd ../ex4 && python decorator_mastery.py
```

### Linting

```bash
flake8 --max-line-length=79 --exclude=__pycache__ .
```

## Resources

- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [functools documentation](https://docs.python.org/3/library/functools.html)
- [PEP 318 – Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
- [Real Python – Closures](https://realpython.com/python-closure/)
- [Real Python – Decorators](https://realpython.com/primer-on-python-decorators/)

### AI Usage

AI (GitHub Copilot) was used to assist with:

- Ensuring flake8 compliance across all source files.
- Adding type hints and docstrings to all functions and methods.
