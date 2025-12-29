from abc import ABC
from typing import Dict, Any
from ex0.Card import Card


class CardFactory(ABC):
    """
    Abstract interface for creating themed card sets and decks.
    """

    def create_creature(self, name_or_power: Any) -> Card:
        """
        Create a creature card based on theme-specific parameters.

        :param name_or_power: Name or power level for the creature.
        :return: A Card instance of type creature.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def create_spell(self, name_or_power: Any) -> Card:
        """
        Create a spell card based on theme-specific parameters.

        :param name_or_power: Name or power level for the spell.
        :return: A Card instance of type spell.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def create_artifact(self, name_or_power: Any) -> Card:
        """
        Create an artifact card based on theme-specific parameters.

        :param name_or_power: Name or power level for the artifact.
        :return: A Card instance of type artifact.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """
        Generate a complete themed deck of a specific size.

        :param size: Number of cards to include in the deck.
        :return: A dictionary containing the deck collection.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def get_supported_types(self) -> Dict[str, Any]:
        """
        Retrieve the types of cards supported by this factory.

        :return: A dictionary of supported card categories.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()
