class GardenError(Exception):
    def __init__(self,
                 message : str = "Unknown Garden Error") -> None:
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self,
                 message : str = "Unknown Plant Error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self,
                 message : str = "Unkown Water Error") -> None:
        super().__init__(message)


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wailing!")

    except PlantError as err:
        print(f"Caught {type(err).__name__}: {err}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")

    except WaterError as err:
        print(f"Caught {type(err).__name__}: {err}")


    print("\nTesting catching all garden errors...")
    for i in range (2):
        try:
            if i == 0:
                raise GardenError("The tomato plant is wailing!")
            elif i == 1:
                raise GardenError("Not enough water in the tank!")
        except GardenError as err:
            print(f"Caught {type(err).__name__}: {err}")

    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    ft_custom_errors()
