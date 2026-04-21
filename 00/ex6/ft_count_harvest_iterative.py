def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: ")) + 1
    for i in range(1, days):
        print("Day", i)
    print("Harvest time!")
