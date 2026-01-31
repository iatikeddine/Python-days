class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def describe(self) -> str:
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        return f"{self.name} provides 78 square meters of shade"

    def describe(self) -> str:
        return (
            f"{self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
            )


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutrition_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrition_value = nutrition_value

    def describe(self) -> str:
        return (
            f"{self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
            )


rose = Flower("Rose", 25, 30, "red")
sunflower = Flower("Sunflower", 80, 150, "yellow")

oak = Tree("Oak", 500, 1825, 50)
maple = Tree("Maple", 1500, 3650, 45)

tomato = Vegetable("Tomato", 80, 90, "summer", "C")
potato = Vegetable("Potato", 20, 60, "winter", "B")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    print(f"Rose (Flower): {rose.describe()}, {rose.color} color")
    print(rose.bloom())
    print(f"Sunflower (Flower): {sunflower.describe()}, "
          f"{sunflower.color} color")
    print(sunflower.bloom())

    print()
    print(f"Oak (Tree): {oak.describe()}")
    print(oak.produce_shade())
    print(f"Maple (Tree): {maple.describe()}")
    print(maple.produce_shade())

    print()
    print(f"Tomato (Vegetable): {tomato.describe()}")
    print(f"Tomato is rich in vitamin {tomato.nutrition_value}")
    print(f"Potato (Vegetable): {potato.describe()}")
    print(f"Potato is rich in vitamin {potato.nutrition_value}")
