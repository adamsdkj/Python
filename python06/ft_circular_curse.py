#!/usr/bin/env python3

from alchemy.grimoire.spellbook import record_spell
from alchemy.grimoire.validator import validate_ingredients


def main():
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    print(
        f'validate_ingredients("fire air"): '
        f"{validate_ingredients('fire air')}"
    )
    print(
        f'validate_ingredients("dragon scales"): '
        f"{validate_ingredients('dragon scales')}\n"
    )
    print("Testing spell recording with validation:")
    print(
        f'record_spell("Fireball", "fire air"): '
        f"{record_spell('Fireball', 'fire air')}"
    )
    print(
        f'record_spell("Dark Magic", "shadow"): '
        f"{record_spell('Dark Magic', 'shadow')}\n"
    )
    print("Testing late import technique:")
    print(
        f'record_spell("Lightning", "air"): '
        f"{record_spell('Lightning', 'air')} \n"
    )
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
