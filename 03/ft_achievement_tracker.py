import random


class Player():
    def __init__(self,
                 name: str,
                 achievements: set[str]) -> None:
        self._name = name
        self._achievements = achievements


    def get_name(self) -> str:
        return(self._name)


    def get_achievements(self) -> set[str]:
        return(self._achievements)

    def show_achievements(self) -> None:
        print(f"Player {self._name}: {self._achievements}")


def gen_player_achievements() -> set[str]:
    achievements: list[str] = ['Crafting Genius', 'Strategist', 'World Savior',
                              'Speed Runner', 'Survivor', 'Master Explorer',
                              'Treasure Hunter', 'Unstoppable', 'First Steps',
                              'Collector Supreme', 'Untouchable', 'Sharp Mind',
                              'Boss Slayer']
    p_achievements: set[str] = set() 
    for _ in range(0, random.randint(1, len(achievements))):
        p_achievements = p_achievements.union({random.choice(achievements)})
    return(p_achievements)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    p1 = Player("Alice", gen_player_achievements())
    p2 = Player("Bob", gen_player_achievements())
    p3 = Player("Charlie", gen_player_achievements())
    p4 = Player("Dylan", gen_player_achievements())
    p1.show_achievements()
    p2.show_achievements()
    p3.show_achievements()
    p4.show_achievements()
    print("\nAll distinct achievements: ", end="")
    print(p1.get_achievements().union(p2.get_achievements(),
                                             p3.get_achievements(),
                                             p4.get_achievements()))
    print("\nCommon achievements: ", end="")
    print(p1.get_achievements().intersection(p2.get_achievements(),
                                             p3.get_achievements(),
                                             p4.get_achievements()))
    print(f"\nOnly {p1.get_name()} has: ", end="")
    print(p1.get_achievements().difference(p2.get_achievements(),
                                           p3.get_achievements(),
                                           p4.get_achievements()))
    print(f"Only {p2.get_name()} has: ", end="")
    print(p2.get_achievements().difference(p1.get_achievements(),
                                           p3.get_achievements(),
                                           p4.get_achievements()))
    print(f"Only {p3.get_name()} has: ", end="")
    print(p3.get_achievements().difference(p2.get_achievements(),
                                           p3.get_achievements(),
                                           p4.get_achievements()))
    print(f"Only {p4.get_name()} has: ", end="")
    print(p4.get_achievements().difference(p1.get_achievements(),
                                           p3.get_achievements(),
                                           p4.get_achievements()))

if __name__ == "__main__":
    main()
