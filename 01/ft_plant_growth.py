class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, height: int) -> None:
        for i in range(1, 7):
            self.height += 0.8
            print(f"{self.height}")

    def age(self, height: int) -> None:
        self.age += 1
        print(f"{self.age} days")

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")




def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Tulip", 20, 5)
    plant1.age()
    plant1.grow()
    plant.show()

if __name__ == "__main__":
    ft_plant_growth()
