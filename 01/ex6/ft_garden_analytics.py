class Plant:
    class Count:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def grow_up(self) -> None:
            self._grow_count += 1

        def age_up(self) -> None:
            self._age_count += 1

        def show_up(self) -> None:
            self._show_count += 1

        def get_age_count(self) -> int:
            return self._age_count

        def get_grow_count(self) -> int:
            return self._grow_count

        def get_show_count(self) -> int:
            return self._show_count

        def display_stats(self, plant: 'Plant') -> None:
            print(f"[statistics for {plant.get_name().capitalize()}]")
            print(f"Stats: {plant._counter.get_grow_count()} grow, ", end="")
            print(f"{plant._counter.get_age_count()} age, ", end="")
            print(f"{plant._counter.get_show_count()} show")

    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int) -> None:
        self._plant_height = 0.0
        self._plant_age = 0
        self._plant_name = plant_name
        self.set_height(plant_height)
        self.set_age(plant_age)
        self._counter = self.Count()

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

    def get_name(self) -> str:
        return self._plant_name

    def get_height(self) -> float:
        return self._plant_height

    def get_age(self) -> int:
        return self._plant_age

    def grow(self, grow_size: float) -> None:
        self._counter.grow_up()
        self.set_height(round((self._plant_height + grow_size), 1))

    def age(self, days: int) -> None:
        self._counter.age_up()
        self.set_age(self._plant_age + days)

    def show(self) -> None:
        self._counter.show_up()
        print(f"{self._plant_name.capitalize()}: ", end="")
        print(f"{self._plant_height}cm, {self._plant_age} days old")

    def show_stats(self) -> None:
        self._counter.display_stats(self)

    @staticmethod
    def is_year(x: int) -> bool:
        if x > 365:
            return True
        else:
            return False

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        unknown = cls("unknown plant", 0.0, 0)
        return unknown


class Flower(Plant):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int,
                 color: str) -> None:
        super().__init__(plant_name, plant_height, plant_age)
        self._color = color
        self._bloomstate = False

    def bloom(self) -> None:
        if self._bloomstate is True:
            print(f" {self._plant_name.capitalize()} is blooming beautifully")

        else:
            print(f"[asking the {self._plant_name} to bloom]")
            self._bloomstate = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomstate is True:
            print(f" {self.get_name().capitalize()} is blooming beautifully!")
        else:
            print(f" {self.get_name().capitalize()} has not bloomed yet")

    def grow_bloom(self, grow_size: float) -> None:
        print(f"[asking the {self.get_name()} to grow and bloom]")
        super().grow(grow_size)
        if self._bloomstate is True:
            print(f" {self._plant_name.capitalize()} is blooming beautifully")

        else:
            self._bloomstate = True


class Seed(Flower):
    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int,
                 color: str) -> None:
        super().__init__(plant_name, plant_height, plant_age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 42

    def grow_age_bloom(self, grow_size: float, days: int) -> None:
        print(f"[make {self.get_name()} grow, age and bloom]")
        super().grow(grow_size)
        super().age(days)
        self.bloom()

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    class Count(Plant.Count):
        def __init__(self):
            super().__init__()
            self._shade_produced = 0

        def get_shade(self) -> int:
            return self._shade_produced

        def add_shade(self) -> None:
            self._shade_produced += 1

        def display_stats(self, plant: 'Plant') -> None:
            super().display_stats(plant)
            print(f"Shade: {self.get_shade()}")

    def __init__(self,
                 plant_name: str,
                 plant_height: float,
                 plant_age: int,
                 trunk_diameter: float):
        super().__init__(plant_name, plant_height, plant_age)
        self.trunk_diameter = trunk_diameter
        self._counter = Tree.Count()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm wide")

    def produce_shade(self) -> None:
        self._counter.add_shade()
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


def display_plant_stats(plant: Plant) -> None:
    plant.show_stats()


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_year(400)}")

    print("\n=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    rose.grow_bloom(8.0)
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    sunflower.grow_age_bloom(30.0, 20)
    sunflower.show()
    display_plant_stats(sunflower)
    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_plant_stats(unknown)


if __name__ == "__main__":
    ft_garden_analytics()
