from abc import ABC
from typing import Dict, Any


class Rankable(ABC):
    """
    Abstract interface for objects that can be ranked within a system.
    Defines the contract for Elo rating and match history management.
    """

    def calculate_rating(self) -> int:
        """
        Calculate and return the current rating of the entity.

        :return: The current rating as an integer.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def update_wins(self, wins: int) -> None:
        """
        Update the winning record of the entity.

        :param wins: The number of wins to add to the total.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def update_losses(self, losses: int) -> None:
        """
        Update the losing record of the entity.

        :param losses: The number of losses to add to the total.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def get_rank_info(self) -> Dict[str, Any]:
        """
        Retrieve a summary of ranking statistics.

        :return: A dictionary containing rating and performance records.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()
