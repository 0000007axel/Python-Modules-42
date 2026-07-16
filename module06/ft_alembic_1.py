from elements import create_water


def test_water() -> None:
    print(f"""=== Alembic 1 ===
Using: 'from ... import ...' structure to access elements.py
Testing create_water: {create_water()}\n""")


if __name__ == "__main__":
    test_water()
