from abc import ABC
from typing import Dict, Any


class Combatable(ABC):
    """
    Abstract interface defining combat capabilities for cards.
    """

    def attack(self, target: Any) -> Dict[str, Any]:
        """
        Execute an attack against a specified target.

        :param target: The entity to be attacked.
        :return: A dictionary containing attack results.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """
        Process incoming damage and determine survival.

        :param incoming_damage: The amount of damage received.
        :return: A dictionary containing defense results.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def get_combat_stats(self) -> Dict[str, Any]:
        """
        Retrieve the combat-related statistics of the card.

        :return: A dictionary containing combat stats (e.g., attack power).
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()
