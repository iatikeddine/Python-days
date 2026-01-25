class Plant:
    """
    This class stores basic plant information such as name, height,
    and age, and keeps a count of how many Plant objects have been created.
    """
    total: int = 0

    def __init__(self, name: str, starting_height: int,
                 starting_age: int) -> None:
        """
        Initialize a Plant instance and prints a custom message
        for created plants
        """
        self.name: str = name
        self.starting_height: int = starting_height
        self.starting_age: int = starting_age
        print(f"Created: {name} ({starting_height}cm, {starting_age} days)")
        Plant.total += 1


if __name__ == "__main__":
    """
    Creates several Plant instances and displays
    the total number of plants created.
    """
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print()
    print(f"Total plants created: {Plant.total}")
