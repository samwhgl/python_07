from typing import Dict, Any
from ex0.Card import Card


class CreatureCard(Card):
    """
    Concrete implementation of a Card representing a creature with combat stats.
    """

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ):
        """
        Initialize a new CreatureCard instance.

        :param name: The name of the creature.
        :param cost: The mana cost to play.
        :param rarity: The rarity level.
        :param attack: Combat power (must be a positive integer).
        :param health: Survival points (must be a positive integer).
        :raises ValueError: If attack or health are not positive integers.
        """
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack < 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Summon the creature to the battlefield.

        :param game_state: Current state of the game.
        :return: A dictionary describing the summoning result.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def get_card_info(self) -> Dict[str, Any]:
        """
        Retrieve full creature statistics including attack and health.

        :return: A dictionary with base card info plus creature stats.
        """
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info

    def attack_target(self, target: Any) -> Dict[str, Any]:
        """
        Execute an attack against a target.

        :param target: The object being attacked (must have a name or be str).
        :return: A dictionary containing combat results.
        """
        target_name = target.name if hasattr(target, 'name') else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
