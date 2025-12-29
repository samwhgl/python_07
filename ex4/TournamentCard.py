from typing import Dict, Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Tournament-ready card implementation using multiple inheritance.
    Combines base card properties, combat abilities, and ranking stats.
    """

    def __init__(self, name: str, cost: int, rarity: str, attack: int):
        """
        Initialize a TournamentCard with ranking and combat attributes.

        :param name: Card name.
        :param cost: Mana cost.
        :param rarity: Rarity level.
        :param attack: Base attack power.
        """
        # Initialisation via Card base
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.wins = 0
        self.losses = 0
        self.rating = 1200  # Base Elo rating

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Implement the Card play interface."""
        return {
            "card_played": self.name,
            "effect": "Entering tournament field"
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        """Implement the Combatable attack interface."""
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Implement the Combatable defense interface."""
        return {"defender": self.name, "status": "Defending"}

    def get_combat_stats(self) -> Dict[str, Any]:
        """Implement the Combatable stats interface."""
        return {"attack": self.attack_power}

    def calculate_rating(self) -> int:
        """Retrieve current ranking value."""
        return self.rating

    def update_wins(self, wins: int) -> None:
        """Update wins and increase rating points."""
        self.wins += wins
        self.rating += (wins * 16)

    def update_losses(self, losses: int) -> None:
        """Update losses and decrease rating points."""
        self.losses += losses
        self.rating -= (losses * 16)

    def get_rank_info(self) -> Dict[str, Any]:
        """Return a summary of ranking and record."""
        return {
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> Dict[str, Any]:
        """Return full tournament performance statistics."""
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }
