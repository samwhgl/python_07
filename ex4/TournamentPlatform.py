from typing import Dict, List, Any
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """
    Management system for competitive tournament play.
    Handles card registration, matchmaking, and leaderboards.
    """

    def __init__(self):
        """
        Initialize the tournament platform with an empty registry.
        """
        self.registry: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard, card_id: str) -> str:
        """
        Register a new card into the tournament system.

        :param card: The TournamentCard instance to register.
        :param card_id: A unique identifier for the card.
        :return: The registered card identifier.
        """
        self.registry[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        """
        Execute a match between two registered cards based on attack power.

        :param card1_id: ID of the first participant.
        :param card2_id: ID of the second participant.
        :return: A summary of the match results including rating updates.
        """
        card1 = self.registry[card1_id]
        card2 = self.registry[card2_id]

        # Simple match logic: higher attack power wins
        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
            w_id, l_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            w_id, l_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": w_id,
            "loser": l_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List[str]:
        """
        Generate a formatted leaderboard sorted by Elo rating.

        :return: A list of strings representing the ranked players.
        """
        # Sort cards by rating in descending order
        sorted_cards = sorted(
            self.registry.values(),
            key=lambda x: x.rating,
            reverse=True
        )

        leaderboard = []
        for i, card in enumerate(sorted_cards, 1):
            info = card.get_rank_info()
            entry = (
                f"{i}. {card.name} - Rating: {info['rating']} "
                f"({info['record']})"
            )
            leaderboard.append(entry)
        return leaderboard

    def generate_tournament_report(self) -> Dict[str, Any]:
        """
        Generate global statistics for the current tournament session.

        :return: A dictionary containing platform-wide metrics.
        """
        total_rating = sum(c.rating for c in self.registry.values())
        count = len(self.registry)
        avg_rating = total_rating // count if count > 0 else 0

        return {
            "total_cards": count,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
