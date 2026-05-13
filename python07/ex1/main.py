#! /usr/bin/env python3
"""Main module demonstrating the Deck Builder."""

from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck

print("\n=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")

try:
    spell_card = SpellCard(
        "Lightning Bolt", 3, "common", 20,
        "Deal 3 damage to target"
    )
    artifact_card = ArtifactCard(
        "Mana Crystal", 2, "common", 10,
        "Permanent: +1 mana per turn"
    )
    creature_card = CreatureCard(
        "Fire dragon", 5, "Legendary", 7, 5
    )

    deck = Deck()

    deck.add_card(spell_card)
    deck.add_card(creature_card)
    deck.add_card(artifact_card)

    print(f"Deck stats: {deck.get_deck_stats()}\n")

    card_drew = deck.draw_card()
    while card_drew:
        game_state = {
            'card': card_drew.name,
            'mana': 100,
        }
        print(
            "Drawing and playing cards:\n"
            f"\nDrew: {card_drew.name} {card_drew}\n"
            f"Play result: {card_drew.play(game_state)}"
        )
        card_drew = deck.draw_card()

    print(
        "\nPolymorphism in action: "
        "Same interface, different card behaviors!"
    )

except Exception as e:
    print(e)
