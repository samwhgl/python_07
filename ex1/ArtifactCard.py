from typing import Dict, Any
from ex0.Card import Card


class ArtifactCard(Card):
    """
    Concrete implementation of a Card representing a permanent artifact.
    """

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        """
        Initialize a new ArtifactCard instance.

        :param name: The name of the artifact.
        :param cost: The mana cost to play.
        :param rarity: The rarity level.
        :param durability: Number of uses before the artifact is depleted.
        :param effect: Description of the artifact's permanent ability.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Place the artifact onto the battlefield.

        :param game_state: Current state of the game.
        :return: A dictionary describing the play result.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}"
        }

    def activate_ability(self) -> Dict[str, Any]:
        """
        Activate the artifact's unique ability, reducing its durability.

        :return: A dictionary containing the result of the activation
                 or an error if depleted.
        """
        if self.durability > 0:
            self.durability -= 1
            return {
                "Artifact": self.name,
                "action": "Ability activated",
                "remaining_durability": self.durability
            }
        return {"error": "Artifact depleted"}
