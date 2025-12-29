from typing import Dict, Any, List
from ex0.Card import Card


class SpellCard(Card):
    """
    Concrete implementation of a Card representing a one-time spell effect.
    """

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """
        Initialize a new SpellCard instance.

        :param name: The name of the spell.
        :param cost: The mana cost to play.
        :param rarity: The rarity level.
        :param effect_type: The type of effect (e.g., damage, heal).
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the spell's play action.

        :param game_state: Current state of the game.
        :return: A dictionary describing the play result.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Spell cast: {self.effect_type}"
        }

    def resolve_effect(self, targets: List[Any]) -> Dict[str, Any]:
        """
        Resolve the specific mechanics of the spell on given targets.

        :param targets: A list of targets affected by the spell.
        :return: A dictionary describing the resolution status.
        """
        return {
            "spell": self.name,
            "targets": targets,
            "status": "Effect resolved"
        }
