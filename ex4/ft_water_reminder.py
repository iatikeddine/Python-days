def ft_water_reminder():
    last_watering = int(input("Days since last watering: "))
    if last_watering <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
