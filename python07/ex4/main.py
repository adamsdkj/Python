"""Main module demonstrating the Tournament Platform."""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """Demonstrate the tournament platform with card registration."""
    fire_dragon = TournamentCard(
        "Fire Dragon", 5, "legendary"
    )
    ice_wizard = TournamentCard(
        "Ice Wizard", 2, "common"
    )
    tournament = TournamentPlatform()

    print(
        "\n=== DataDeck Tournament Platform ===\n"
        "\nRegistering Tournament Cards..."
        f"\n {tournament.register_card(fire_dragon)}\n"
        f"\n {tournament.register_card(ice_wizard)}"
    )

    print(
        "\nCreating tournament match...\n"
        "Match result: "
        f"{tournament.create_match(fire_dragon.id, ice_wizard.id)}"
    )

    print("\nTournament Leaderboard:")
    for i, card in enumerate(tournament.get_leaderboard()):
        print(
            f"{i + 1}. {card.name} "
            f"- Rating{card.rating}: "
            f"({card.win}-{card.lose})"
        )

    print("\nTournament Report:")
    print(tournament.generate_tournament_report())

    print(
        "\n=== Tournament Platform Successfully Deployed! "
        "===\n"
        "All abstract patterns working together "
        "harmoniously!"
    )


if __name__ == "__main__":
    main()
