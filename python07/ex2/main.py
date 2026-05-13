"""Main module demonstrating the EliteCard ability system."""

from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical

card_methods = [
    name for name in dir(Card) if not name.startswith("_")
]
combatable_methods = [
    name for name in dir(Combatable) if not name.startswith("_")
]
magical_methods = [
    name for name in dir(Magical) if not name.startswith("_")
]

try:
    elite_card = EliteCard(
        "Arcane Warrior", 4, "common", 5, "melee", 3, 10, 14
    )
except Exception as e:
    print(e)

print("\n=== DataDeck Ability System ===")
print(
    "EliteCard capabilities:\n"
    f"- Card: {card_methods}\n"
    f"- Combatable: {combatable_methods}\n"
    f"- Magical: {magical_methods}\n"
)
print(
    "Playing Arcane Warrior (Elite Card):\n"
    "Combat phase:\n"
    f"Attack result: {elite_card.attack('Enemy')}\n"
    f"6Defend result: {elite_card.defend(5)}\n"
)
print(
    "Magic phase:\n"
    f"Spell cast: "
    f"{elite_card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}\n"
    f"Mana channel: {elite_card.channel_mana(3)}"
)
print("\nMultiple interface implementation successful!")
