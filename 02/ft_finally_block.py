class GardenError(Exception):
    def __init__(self,
                 message : str = "Unknown Garden Error") -> None:
        self.message = message
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self,
                 message : str = "Unknown Plant Error") -> None:
        super().__init__(message)



def water_plant(plant_name : str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing valid plants ...")
    try:
        print("Opening watering system")
        for i in ['Tomato', 'Lettuce', 'Carrots']:
            water_plant(i)
    except PlantError as err:
        print(f"Caught {type(err).__name__}: {err}")
        print("...ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants ...")
    try:
        print("Opening watering system")
        for i in ['Tomato', 'lettuce', 'Carrots']:
            water_plant(i)
    except PlantError as err:
        print(f"Caught {type(err).__name__}: {err}")
        print("...ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()
