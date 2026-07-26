from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    DefensiveStrategy,
    AggressiveStrategy,
)


def battle(
    opps: list[tuple[
        CreatureFactory
        | HealingCreatureFactory
        | TransformCreatureFactory,
        BattleStrategy,
    ]]
) -> None:
    print(f"{len(opps)} opponents involved")
    for i in range(len(opps) - 1):
        for j in range(i + 1, len(opps)):
            fact_a, strat_a = opps[i]
            fact_b, strat_b = opps[j]
            creature_a = fact_a.create_base()
            creature_b = fact_b.create_base()
            print(f"""
  * Battle *
{creature_a.describe()}
  vs.
{creature_b.describe()}
  now fight!""")
            try:
                strat_a.act(creature_a)
                strat_b.act(creature_b)
            except ValueError as e:
                print(e)
            finally:
                print()


if __name__ == "__main__":
    flame_f: FlameFactory = FlameFactory()
    aqua_f: AquaFactory = AquaFactory()
    heal_f: HealingCreatureFactory = HealingCreatureFactory()
    tran_f: TransformCreatureFactory = TransformCreatureFactory()
    n_strat: NormalStrategy = NormalStrategy()
    d_strat: DefensiveStrategy = DefensiveStrategy()
    a_strat: AggressiveStrategy = AggressiveStrategy()
    print("* * * T O U R N A M E N T   0 * * *")
    battle([(flame_f, n_strat), (heal_f, d_strat)])
    print("* * * T O U R N A M E N T   1 * * *")
    battle([(flame_f, a_strat), (heal_f, d_strat)])
    print("* * * T O U R N A M E N T   2 * * *")
    battle([(aqua_f, n_strat), (heal_f, d_strat), (tran_f, a_strat)])
