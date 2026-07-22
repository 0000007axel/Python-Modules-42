from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str="Creature", type: str="Any") -> None:
        self._name: str = name
        self._type: str = type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self):
        print(f"{self._name} is a {self._type} type Creature")


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")
    
    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Water")

    
    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    
    def attack(self) -> str:
        return f"{self._name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    
    def attack(self) -> str:
        return f"{self._name} uses Hydro Pump!"


class CreatureFactory(ABC):
    def __init__(self, starter: Creature) -> None:
        self._starter = starter

    @abstractmethod
    def create_base(self, evolved_creature: Creature) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self, base_creature) -> Creature:
        ...


class FlameFactory(CreatureFactory):

    def create_base(self, name) -> Flameling:






















