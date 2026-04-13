class Plant:
    def __init__(self, plant_name: str,
                 plant_height: float,
                 plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age
        print("Created: ", end="")
        self.show()

    def grow(self, grow_size: float) -> None:
        self.plant_height = round((self.plant_height + grow_size), 1)

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"{self.plant_name}:", end="")
        print(f"{self.plant_height}cm, {self.plant_age} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)


if __name__ == "__main__":
    ft_plant_factory()
