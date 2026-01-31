class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def age(self) -> None:
        self.plant_age += 1

    def grow(self) -> None:
        self.height += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 120, 250)

if __name__ == "__main__":
    print("=== Day 1 ===")
    print(rose.get_info())
    print(sunflower.get_info())
    for x in range(6):
        rose.age()
        rose.grow()
        sunflower.age()
        sunflower.grow()
    print("=== Day 7 ===")
    print(rose.get_info())
    print(sunflower.get_info())
    print(f"Growth this week: +{x + 1}cm")
