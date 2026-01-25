class Plant:
    """This class stores basic information shared by all plants"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


rose: Plant = Plant("Rose", 25, 30)
sunflower: Plant = Plant("Sunflower", 80, 45)
cactus: Plant = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
