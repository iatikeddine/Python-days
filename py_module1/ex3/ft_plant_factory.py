class Plant:
    total: int = 0

    def __init__(self, name: str, starting_height: int,
                 starting_age: int) -> None:
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
        print(f"Created: {name} ({starting_height}cm, {starting_age} days)")
        Plant.total += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    print()
    print(f"Total plants created: {Plant.total}")
