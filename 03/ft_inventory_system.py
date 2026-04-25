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
    return (inventory)


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = create_inventory()
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items:"
          f" {sum(inventory.values())}")
    max_min: tuple[int, int] = (max(inventory.values()),
                                min(inventory.values()))
    max_key: str = ""
    min_key: str = ""
    for item in inventory:
        print(f"Item {item} represents"
              f" {round(inventory[item] * 100 / sum(inventory.values()), 1)}%")
        if inventory[item] == max_min[0]:
            max_key = item
        elif inventory[item] == max_min[1]:
            min_key = item
    print(f"Item most abundant: {max_key} with quantity {inventory[max_key]}")
    print(f"Item least abundant: {min_key} with quantity {inventory[min_key]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
