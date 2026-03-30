def helper(current, days):
    if current > days:
        return
    print("Day", days)
    helper(current +1, days)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper(1,days)
    print("Harvest time!")
    ft_count_harvest_recursive()