days = int(input("Days until harvest: "))

def count_recursive (day):
    i = 1
    if i < days:
        print("Day ", i)
    else:
        count_recursive(days-i)

count_recursive(days)