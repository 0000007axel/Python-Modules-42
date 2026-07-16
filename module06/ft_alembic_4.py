import alchemy


def test_air() -> None:
    print(f"Testing create_air: {alchemy.create_air()}")


def test_earth() -> None:
    print(f"Testing create_earth: {alchemy.create_earth()}")


if __name__ == "__main__":
    print(f"""=== Alembic 4 ===
Accessing the alchemy module using 'import alchemy'
Testing create_air: {alchemy.create_air()}
Now show that not all functions can be reached
This will raise an exception!
Testing the hidden create_earth:""", end="")
    print(f"{alchemy.create_earth()}")
