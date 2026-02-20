class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def catch_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    tomato_health = "lol"
    watering = 1
    try:
        print("Testing PlantError...")
        if tomato_health > 3:
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        if watering < 3:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        if tomato_health > 3:
            raise PlantError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        if watering < 3:
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    try:
        catch_errors()
    except Exception as e:
        print(e)
