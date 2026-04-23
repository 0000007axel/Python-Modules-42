import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        usr_input: str = input(
                "Enter new coordinates as floats in format 'x,y,z': ")
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


def calculate_distance(p1: tuple[float, float, float],
                       p2: tuple[float, float, float]) -> float:
    dist: float = round(math.sqrt((p2[0]-p1[0])**2
                            + (p2[1]-p1[1])**2
                            + (p2[2]-p1[2])**2),
                        4)
    return dist


def main() -> None:
    print("=== Game Coordinates System ===\n")
    print("Get a first set of coordinates")
    set1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {set1}")
    print(f"It includes: X={set1[0]}, Y={set1[1]}, Z={set1[2]}")
    print(f"Distance to center: {calculate_distance(set1, (0, 0, 0))}\n")
    print("Get a second set of coordinates")
    set2: tuple[float, float, float] = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{calculate_distance(set1, set2)}")



if __name__ == "__main__":
    main()
