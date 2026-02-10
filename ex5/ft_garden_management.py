class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class SunError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, name: str, water: int, sun: int) -> None:
        if name == "" or name is None:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append({"name": name, "water": water, "sun": sun})
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant['name']} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str, water: int, sun: int) -> None:
        if water < 1 or water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        if sun < 2 or sun > 12:
            raise SunError(f"Sunlight hours {sun} is too low (min 2)")
        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    
    manager = GardenManager()
    
    print("\nAdding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
    except GardenError as e:
        print(f"Error adding plant: {e}")
    
    try:
        manager.add_plant("lettuce", 7, 6)
    except GardenError as e:
        print(f"Error adding plant: {e}")
    
    try:
        manager.add_plant("", 9, 6)
    except GardenError as e:
        print(f"Error adding plant: {e}")
    
    print("\nWatering plants...")
    manager.water_plants()
    
    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato", 5, 8)
    except GardenError as e:
        print(f"Error checking tomato: {e}")
    
    try:
        manager.check_plant_health("lettuce", 15, 7)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")
    
    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")
    
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()