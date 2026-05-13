#!/usr/bin/env python3
"""CreatureCard module for creature-type cards."""

from typing import Dict

from ex0.Card import Card


class CreatureCard(Card):
    """A card representing a creature with attack and health."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        attack: int, health: int
    ) -> None:
        """Initialize a CreatureCard.

        Args:
            name: The name of the creature.
            cost: The mana cost to play.
            rarity: The rarity level.
            attack: The attack power.
            health: The health points.

        Raises:
            ValueError: If attack, health, or cost is negative.
        """
        if (attack or health or cost) < 0:
            raise ValueError(
                "CreatureCard: A negative number is not valid"
            )
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def play(self, game_state: dict) -> Dict:
        """Play the creature card given a game state.

        Args:
            game_state: Current state of the game.

        Returns:
            A dict describing the result, or None on error.
        """
        try:
            if game_state.get('mana') < self.cost:
                return {'error': 'Not enough mana to play this card.'}
            result: Dict = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield',
            }
            return result
        except Exception as e:
            if isinstance(e, ValueError):
                print(e)
            else:
                print("Error")
            return None

    def attack_target(self, target: str) -> Dict:
        """Attack a target with this creature.

        Args:
            target: The name of the target to attack.

        Returns:
            A dict describing the attack result.
        """
        result: Dict = {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True,
        }
        return result

    def get_card_info(self) -> dict:
        """Return creature card information as a dictionary.

        Returns:
            A dict with card info including type, attack and health.
        """
        card_info = super().get_card_info()
        card_info.update(
            {"type": "Creature",
             "attack": self.attack,
             "health": self.health}
        )
        return card_info

    def __str__(self) -> str:
        """Return string representation of the creature card."""
        return "(Creature)"
