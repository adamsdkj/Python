#! /usr/bin/env python3
"""SpellCard module for spell-type cards."""

from typing import Dict

from ex0.Card import Card


class SpellCard(Card):
    """A card representing a spell with durability and effect type."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        durability: int, effect_type: str
    ) -> None:
        """Initialize a SpellCard.

        Args:
            name: The name of the spell.
            cost: The mana cost to play.
            rarity: The rarity level.
            durability: How durable the spell is.
            effect_type: The type of effect the spell has.

        Raises:
            ValueError: If cost or durability is negative.
        """
        if (cost or durability) < 0:
            raise ValueError(
                "Spellcard: A negative number is not valid"
            )
        super().__init__(name, cost, rarity)
        self.rarity = rarity
        self.durability = durability
        self.effect_type = effect_type

    def play(self, game_state: Dict) -> Dict:
        """Play the spell card given a game state.

        Args:
            game_state: Current state of the game.

        Returns:
            A dict describing the result of playing the card.
        """
        result: Dict = {}
        if game_state.get('mana') < self.cost:
            return {'error': 'Not enough mana to play this card.'}
        result.update({
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type,
        })
        return result

    def activate_ability(self) -> Dict:
        """Activate the spell's special ability.

        Returns:
            A dict describing the activated ability.
        """
        return {}

    def __str__(self) -> str:
        """Return string representation of the spell card."""
        return "(Spell)"
