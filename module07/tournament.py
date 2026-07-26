from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, DefensiveStrategy, AggressiveStrategy

def battle(opps: list[tuple[CreatureFactory, BattleStrategy]]):
    for i in range(len(opps) - 1):
        for j in range(i + 1, len(opps)):
            fact_a, strat_a = opps[i]
            fact_b, strat_b = opps[j]
            creature_a = fact_a.create_base()
            creature_b = fact_b.create_base()
            print(f"""  Xx Battle xX
{creature_a.describe()}
  vs.
{creature_b.describe()}
  now fight!""")
            strat_a.act(creature_a)
            strat_b.act(creature_b)




if __name__ == "__main__":
    flame_f: FlameFactory = FlameFactory()
    aqua_f: AquaFactory = AquaFactory()
    n_strat = NormalStrategy()
    battle([(flame_f, n_strat), (aqua_f, n_strat)])
