#!/usr/bin/env python3

import alchemy
import alchemy.transmutation as t


def main():
    print("\n=== Pathway Debate Mastery ===\n")

    print(
        "Testing Absolute Imports (from basic.py):\n"
        f"lead_to_gold(): {t.lead_to_gold()}\n"
        f"stone_to_gem(): {t.stone_to_gem()}\n"
    )

    print(
        "Testing Relative Imports (from advanced.py):\n"
        f"philosophers_stone(): {t.philosophers_stone()}\n"
        f"elixir_of_life(): {t.elixir_of_life()}\n"
    )

    print(
        "Testing Package Access:\n"
        f"alchemy.transmutation.lead_to_gold(): "
        f"{alchemy.transmutation.lead_to_gold()}\n"
        f"alchemy.transmutation.philosophers_stone(): "
        f"{alchemy.transmutation.philosophers_stone()}\n"
    )

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
