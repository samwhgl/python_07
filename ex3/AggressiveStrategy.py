from typing import List, Dict, Any
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Concrete strategy implementation that focuses on direct damage
    and playing low-cost cards early.
    """

    def get_strategy_name(self) -> str:
        """
        Return the unique name of this strategy.

        :return: The string 'AggressiveStrategy'.
        """
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """
        Determine target priority, focusing on the enemy player.

        :param available_targets: List of potential targets.
        :return: A list containing prioritized targets.
        """
        if "Enemy Player" in available_targets:
            return ["Enemy Player"]
        return available_targets

    def execute_turn(self, hand: List[Any], battlefield: List[Any]) -> Dict[str, Any]:
        """
        Execute a game turn based on aggressive logic.

        :param hand: List of Card objects currently in hand.
        :param battlefield: List of cards currently on the field.
        :return: A dictionary containing the summary of actions taken.
        """
        played = []
        mana_used = 0
        mana_limit = 5  # Simulated mana limit for the example

        for card in hand:
            if mana_used + card.cost <= mana_limit:
                played.append(card.name)
                mana_used += card.cost

        return {
            "cards_played": played,
            "mana_used": mana_used,
            "targets_attacked": self.prioritize_targets(["Enemy Player"]),
            "damage_dealt": 8
        }
