from abc import ABC


class Magical(ABC):
    """
    Abstract interface defining magical capabilities for cards.
    """

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Cast a magical spell targeting specific entities.

        :param spell_name: The name of the spell to cast.
        :param targets: A list of targets affected by the spell.
        :return: A dictionary containing spell execution details.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def channel_mana(self, amount: int) -> dict:
        """
        Increase the mana reserve of the card.

        :param amount: The amount of mana to channel.
        :return: A dictionary containing updated mana status.
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()

    def get_magic_stats(self) -> dict:
        """
        Retrieve the magical statistics of the card.

        :return: A dictionary containing magic stats (e.g., mana reserve).
        :raises NotImplementedError: If the subclass does not implement this.
        """
        raise NotImplementedError()
