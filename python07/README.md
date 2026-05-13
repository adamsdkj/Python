*This project has been created as part of the 42 curriculum by adadra.*

## Description

Module 07 explores **Object-Oriented Programming (OOP)** design patterns in Python through a fantasy card game called **DataDeck**. The goal is to practice abstract base classes (ABCs), inheritance, polymorphism, multiple interfaces, the Abstract Factory pattern, the Strategy pattern, and tournament ranking systems.

Each exercise builds on the previous one:

- **ex0** – Defines the `Card` abstract base class and a `CreatureCard` implementation.
- **ex1** – Adds `SpellCard`, `ArtifactCard`, and a `Deck` manager demonstrating polymorphism.
- **ex2** – Introduces `Combatable` and `Magical` interfaces with an `EliteCard` using multiple inheritance.
- **ex3** – Implements the Abstract Factory (`CardFactory` / `FantasyCardFactory`) and Strategy (`GameStrategy` / `AggressiveStrategy`) patterns with a `GameEngine`.
- **ex4** – Adds a `Rankable` interface, `TournamentCard`, and `TournamentPlatform` for an Elo-style ranking system.

## Instructions

All exercises are designed to be run from the `module07/` directory.

```bash
# ex0 – Card Foundation
cd ex0 && python main.py

# ex1 – Deck Builder (run from module07 root)
cd .. && python -m ex1.main

# ex2 – Ability System
python -m ex2.main

# ex3 – Game Engine
python -m ex3.main

# ex4 – Tournament Platform
python -m ex4.main
```

### Requirements

- Python 3.10+
- No external dependencies (standard library only)

### Linting

```bash
flake8
```

## Resources

- [Python ABC documentation](https://docs.python.org/3/library/abc.html)
- [PEP 3119 – Introducing Abstract Base Classes](https://peps.python.org/pep-3119/)
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) (Gang of Four)
- [Real Python – Abstract Classes](https://realpython.com/python-interface/)
- [Factory Method & Abstract Factory Patterns](https://refactoring.guru/design-patterns/abstract-factory/python/example)

### AI Usage

AI (GitHub Copilot) was used to assist with:

- Ensuring flake8 compliance across all source files.
- Adding type hints and docstrings to all functions and methods.
