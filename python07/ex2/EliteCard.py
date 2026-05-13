"""EliteCard module for elite cards with combat and magic."""

from typing import Dict, List

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """An elite card combining Card, Combatable and Magical interfaces."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        damage: int, combat_type: str, shield: int,
        health: int, mana: int
    ) -> None:
        """Initialize an EliteCard.

        Args:
            name: The name of the card.
            cost: The mana cost to play.
            rarity: The rarity level.
            damage: The damage value.
            combat_type: The type of combat (e.g. melee).
            shield: The shield value.
            health: The health points.
            mana: The mana pool.

        Raises:
            ValueError: If any numeric stat is negative.
        """
        if (cost or damage or shield or health) < 0:
            raise ValueError("Negative number")
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.combat_type = combat_type
        self.shield = shield
        self.health = health
        self.mana = mana

    def play(self, game_state: Dict) -> Dict:
        """Play the elite card given a game state.

        Args:
            game_state: Current state of the game.

        Returns:
            A dict describing the result of playing the card.
        """
        result: Dict = {}
        if game_state.get('mana') < self.cost:
            result.update({
                'error': 'Not enough mana to play this card.',
            })
        else:
            result.update({
                'name': self.name,
                'mana_used': self.cost,
                'combat_type': self.combat_type,
            })
        return result

    def attack(self, target: str) -> Dict:
        """Attack a target.

        Args:
            target: The name of the target.

        Returns:
            A dict describing the attack result.
        """
        result: Dict = {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type,
        }
        return result

    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage.

        Args:
            incoming_damage: The amount of damage to defend.

        Returns:
            A dict describing the defense result.
        """
        result: Dict = {}
        damage_blocked = 0
        health = self.health
        damage = max(0, (incoming_damage - self.shield))
        if damage != 0:
            damage_blocked = self.shield
            self.shield = 0
        else:
            rest = self.shield - incoming_damage
            damage_blocked = self.shield - rest
            self.shield = rest
        health -= damage
        result.update({
            'defender': self.name,
            'damage_taken': damage,
            'damage_blocked': damage_blocked,
            'still_alive': health > 0,
        })
        return result

    def get_combat_stats(self) -> Dict:
        """Return combat statistics.

        Returns:
            A dict with combat-related stats.
        """
        result: Dict = {
            'damage': self.damage,
            'combat_type': self.combat_type,
            'shield': self.shield,
            'health': self.health,
        }
        return result

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Cast a spell on targets.

        Args:
            spell_name: The name of the spell to cast.
            targets: List of targets for the spell.

        Returns:
            A dict describing the spell result.
        """
        result: Dict = {}
        self.mana = max(0, self.mana - self.cost)
        if self.mana == 0:
            result.update({
                'spell_cast': False,
                'reason': 'Not enough mana',
            })
        else:
            result.update({
                'attacker': self.name,
                'spell': spell_name,
                'target': targets,
                'mana_used': self.cost,
            })
        return result

    def channel_mana(self, amount: int) -> Dict:
        """Channel mana energy.

        Args:
            amount: The amount of mana to channel.

        Returns:
            A dict describing the channeling result.
        """
        if amount < 0:
            return {'error': 'cannot chanel negative mana'}
        result: Dict = {}
        rest = max(0, self.mana - amount)
        if rest == 0:
            amount = self.mana
            self.mana = 0
        else:
            self.mana -= amount
        result.update({
            'channeled': amount,
            'total': self.mana,
        })
        return result

    def get_magic_stats(self) -> Dict:
        """Return magic-related statistics.

        Returns:
            A dict with magic-related stats.
        """
        result: Dict = {
            'mana': self.mana,
            'cost': self.cost,
        }
        return result
