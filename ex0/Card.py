from abc import ABC
from typing import Dict, Any


class Card(ABC):
    """
    Abstract Base Class representing the foundational blueprint for all cards.
    """

    def __init__(self, name: str, cost: int, rarity: str):
        """
        Initialize a new Card instance.

        :param name: The name of the card.
        :param cost: The mana cost to play the card.
        :param rarity: The rarity level of the card (e.g., Common, Legendary).
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Abstract method to define the card's effect when played.

        :param game_state: A dictionary representing the current game status.
        :return: A dictionary describing the result of playing the card.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError("Subclass must implement play()")

    def get_card_info(self) -> Dict[str, Any]:
        """
        Retrieve the basic information of the card.

        :return: A dictionary containing the card's name, cost, and rarity.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Check if the card can be played given the available mana.

        :param available_mana: The current amount of mana the player has.
        :return: True if the cost is less than or equal to available mana.
        """
        return available_mana >= self.cost
