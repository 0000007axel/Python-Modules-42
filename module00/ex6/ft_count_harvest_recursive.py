def recursive_engine(day: int, max_days: int) -> None:
    if day <= max_days:
        print("Day ", day)
        recursive_engine(day + 1, max_days)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive() -> None:
    max_days = int(input("Days until harvest: "))
    recursive_engine(1, max_days)
