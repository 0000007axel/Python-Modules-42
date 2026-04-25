import sys


def create_inventory() -> dict[str, int]:
    pairs = sys.argv[1:]
    inventory: dict[str, int] = {}
    for pair in pairs:
        try:
            key: str = (pair.split(':'))[0]
            if key in inventory.keys():
                print(f"Redundant item: '{key}' - discarding")
                continue
            value: int = int((pair.split(':'))[1])
            inventory.update({key: value})
        except IndexError:
            print(f"Error - invalid parameter '{pair}'")
        except ValueError as err2:
            print(f"Quantity error for 'key': {err2}")
    print(f"Got inventory: {inventory}")
    return(inventory)


def main() -> None:
    print("=== Inventory System Analysis ===")
    create_inventory()

if __name__ == "__main__":
    main()
