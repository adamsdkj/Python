"""TournamentCard module for tournament-capable cards."""

from typing import Dict

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """A card that combines Card, Combatable and Rankable."""

    def __init__(
        self, name: str, cost: int, rarity: str
    ) -> None:
        """Initialize a TournamentCard.

        Args:
            name: The name of the card.
            cost: The mana cost to play.
            rarity: The rarity level.
        """
        super().__init__(name, cost, rarity)
        self.id: str = "0"
        self.rating: int = 0
        self.win: int = 0
        self.lose: int = 0

    def play(self, game_state: Dict) -> Dict:
        """Play the tournament card given a game state.

        Args:
            game_state: Current state of the game.

        Returns:
            A dict describing the result of playing the card.
        """
        if game_state.get('mana', 0) < self.cost:
            return {
                'error': 'Not enough mana to play this card.',
            }
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Entered the tournament queue',
        }

    def attack(self, target: str) -> Dict:
        """Attack a target based on rating.

        Args:
            target: The name of the target.

        Returns:
            A dict describing the attack result.
        """
        damage = max(1, self.rating // 100)
        return {
            'attacker': self.name,
            'target': target,
            'damage': damage,
            'combat_type': 'tournament',
        }

    def calculate_rating(self) -> int:
        """Calculate and return the card's rating.

        Returns:
            The current rating, minimum 0.
        """
        return max(0, self.rating)

    def get_tournament_stats(self) -> Dict:
        """Return tournament statistics for this card.

        Returns:
            A dict with id, rating, wins, losses and record.
        """
        return {
            'id': self.id,
            'rating': self.rating,
            'wins': self.win,
            'losses': self.lose,
            'record': f"{self.win}-{self.lose}",
        }

    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage.

        Args:
            incoming_damage: The amount of damage to defend.

        Returns:
            A dict describing the defense result.
        """
        shield = max(0, self.rating // 120)
        damage_blocked = min(incoming_damage, shield)
        damage_taken = incoming_damage - damage_blocked
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_competing': (
                damage_taken < max(1, self.rating // 100)
            ),
        }

    def get_combat_stats(self) -> Dict:
        """Return combat statistics.

        Returns:
            A dict with id, rating, wins and losses.
        """
        return {
            'id': self.id,
            'rating': self.rating,
            'wins': self.win,
            'losses': self.lose,
        }

    def update_wins(self, wins: int) -> None:
        """Update the number of wins.

        Args:
            wins: Number of wins to add.
        """
        if wins < 0:
            return
        self.win += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        """Update the number of losses.

        Args:
            losses: Number of losses to add.
        """
        if losses < 0:
            return
        self.lose += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> Dict:
        """Return ranking information.

        Returns:
            A dict with rating, wins, losses and record.
        """
        return {
            'rating': self.calculate_rating(),
            'wins': self.win,
            'losses': self.lose,
            'record': f"{self.win}-{self.lose}",
        }
