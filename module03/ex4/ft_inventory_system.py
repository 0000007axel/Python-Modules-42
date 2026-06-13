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
    inventory = {}
    if len(sys.argv) < 2:
        print("No arguments were passed")
        return(inventory)
        
    for arg in sys.argv[1:]:
        try:
            if ':' not in arg:
                raise ValueError(f"Invalid format for '{arg}'")
            key, value = arg.split(":")
            if key not in inventory:
                if not key and not value:
                    raise ValueError("No items were passed")
                elif not key:
                    raise ValueError(f"No item passed for quantity {value}")
                elif not value:
                    raise ValueError(f"No quantity passed for item {key}")
                for char in value:
                    if char not in "0123456789":
                        raise ValueError(f"Invalid value for item '{key}'")    
                if int(value) < 0:
                    raise ValueError(f"Quantity of item '{key}' is invalid")
                inventory[key] = int(value)
            else:
                print(f"Redundant item {key} - Discarding")
        except ValueError as e:
            print(e)
    return(inventory)


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    inventory: dict[str, int] = create_inventory()
    print(inventory)

if __name__ == "__main__":
    main()
