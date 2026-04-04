class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, height: int) -> None:
        for i in range(1, 7):

    def age(self, height: int) -> None:

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")




def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")

if __name__ == "__main__":

    ft_plant_growth()