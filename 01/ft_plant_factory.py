class Plant:
    def __init__(self, plant_name: str, plant_height: float, plant_age: int) -> None:
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

    def grow(self, grow_size : float) -> None:
        self.plant_height = round((self.plant_height + grow_size), 1)

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"Created: {self.plant_name}: {self.plant_height}cm, {self.plant_age} days old")

def ft_plant_factory() -> None:
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflower", 80, 45)
    plant5 = Plant("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()

if __name__ == "__main__":
    ft_plant_factory()