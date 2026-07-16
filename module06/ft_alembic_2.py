import alchemy.elements


def test_earth() -> None:
    print(f"""=== Alembic 2 ===
Accessing alchemy/elements.py using 'import ...' structure
Testing create_earth: {alchemy.elements.create_earth()}\n""")


if __name__ == "__main__":
    test_earth()
