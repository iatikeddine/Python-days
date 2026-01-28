def check_plant_health(plant_name, water_level, sunlight_hours):
    healthy = True
    try:
        if plant_name == "":
            raise ValueError("Invalid Plant Name")
    except ValueError:
        healthy = False
        print("Error: Plant name cannot be empty!")
    
    try:
        if water_level < 1 or water_level > 10:
            raise ValueError("Bad Water Level")
            healthy = False
    except ValueError:
        healthy = False
        print(f"Error: Water level {water_level} is too high (max 10)")

    try:
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError("Bad Sunlight")
            healthy = False
    except ValueError:
        healthy = False
        print(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")

    if healthy:
        print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 5, 7)

    print("\nTesting empty plant name...")
    check_plant_health("", 5, 7)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 7)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)

    print("\nAll error raising tests completed!")

test_plant_checks()
    