import sys


def create_inventory() -> dict[str, int]:

    pairs = sys.argv[1:]
    inventory: dict[str, int] = {}
    for pair in pairs:
        try:
            key: str = (pair.split(':'))[0]
            value: str = (pair.split(':'))[1]
            inventory.update({key: int(value)})
        except IndexError:
            print(f"Invalid parameter '{pair}'")
        except ValueError as err2:
            print(f"Quantity error for 'key': {err2}")
    print(inventory)
    return(inventory)


'''
def parser() -> list[str]:
    args: list[str] = sys.argv
    args.remove(args[0])
    print(args)
    for arg in arg:
        key, value = s.split(arg)

    return(args)
'''


def main() -> None:
    print("=== Inventory System Analysis ===")
    print(create_inventory())


if __name__ == "__main__":
    main()
