from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, DefensiveStrategy, AggressiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]):
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a  = opponents[i]
            factory_b, strategy_b = opponents[j]
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
            print(f"""{creature_a.describe()}
  vs.
{creature_b.describe()}
  now fight!
{strategy_a.act(creature_a)}
""")
        


if __name__ == "__main__":
    print(f"""Tournament 0 (basic)
 [ (Flameling+Normal), (Healing+Defensive) ]""")
    f_factory: FlameFactory = FlameFactory()
    a_factory: AquaFactory = AquaFactory()
    h_factory: HealingCreatureFactory = HealingCreatureFactory()
    test1= [ (f_factory, NormalStrategy), (h_factory, DefensiveStrategy) ]
    battle(test1)
