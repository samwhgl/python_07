from typing import Dict, Any, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Powerful card implementing multiple inheritance for combat and magic.
    """

    def __init__(
        self, name: str, cost: int, rarity: str,
        attack_power: int, mana_reserve: int
    ):
        """
        Initialize an EliteCard with both combat and magical properties.

        :param name: Card name.
        :param cost: Mana cost.
        :param rarity: Rarity level.
        :param attack_power: Base attack damage.
        :param mana_reserve: Starting mana for spells.
        """
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.mana_reserve = mana_reserve

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Play the card to the battlefield.

        :param game_state: Current game environment.
        :return: Status of the card being played.
        """
        return {
            "card_played": self.name,
            "type": "EliteCard",
            "status": "Ready for multi-action"
        }

    def attack(self, target: Any) -> Dict[str, Any]:
        """
        Execute a melee attack.

        :param target: Target entity.
        :return: Detailed attack results.
        """
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """
        Defend against an incoming attack with damage reduction.

        :param incoming_damage: Initial damage value.
        :return: Damage mitigation report.
        """
        blocked = 3
        taken = max(0, incoming_damage - blocked)
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        """
        Retrieve combat-related attributes.

        :return: Combat stats dictionary.
        """
        return {"attack": self.attack_power}

    def cast_spell(self, spell_name: str, targets: List[Any]) -> dict:
        """
        Cast a magical spell consuming mana.

        :param spell_name: Name of the spell.
        :param targets: Affected targets.
        :return: Result of the spell casting.
        """
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """
        Channel energy to increase mana reserve.

        :param amount: Amount of mana to add.
        :return: Updated mana status.
        """
        self.mana_reserve += amount
        return {"channeled": amount, "total_mana": self.mana_reserve}

    def get_magic_stats(self) -> Dict[str, Any]:
        """
        Retrieve magic-related attributes.

        :return: Magic stats dictionary.
        """
        return {"mana_reserve": self.mana_reserve}
