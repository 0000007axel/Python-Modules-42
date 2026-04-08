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
        print(f"{self.plant_name}: {self.plant_height}cm, {self.plant_age} days old")

def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Roses", 25.0, 30)
    original_height = plant1.plant_height
    plant1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.grow(0.8)
        plant1.age()
        plant1.show()
    print(f"Growth this week : {round((plant1.plant_height - original_height), 1)}cm")

if __name__ == "__main__":
    ft_plant_growth()
