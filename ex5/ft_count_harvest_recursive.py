def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def days_recurse(day) -> None:
        if day > days:
            return
        print("Day", day)
        days_recurse(day + 1)

    days_recurse(1)
    print("Harvest time")
