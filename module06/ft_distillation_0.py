from alchemy.potions import healing_potion, strength_potion

def brew() -> None:
    print(f"""Testing strength_potion: {strength_potion()}
Testing healing_potion: {healing_potion()}""")


if __name__ == "__main__":
    print("""=== Distillation 0 ===
Direct access to alchemy/potions.py""")
    brew()

