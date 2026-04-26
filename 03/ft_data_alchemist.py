import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players_list: list[str] = ['Alice',
                               'bob',
                               'Charlie',
                               'dylan',
                               'Emma',
                               'Gregory',
                               'john',
                               'kevin',
                               'Liam']
    all_names: list[str] = [name.capitalize() for name in players_list]
    cap_names: list[str] = [name for name in players_list if name[0].isupper()]
    print(f"Initial list of players: {players_list}")
    print(f"New list with all names capitalized: {cap_names}")
    print(f"New list of capitalized names only: {all_names}\n")
    an_dict: dict[str, int] = {name: random.randint(0, 1000) for name in players_list }
    average: float = round(sum(an_dict.values()) / len(an_dict), 2)
    print(f"Score dict: {an_dict}")
    print(f"Score average: {average}")
    hi_dict: dict[str, int] = {name: an_dict[name] for name in an_dict if an_dict[name] > average}
    print(f"High scores: {hi_dict}")


if __name__ == "__main__":
    main()
