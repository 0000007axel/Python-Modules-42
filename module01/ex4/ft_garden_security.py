#!/usr/bin/env python3.13


class Plant:
    def __init__(self, plant_name: str, plant_height: float,
                 plant_age: int) -> None:
        self._plant_name = plant_name
        self._plant_height = 0.0
        self._plant_age = 0

        self.set_height(plant_height)
        self.set_age(plant_age)

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.get_name()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._plant_height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._plant_name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = new_age

    def get_name(self) -> str:
        return (self._plant_name)

    def get_height(self) -> float:
        return (self._plant_height)

    def get_age(self) -> int:
        return (self._plant_age)

    def grow(self, grow_size: float) -> None:
        self.set_height(round((self._plant_height + grow_size), 1))

    def age(self) -> None:
        self.set_age(self.get_age() + 1)

    def show(self) -> None:
        print(f"{self._plant_name}: "
              f"{self._plant_height}cm, {self._plant_age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant1.show()
    plant1.set_height(25)
    print(f"\nHeight updated: {plant1.get_height()}cm")
    plant1.set_age(30)
    print(f"Age updated: {plant1.get_age()}cm\n")
    plant1.set_height(-7)
    plant1.set_age(-25)
    print("\nCurrent state: ", end="")
    plant1.show()


if __name__ == "__main__":
    main()
