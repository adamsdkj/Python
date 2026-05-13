#!/usr/bin/env python3
"""Main module demonstrating CreatureCard usage."""

from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Demonstrate the abstract base class design with CreatureCard."""
    print("\n=== DataDeck Card Foundation ===\n"
          "\nTesting Abstract Base Class Design:\n")
    try:
        card = CreatureCard("Fire dragon", 5, "Legendary", 7, 5)
        mana = 6
        game_state = {
            'card': card.name,
            'mana': mana,
        }

        print(f"CreatureCard Info:\n{card.get_card_info()}")
        print(
            f"\nPlaying Fire Dragon with {mana} mana available:"
            f"\nPlayable: {card.is_playable(6)}"
        )
        print(f"Play result: {card.play(game_state)}")
        print(
            "\nFire Dragon attacks Goblin Warrior:\n"
            f"Attack result: {card.attack_target('Goblin Warrior')}"
        )
        print(
            "Testing insufficient mana (3 available):\n"
            f" Playable: {card.is_playable(3)}\n"
            "\nAbstract pattern successfully demonstrated!"
        )

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
