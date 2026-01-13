def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    for x in range(days):
        print("Day", i)
        i += 1
    print("Harvest time!")
