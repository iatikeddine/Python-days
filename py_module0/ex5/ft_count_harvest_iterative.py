def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    i: int = 1
    for x in range(days):
        print("Day", i)
        i += 1
    print("Harvest time!")
