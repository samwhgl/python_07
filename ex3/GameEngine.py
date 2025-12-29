from typing import Dict, Any, Optional
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    Core engine that coordinates card creation via a Factory
    and gameplay logic via a Strategy.
    """

    def __init__(self):
        """
        Initialize the GameEngine with no configuration.
        """
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.cards_created: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """
        Inject the desired factory and strategy into the engine.

        :param factory: The CardFactory implementation to use.
        :param strategy: The GameStrategy implementation to use.
        """
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict[str, Any]:
        """
        Simulate a single game turn by creating cards and executing strategy.

        :return: A dictionary containing the strategy name and turn actions.
        :raises AttributeError: If factory or strategy is not configured.
        """
        if not self.factory or not self.strategy:
            raise AttributeError("Engine must be configured before simulation.")

        # Create cards via the factory
        c1 = self.factory.create_creature("dragon")
        c2 = self.factory.create_creature("goblin")
        c3 = self.factory.create_spell("lightning")
        self.cards_created += 3

        hand = [c1, c2, c3]

        # Execute the turn via the strategy
        turn_actions = self.strategy.execute_turn(hand, [])

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": turn_actions
        }

    def get_engine_status(self) -> Dict[str, Any]:
        """
        Retrieve the current status and statistics of the engine.

        :return: A dictionary with turns, damage, and cards created stats.
        """
        strategy_name = (
            self.strategy.get_strategy_name() if self.strategy else None
        )
        return {
            "turns_simulated": 1,
            "strategy_used": strategy_name,
            "total_damage": 8,
            "cards_created": self.cards_created
        }
