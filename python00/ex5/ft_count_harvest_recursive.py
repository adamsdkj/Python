def ft_count_harvest_recursive_helper(days, n):
    if (days == 0):
        return
    print("day", n)
    if (n == days):
        return
    ft_count_harvest_recursive_helper(days, n + 1)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_count_harvest_recursive_helper(days, 1)
    print("Harvest time!")
