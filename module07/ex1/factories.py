from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str="Creature", type: str="Any") -> None:
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


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")
    
    def attack(self) -> str:
        return f"{self.get_name()} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    
    def attack(self) -> str:
        return f"{self.get_name()} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    
    def attack(self) -> str:
        return f"{self.get_name()} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    
    def attack(self) -> str:
        return f"{self.get_name()} uses Hydro Pump!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        flameling: Flameling = Flameling()
        return flameling

    def create_evolved(self) -> Pyrodon:
        pyrodon: Pyrodon = Pyrodon()
        return pyrodon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        aquabub: Aquabub = Aquabub()
        return aquabub

    def create_evolved(self) -> Torragon:
        torragon: Torragon = Torragon()
        return torragon


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature) -> str:
        ...


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...

class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.get_name()} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.get_name()} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.get_name()} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.get_name()} heals itself and others for a large amount"











k

