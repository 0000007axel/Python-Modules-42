class Plant:
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int) -> None:
        self._plant_name = plant_name
        self._plant_height = 0.0
        self._plant_age = 0

        self.set_height(plant_height)
        self.set_age(plant_age)

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._plant_name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._plant_height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._plant_name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = new_age

    def get_height(self) -> float:
        return self._plant_height

    def get_age(self) -> int:
        return self._plant_age

    def grow(self, grow_size: float) -> None:
        self.set_height(round((self._plant_height + grow_size), 1))

    def age(self, days: int) -> None:
        self.set_age(self._plant_age + days)

    def show(self) -> None:
        print(f"{self._plant_name.capitalize()}: ", end="")
        print(f"{self._plant_height}cm, {self._plant_age} days old")


class Flower(Plant):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int,
                 color: str) -> None:
        super().__init__(plant_name, plant_height, plant_age)
        self.color = color
        self.bloomstate = False
        print("=== Flower")

    def bloom(self) -> None:
        if self.bloomstate is False:
            print(f"[asking the {self._plant_name} to bloom]")
            self.bloomstate = True

        elif self.bloomstate is True:
            print(f" {self._plant_name.capitalize()} is blooming beautifully")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomstate is True:
            print(f" {self._plant_name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self._plant_name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int,
                 trunk_diameter: float):
        super().__init__(plant_name, plant_height, plant_age)
        self.trunk_diameter = trunk_diameter
        print("=== Tree")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm wide")

    def produce_shade(self) -> None:
        print(f"[asking the {self._plant_name} to produce shade]")
        print(f"Tree {self._plant_name.capitalize()} now produces", end="")
        print(f" a shade of {self.get_height()}cm long and ", end="")
        print(f"{self.trunk_diameter} wide.")


class Vegetable(Plant):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int,
                 harvest_season: str,):
        super().__init__(plant_name, plant_height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        print("=== Vegetable")

    def age(self, days: int) -> None:
        print(f"[make {self._plant_name.capitalize()} grow and age ", end="")
        print(f"for {days} days]")
        self.nutritional_value += days
        for i in range(0, days):
            self.grow(2.1)
        super().age(days)

    def show(self) -> None:
        super().show()
        print(f" Harvest_season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print("")
    tomato = Vegetable("tomato", 5.0, 10, "April")
    tomato.show()
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
