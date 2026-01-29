class GardenError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class WaterError(GardenError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class SunError(GardenError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class GardenManager:
    plants = []

    @classmethod
    def add_plants(cls, plant):
        name = plant[0]
        success = True
        try:
            if name == "":
                raise PlantError("Error adding plant: Plant name "
                                 "cannot be empty!")
            else:
                cls.plants.append(plant)
                print(f"Added {name} successfully")
        except GardenError as e:
            success = False
            print(e)

    def water_plants(self, plants):
        print("Opening watering system")
        try:
            for plant in plants:
                print(f"Watering {plant[0]} - success")
        except:
            print("Error Encountered")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plants):
        for plant in plants:
            health = True
            try:
                if plant[1] < 1 or plant[1] > 10:
                    raise WaterError("Watering problem")
            except GardenError:
                health = False
                if plant[1] > 10:
                    print(f"Error checking {plant[0]}: Water level {plant[1]} is too high (max 10)")
                else:
                    print(f"Error checking {plant[0]}: Water level {plant[1]} is too low (min 1)")
            try:
                if plant[2] < 2 or plant[2] > 12:
                    raise WaterError("Sun problem")
            except GardenError:
                health = False
                if plant[2] > 12:
                    print(f"Error: {plant[0]} Sunlight hours {plant[2]} is too high (max 12)")
                else:
                    print(f"Error: {plant[0]} Sunlight hours {plant[2]} is too low (min 2)")
            if health:
                print(f"{plant[0]}: healthy (water: {plant[1]}, sun: {plant[2]})")


print("=== Garden Management System ===")
plant_list = [("tomato", 5, 8),("lettuce", 15, 7), ("", 9, 6)]

print("\nAdding plants to garden...")
for plant in plant_list:
    GardenManager.add_plants(plant)
manager = GardenManager()

print("\nWatering plants...")
manager.water_plants(GardenManager.plants)

print("\nChecking plant health...")
manager.check_plant_health(GardenManager.plants)

print("\nTesting error recovery...")
try:
    raise GardenError("Not enough water in tank")
except GardenError as e:
    print(f"Caught GardenError: {e}")
print("System recovered and continuing...")

print("\nGarden management system test complete!")