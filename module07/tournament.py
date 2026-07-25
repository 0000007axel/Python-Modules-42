from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy


if __name__ == "__main__":
    flame_f: FlameFactory = FlameFactory()
    aqua_f: AquaFactory = AquaFactory()

    flame = flame_f.create_base()
    aqua = aqua_f.create_base()
