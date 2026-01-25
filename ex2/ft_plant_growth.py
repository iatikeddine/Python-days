class Plant:
    """
    The Plant class stores basic plant information and provides
    methods to increase its age and height
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name: str = name
        self.height: int = height
        self.plant_age: int = age

    def age(self) -> None:
        """Increase plant age by 1 day"""
        self.plant_age += 1

    def grow(self) -> None:
        """Increase plant height by 1cm"""
        self.height += 1

    def get_info(self) -> str:
        """Returns Plant name, height and age"""
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


rose: Plant = Plant("Rose", 25, 30)

if __name__ == "__main__":
    print("=== Day 1 ===")
    print(rose.get_info())
    for x in range(6):
        rose.age()
        rose.grow()
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{x + 1}cm")
