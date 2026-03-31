def recursive_engine(day, max_days):
    if day <= max_days:
        print("Day ", day)
        recursive_engine(day + 1, max_days)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive():
    max_days = int(input("Days until harvest: "))
    recursive_engine(1, max_days)
