class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age += 1
        self.grow()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")




def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Tulip", 20, 5)
    for i in range(1, 7)
        plant1.age()
        plant1.grow()
        plant.show()

if __name__ == "__main__":
    ft_plant_growth()
