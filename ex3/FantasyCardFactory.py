from typing import Dict, Any, List
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    """
    Concrete factory for creating Fantasy-themed cards.
    """

    def create_creature(self, name_or_power: Any) -> CreatureCard:
        """
        Create a fantasy creature card based on a keyword or power level.

        :param name_or_power: The type of creature to create.
        :return: A CreatureCard instance (Dragon or Goblin).
        """
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)

    def create_spell(self, name_or_power: Any) -> SpellCard:
        """
        Create a fantasy-themed spell card.

        :param name_or_power: The type of spell to create.
        :return: A SpellCard instance.
        """
        return SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage")

    def create_artifact(self, name_or_power: Any) -> ArtifactCard:
        """
        Create a fantasy-themed artifact card.

        :param name_or_power: The type of artifact to create.
        :return: An ArtifactCard instance.
        """
        return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana")

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """
        Return a summary of a generated fantasy-themed deck.

        :param size: The number of cards in the deck.
        :return: A dictionary describing the themed deck.
        """
        return {"theme": "Fantasy", "size": size}

    def get_supported_types(self) -> Dict[str, List[str]]:
        """
        Retrieve all fantasy card types supported by this factory.

        :return: A dictionary mapping card categories to their types.
        """
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
