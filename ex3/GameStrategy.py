from abc import ABC
from typing import List, Dict, Any


class GameStrategy(ABC):
    """
    Abstract interface for defining NPC or player AI decision-making logic.
    """

    def execute_turn(
        self, hand: List[Any], battlefield: List[Any]
    ) -> Dict[str, Any]:
        """
        Determine actions to take during a single game turn.

        :param hand: List of cards currently held by the player.
        :param battlefield: List of cards currently in play.
        :return: A dictionary describing the actions performed.
        :raises NotImplementedError: If not implemented by subclass.
        """
        raise NotImplementedError()

    def get_strategy_name(self) -> str:
        """
        Retrieve the unique name identifier for the strategy.

        :return: The name of the strategy as a string.
        :raises NotImplementedError: If not implemented by subclass.
        """
        raise NotImplementedError()

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """
        Decide the order of targets to attack based on strategy logic.

        :param available_targets: List of possible targets to attack.
        :return: A prioritized list of targets.
        :raises NotImplementedError: If not implemented by subclass.
        """
        raise NotImplementedError()
