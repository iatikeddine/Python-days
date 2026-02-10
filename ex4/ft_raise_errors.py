def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str | None:
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    
    if water_level < 1 or water_level > 10:
        raise ValueError(
            f"Water level {water_level} is too "
            f"high (max 10)")
    
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} "
            f"is too low (min 2)")
    
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")
    
    print("Testing good values...")
    print(check_plant_health("tomato", 5, 7))
    
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 7)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 7)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
