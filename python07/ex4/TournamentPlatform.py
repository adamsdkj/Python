"""TournamentPlatform module for managing card tournaments."""

from typing import Dict, List

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Platform for registering cards and running tournament matches."""

    def __init__(self) -> None:
        """Initialize the tournament platform."""
        self.cards: Dict = {}
        self.matches: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card for the tournament.

        Args:
            card: The TournamentCard to register.

        Returns:
            A formatted string with registration details.
        """
        base_name = card.name.split(" ")[-1].lower()
        count = sum(
            1 for c in self.cards.values()
            if c.name == card.name
        ) + 1
        card.id = f"{base_name}_{count:03d}"
        card.rating = (
            1200 if card.rarity == "legendary" else 1150
        )
        info = (
            f"{card.name} (ID: {card.id}):\n"
            "- Interfaces: [Card, Combatable, Rankable]\n"
            f"- Rating: {card.rating}\n"
            f"- Record: {card.win}-{card.lose}"
        )
        self.cards.update({f"{card.id}": card})
        return info

    def create_match(
        self, card1_id: str, card2_id: str
    ) -> Dict:
        """Create a match between two registered cards.

        Args:
            card1_id: ID of the first card.
            card2_id: ID of the second card.

        Returns:
            A dict with match results.
        """
        result: Dict = {}
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        if card1.rating > card2.rating:
            card1.rating += 16
            card1.win += 1
            card2.rating -= 16
            card2.lose += 1
            result.update({
                'winner': card1_id,
                'loser': card2_id,
                'winner_rating': card1.rating,
                'loser_rating': card2.rating,
            })
        else:
            card2.rating += 16
            card2.win += 1
            card1.rating -= 16
            card1.lose += 1
            result.update({
                'winner': card2_id,
                'loser': card1_id,
                'winner_rating': card2.rating,
                'loser_rating': card1.rating,
            })
            self.matches += 1
        return result

    def get_leaderboard(self) -> List:
        """Get the leaderboard sorted by rating.

        Returns:
            A list of cards sorted by rating descending.
        """
        def sort_key(card: TournamentCard) -> int:
            """Return the rating for sorting."""
            return card.rating

        return sorted(
            self.cards.values(), key=sort_key, reverse=True
        )

    def generate_tournament_report(self) -> Dict:
        """Generate a report of the tournament status.

        Returns:
            A dict with total cards, matches, avg rating, status.
        """
        if self.cards:
            total = sum(
                c.rating for c in self.cards.values()
            )
            avg_rating = total / len(self.cards)
        else:
            avg_rating = 0.0

        result: Dict = {
            'total_cards': len(self.cards),
            'total_matches': self.matches,
            'average_rating': avg_rating,
            'platform_status': 'active',
        }
        return result
