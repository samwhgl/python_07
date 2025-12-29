"""
Main demonstration script for Exercise 1: Deck Builder System.
"""
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    """
    Demonstrate the deck management system and polymorphism.
    """
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    # Adding cards as required by the exercise example
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana"))

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    # We do not shuffle here to guarantee the output order matches the example
    for _ in range(3):
        card = deck.draw_card()
        # Determine the type for display (Spell, Artifact, Creature)
        card_type = card.__class__.__name__.replace("Card", "")
        print(f"Drew: {card.name} ({card_type})")
        print(f"Play result: {card.play({})}")

    print("\nPolymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
