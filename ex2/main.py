"""
Main demonstration script for Exercise 2: Ability System.
Explores multiple inheritance through the EliteCard implementation.
"""
from ex2.EliteCard import EliteCard


def main() -> None:
    """
    Demonstrate the capabilities of EliteCard combining multiple interfaces.
    """
    print("=== DataDeck Ability System ===")

    # Create the Arcane Warrior instance
    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 4)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {warrior.name} (Elite Card):")

    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    spell_res = warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])
    print(f"Spell cast: {spell_res}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
