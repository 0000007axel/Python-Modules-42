#!/usr/bin/env python3.13


import math


def create_coords() -> tuple[float, float, float]:
    while True:
        try:
            usr_input: str = input(
                    "Enter new coordinates as floats in format 'x,y,z': ")
            usr_xyz: list[str] = usr_input.split(',')
            if len(usr_xyz) != 3:
                raise ValueError("You need 3 dimensions")
            return (float(usr_xyz[0]), float(usr_xyz[1]), float(usr_xyz[2]))
        except ValueError as err:
            print(f"Error on passed parameters: {err}")
            continue
        except TypeError:
            print("Invalid syntax")
            continue


def calculate_distance(p1: tuple[float, float, float],
                       p2: tuple[float, float, float]) -> float:
    try:
        dist: float = round(math.sqrt((p2[0]-p1[0])**2
                                      + (p2[1]-p1[1])**2
                                      + (p2[2]-p1[2])**2),
                            4)
        return dist
    except OverflowError as e:
        print(e)


def main() -> None:
    try:
        print("""=== Game Coordinate System ===\n
Get a first set of coordinates\n""")
        set1: tuple[float, float, float] = create_coords()
        print(f"""Got a first tuple: {set1}
It includes: X={set1[0]}, Y={set1[1]}, Z={set1[2]}")
Distance to center: {calculate_distance(set1, (0, 0, 0))}\n
Get a second set of coordinates""")
        set2: tuple[float, float, float] = create_coords()
        print(f"Distance between the 2 sets of coordinates: "
              f"{calculate_distance(set1, set2)}")
    except KeyboardInterrupt:
        print("\nThe user interrupted the program")
    except EOFError:
        print("\n The user interrupted the program")


if __name__ == "__main__":
    main()
