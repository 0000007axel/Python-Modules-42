import alchemy


def brew_1() -> None:
    print(f"""Testing strength potion: {alchemy.strength_potion()}
Testing heal alias: {alchemy.heal()}""")


if __name__ == "__main__":
    print("""=== Distillation 1 ===
Using: 'import alchemy' structure to access potions""")
    brew_1()
