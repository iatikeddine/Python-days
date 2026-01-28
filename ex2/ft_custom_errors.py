class GardenError(Exception):
    """ GadenError """
class PlantError(GardenError):
    """ GadenError """
class WaterError(GardenError):
    """ GadenError """
    
def catch_errors():
    print("=== Custom Garden Errors Demo ===\n")
    tomato_health = 5
    watering = 1
    try:
        print("Testing PlantError...")
        if tomato_health > 3:
            raise PlantError("plant error")
    except GardenError:
        print("Caught PlantError: The tomato plant is wilting!\n")

    try:
        print("Testing WaterError...")
        if watering < 3:
            raise WaterError("water error")
    except GardenError:
        print("Caught WaterError: Not enough water in the tank!\n")

    try:
        print("Testing catching all garden errors...")
        if tomato_health > 3 and watering < 3:
            raise GardenError("garden error")
    except GardenError:
        print("Caught a garden error: The tomato plant is wilting!\nCaught a garden error: Not enough water in the tank!\n")

    print("All custom error types work correctly!")

catch_errors()

