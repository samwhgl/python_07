import random
from typing import Dict, Any, List
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


class Deck:
    """
    A class to manage a collection of various card types.
    """

    def __init__(self):
        """
        Initialize an empty deck.
        """
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck.

        :param card: The Card instance to add.
        """
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove a card from the deck by its name.

        :param card_name: The name of the card to remove.
        :return: True if a card was removed, False otherwise.
        """
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """
        Randomly reorder the cards in the deck.
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Remove and return the top card of the deck.

        :return: The Card instance drawn.
        :raises IndexError: If the deck is empty.
        """
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict[str, Any]:
        """
        Calculate statistics about the cards currently in the deck.

        :return: A dictionary containing card counts and average cost.
        """
        stats = {
            "total_cards": len(self.cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0.0
        }
        if not self.cards:
            return stats

        total_cost = 0
        for card in self.cards:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                stats["creatures"] += 1
            elif isinstance(card, SpellCard):
                stats["spells"] += 1
            elif isinstance(card, ArtifactCard):
                stats["artifacts"] += 1

        stats["avg_cost"] = total_cost / stats["total_cards"]
        return stats
