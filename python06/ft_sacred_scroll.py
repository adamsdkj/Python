#! /usr/bin/env python3

import alchemy
import alchemy.elements


def main():
    print("\n=== Sacred Scroll Mastery ===\n")
    print(
        "Testing direct module access:\n"
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n"
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}\n"
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}\n"
        f"alchemy.elements.create_air(): {alchemy.elements.create_air()}\n"
    )

    print(
        "Testing package-level access (controlled by __init__.py):\n"
        f"alchemy.create_fire(): {alchemy.create_fire()}\n"
        f"alchemy.create_water(): {alchemy.create_water()}"
    )
    try:
        alchemy.create_earth()
    except Exception:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        alchemy.create_air()
    except Exception:
        print("alchemy.create_air(): AttributeError - not exposed")

    print(
        "\nPackage metadata:\n"
        f"Version: {alchemy.__verion__}\n"
        f"Author: {alchemy.__author__}"
    )


if __name__ == "__main__":
    main()
