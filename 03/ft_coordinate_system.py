import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        usr_input: str = input("Enter new coordinates as floats in format 'x,y,z': ")
        usr_xyz: list[str] = usr_input.split(',')
        if len(usr_xyz) != 3:
            print("Invalid syntax")
            continue
        xyz: list[float] = [0, 0, 0]
        try:
            for i in range(0, 3):
                xyz[i] = float(usr_xyz[i])
            return (float(xyz[0]), float(xyz[1]), float(xyz[2]))
        except ValueError as err:
            print(f"Error on parameter '{usr_xyz[i]}': {err}")
            continue
        except TypeError:
            print("Invalid syntax")
            continue


def main() -> None:
    print("=== Game Coordinates System ===\n")
    print("Get a first set of coordinates")
    xyz: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {xyz}")
    print(f"It includes: X={xyz[0]}, Y={xyz[1]}, Z={xyz[2]}")


if __name__ == "__main__":
    main()
