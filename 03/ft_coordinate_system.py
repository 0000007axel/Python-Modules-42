import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        str_pos: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        usr_input = str_pos.split(',')
        xyz: list[float] = [0, 0, 0]

        for i in range(0, 3):
            try:
                xyz[i] = float(usr_input[i])
            except TypeError as e1:
                print(f"Error on parameter '{xyz[i]}': {e1}")
            except ValueError as e2:
                print(f"")
        print(f"Got a first tuple: {x , y, z}")
        return (x, y, z)


def main() -> None:
    print("=== Game Coordinates System ===\n")
    get_player_pos()


if __name__ == "__main__":
    main()
