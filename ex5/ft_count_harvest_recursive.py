def ft_count_harvest_recursive(i=1, days=0):
    if days == 0:
        days = int(input("Days until harvest: "))
    if i > days:
        print("Harvest time!")
        return
    print("Day", i)
    ft_count_harvest_recursive(i + 1, days)
