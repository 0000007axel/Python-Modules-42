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
    def __init__(self) -> None:
        self.is_sharp: bool = False

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


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")

    def attack(self) -> str:
        if self.is_sharp:
            return f"{self.get_name()} performs a boosted strike."
        else:
            return f"{self.get_name()} attacks normally."

    def transform(self) -> str:
        if not self.is_sharp:
            self.is_sharp = True
            return f"{self.get_name()} shifts into a sharper form!"
        else:
            return f"{self.get_name()} is already in its sharp form."

    def revert(self) -> str:
        if self.is_sharp:
            self.is_sharp = False
            return f"{self.get_name()} returns to normal."
        else:
            return f"{self.get_name()} is already in its normal form."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if self.is_sharp:
            return f"{self.get_name()} performs a devastating morph strike!"
        else:
            return f"{self.get_name()} attacks normally."

    def transform(self) -> str:
        if not self.is_sharp:
            self.is_sharp = True
            return f"{self.get_name()} shifts into a dragonic battle form!"
        else:
            return f"{self.get_name()} is already in its dragonic form."

    def revert(self) -> str:
        if self.is_sharp:
            self.is_sharp = False
            return f"{self.get_name()} stabilizes its form."
        else:
            return f"{self.get_name()} is already in its stabilized form."


class HealingCreatureFactory(ABC):
    def create_base(self) -> Sproutling:
        sproutling: Sproutling = Sproutling()
        return sproutling

    def create_evolved(self) -> Bloomelle:
        bloomelle: Bloomelle = Bloomelle()
        return bloomelle


class TransformCreatureFactory(ABC):
    def create_base(self) -> Shiftling:
        shiftling: Shiftling = Shiftling()
        return shiftling

    def create_evolved(self) -> Morphagon:
        morphagon: Morphagon = Morphagon()
        return morphagon
