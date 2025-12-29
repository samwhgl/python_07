"""
Main demonstration script for Exercise 0: Card Foundation.
"""
from ex0.CreatureCard import CreatureCard


def main() -> None:
    """
    Execute the demonstration of the Card and CreatureCard functionality.
    """
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    # Initialisation des cartes pour le test
    try:
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        goblin = CreatureCard("Goblin Warrior", 1, "Common", 1, 1)

        # Affichage des infos
        print("\nCreatureCard Info:")
        print(dragon.get_card_info())

        # Test du mana (Playable: True)
        mana_available = 6
        msg = f"\nPlaying {dragon.name} with {mana_available} mana available:"
        print(msg)
        print(f"Playable: {dragon.is_playable(mana_available)}")

        # Résultat du play
        game_state = {}
        play_result = dragon.play(game_state)
        print(f"Play result: {play_result}")

        # Combat
        print(f"\n{dragon.name} attacks {goblin.name}:")
        attack_result = dragon.attack_target(goblin)
        print(f"Attack result: {attack_result}")

        # Test mana insuffisant (Playable: False)
        mana_insufficient = 3
        msg_insufficient = (
            f"\nTesting insufficient mana ({mana_insufficient} available):"
        )
        print(msg_insufficient)
        print(f"Playable: {dragon.is_playable(mana_insufficient)}")

        print("\nAbstract pattern successfully demonstrated!")

    except Exception as e:
        print(f"An error occurred during testing: {e}")


if __name__ == "__main__":
    main()
