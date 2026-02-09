class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def catch_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    tomato_health = 5
    watering = 1
    try:
        print("Testing PlantError...")
        if tomato_health > 3:
            raise PlantError("Caught PlantError: The tomato plant is wilting!")
    except GardenError as e:
        print(f"{e}\n")

    try:
        print("Testing WaterError...")
        if watering < 3:
            raise WaterError("Caught WaterError: Not enough water"
                             " in the tank!")
    except GardenError as e:
        print(f"{e}\n")

    print("Testing catching all garden errors...")
    try:
        if tomato_health > 3:
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        if watering < 3:
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print()
    print("All custom error types work correctly!")


catch_errors()
