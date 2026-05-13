"""AggressiveStrategy module implementing an aggressive game plan."""

from typing import Dict, List

from ex0.CreatureCard import CreatureCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """A strategy that prioritizes dealing maximum damage."""

    def __init__(self) -> None:
        """Initialize the aggressive strategy with zero counters."""
        self.turns_simulated: int = 0
        self.total_damage: int = 0

    def execute_turn(
        self, hand: list, battlefield: list
    ) -> Dict:
        """Execute an aggressive turn.

        Args:
            hand: List of cards in hand.
            battlefield: List of entities on the battlefield.

        Returns:
            A dict describing turn actions and damage.
        """
        result: Dict = {}
        cards_played: List[str] = []
        mana_used = 0
        damage_dealt = 0
        for card in hand:
            cards_played.append(card.name)
            mana_used += card.cost
            if isinstance(card, CreatureCard):
                damage_dealt += card.attack

        result.update({
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': battlefield,
            'damage_dealt': damage_dealt,
        })
        self.turns_simulated += 1
        self.total_damage += damage_dealt
        return result

    def get_strategy_name(self) -> str:
        """Return the name of this strategy.

        Returns:
            The string 'AggressiveStrategy'.
        """
        return "AggressiveStrategy"

    def prioritize_targets(
        self, available_targets: list
    ) -> List:
        """Prioritize targets, placing enemy player first.

        Args:
            available_targets: List of potential targets.

        Returns:
            Sorted list of targets by priority.
        """
        def target_priority(target: object) -> int:
            """Return priority for a target."""
            if str(target) == 'Enemy Player':
                return 0
            return 1

        return sorted(available_targets, key=target_priority)
