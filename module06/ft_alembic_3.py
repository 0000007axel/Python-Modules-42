from alchemy.elements import create_air


def test_air() -> None:
    print(f"""=== Alembic 3 ===
Accessing alchemy/elements.py using 'from ... import ...' structure
Testing create_air: {create_air()}\n""")


if __name__ == "__main__":
    test_air()
