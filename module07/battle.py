from ex0 import CreatureFactory, AquaFactory, FlameFactory


def factory_tester(factory: CreatureFactory) -> bool:
    try:
        print(f"""Testing factory
{factory.create_base().describe()}
{factory.create_base().attack()}
{factory.create_evolved().describe()}
{factory.create_evolved().attack()}\n""")
        return True
    except AttributeError:
        print(f"The argument is not valid")
        return False


def battle_tester(factory_one: CreatureFactory, factory_two: CreatureFactory):
    print(f"""Testing battle
{factory_one.create_base().describe()}
  vs.
{factory_two.create_base().describe()}
  fight!
{factory_one.create_base().attack()}
{factory_two.create_base().attack()}
""")


if __name__ == "__main__":
    f: FlameFactory = FlameFactory()
    a: AquaFactory = AquaFactory()
    f_condition: bool = factory_tester(f)
    a_condition: bool = factory_tester(a)
    if f_condition and a_condition:
        battle_tester(f, a)
