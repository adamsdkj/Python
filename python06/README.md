*This project has been created as part of the 42 curriculum by adadra.*

# Module 06 - Python Import Alchemy

This project demonstrates Python import mechanics using a fantasy-themed package named `alchemy`.

## Requirements

- Python 3.10+ (works with `python3`)
- Run commands from the project root:
  - `/sgoinfre/adadra/core/python/module06`

## Project Structure

```text
module06/
├── alchemy/
│   ├── __init__.py
│   ├── elements.py
│   ├── potions.py
│   ├── transmutation/
│   │   ├── __init__.py
│   │   ├── basic.py
│   │   └── advanced.py
│   └── grimoire/
│       ├── __init__.py
│       ├── validator.py
│       └── spellbook.py
├── ft_sacred_scroll.py
├── ft_import_transmutation.py
├── ft_pathway_debate.py
└── ft_circular_curse.py
```

## What Each Script Teaches

### `ft_sacred_scroll.py`

- Package exports through `alchemy/__init__.py`
- Difference between direct module access and package-level exposed symbols
- Reading package metadata (`__verion__`, `__author__`)

Run:

```bash
python3 ft_sacred_scroll.py
```

### `ft_import_transmutation.py`

- Full module import (`import alchemy.elements`)
- Specific symbol import (`from ... import ...`)
- Aliased import (`as`)
- Multiple imports in one line

Run:

```bash
python3 ft_import_transmutation.py
```

### `ft_pathway_debate.py`

- Absolute imports (example in `alchemy/transmutation/basic.py`)
- Relative imports (example in `alchemy/transmutation/advanced.py`)
- Accessing subpackage functions via package namespace

Run:

```bash
python3 ft_pathway_debate.py
```

### `ft_circular_curse.py`

- Circular dependency avoidance with **late import**
- Ingredient validation and spell recording flow:
  - `validate_ingredients(...)`
  - `record_spell(...)`
- Formatted success/failure responses for spell registration

Run:

```bash
python3 ft_circular_curse.py
```

## Key Package Notes

- `alchemy/__init__.py` controls top-level package exposure (`create_fire`, `create_water`, and `transmutation`).
- `alchemy/grimoire/spellbook.py` performs a local import inside `record_spell`:
  - `from . import validator as v`
- That local import is a classic late-import pattern to reduce circular import risk.

## Quick Run (All Exercises)

```bash
python3 ft_sacred_scroll.py
python3 ft_import_transmutation.py
python3 ft_pathway_debate.py
python3 ft_circular_curse.py
```

## Learning Goals Covered

- Absolute vs relative imports
- Package `__init__.py` exports
- Import aliasing patterns
- Subpackage organization
- Late import technique for circular dependency mitigation
