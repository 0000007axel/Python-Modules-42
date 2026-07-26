from abc import ABC, abstractmethod
from typing import Any


class Creature(ABC):
    def __init__(self, name: str = "Creature", type: str = "Any") -> None:
        self._name: str = name
        self._type: str = type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.get_name()} is a {self.get_type()} type Creature"

    def get_name(self) -> str:
        return self._name

    def get_type(self) -> str:
        return self._type


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Any) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return hasattr(creature, "attack")

    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if (hasattr(creature, "transform")
                and hasattr(creature, "attack")
                and hasattr(creature, "revert")):
            return True
        return False

    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise ValueError("Battle error, aborting tournament: "
                             f"Invalid Creature '{creature.get_name()}' "
                             "for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if hasattr(creature, "attack") and hasattr(creature, "heal"):
            return True
        return False

    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal())
        else:
            raise ValueError("Battle error, aborting tournament: "
                             f"Invalid Creature '{creature.get_name()}' "
                             "for this defensive strategy")
