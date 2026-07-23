from ex0 import CreatureFactory, AquaFactory, FlameFactory


def factory_tester(factory: CreatureFactory):
    print(f"""Testing factory
{factory.create_base().describe()}
{factory.create_base().attack()}
{factory.create_evolved().describe()}
{factory.create_evolved().attack()}""")

if __name__ == "__main__":
    f: FlameFactory = FlameFactory()
    a: AquaFactory = AquaFactory()
