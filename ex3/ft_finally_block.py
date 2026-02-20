class InvalidPlant(Exception):
    pass


def water_plants(plant_list: list) -> None:
    success = True
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None or plant == "":
                raise InvalidPlant("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except InvalidPlant as e:
        success = False
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print(e)
