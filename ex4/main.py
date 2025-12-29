"""
Main demonstration script for Exercise 4: Tournament System.
Showcases multiple inheritance and complex system integration.
"""
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """
    Execute a tournament simulation with card registration and matches.
    """
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 4)

    platform.register_card(dragon, "dragon_001")
    platform.register_card(wizard, "wizard_001")

    # Display initial rankings
    cards_to_show = [("dragon_001", dragon), ("wizard_001", wizard)]
    for cid, card in cards_to_show:
        print(f"{card.name} (ID: {cid}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(entry)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
