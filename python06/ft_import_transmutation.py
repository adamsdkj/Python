#!/usr/bin/env python3

import alchemy.elements
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion
from alchemy.elements import create_fire, create_water, create_earth


def main():
    print("\n=== Import Transmutation Mastery ===\n")

    print(
        "Method 1 - Full module import:\n"
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n"
    )

    print(
        "Method 2 - Specific function import:\n"
        f"create_water(): {create_water()}\n"
    )

    print(
        "Method 3 - Aliased import:\n"
        f"heal(): {heal()}\n"
    )

    print(
        "Method 4 - Multiple imports:\n"
        f"create_earth(): {create_earth()}\n"
        f"create_fire(): {create_fire()}\n"
        f"strength_potion(): {strength_potion()}\n"
    )

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
