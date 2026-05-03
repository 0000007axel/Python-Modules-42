#!/usr/bin/env python3.13


import sys


def find_max(usr_dict: dict[str, int]) -> int:
    max_value: int = 0
    for value in usr_dict.values():
        if value > max_value:
            max_value = value
    return (max_value)


def find_min(usr_dict: dict[str, int]) -> int:
    min_value: int = find_max(usr_dict)
    for value in usr_dict.values():
        if value < min_value:
            min_value = value
    return (min_value)


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
    max_min: tuple[int, int] = (find_max(inventory),
                                find_min(inventory))
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
