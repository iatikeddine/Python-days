class Plant:
    """
    This base class stores common attributes shared by all plants,
    such as name, height, and age.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    Represents a flower plant.

    A Flower is a Plant with an additional color attribute
    and the ability to bloom.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower instance."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self):
        """
        Returns: A message describing the blooming state.
        """
        return f"{self.name} is blooming beautifully!"


class Tree(Plant):
    """
    Represents a tree.

    A Tree is a Plant with a trunk diameter and the ability
    to provide shade.
    """
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:

        """ Initialize a Tree instance."""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self):
        """
        Returns: A message describing the amount of shade produced.
        """
        return f"{self.name} provides 78 square meters of shade"


class Vegetable(Plant):
    """
    Represents a vegetable plant.

    A Vegetable is a Plant that has a harvest season
    and nutritional value.
    """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutrition_value: str):

        """Initialize a Vegetable instance."""
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutrition_value: str = nutrition_value


rose: Flower = Flower("Rose", 25, 30, "red")
sunflower: Flower = Flower("Sunflower", 80, 150, "yellow")

oak: Tree = Tree("Oak", 500, 1825, 50)
maple: Tree = Tree("Maple", 1500, 3650, 45)

tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
potato: Vegetable = Vegetable("Potato", 20, 60, "winter", "B")


if __name__ == "__main__":
    """
    Demonstrates different plant types and their unique behaviors.
    """
    print("=== Garden Plant Types ===")
    print()
    print(
        f"Rose (Flower): {rose.height}cm, {rose.age} days,"
        f"{rose.color} color"
    )
    print(rose.bloom())

    print()
    print(
        f"Oak (Tree): {oak.height}cm, {oak.age} days, "
        f"{oak.trunk_diameter}cm diameter"
    )
    print(oak.produce_shade())

    print()
    print(
        f"Tomato (Vegetable): {tomato.height}cm, "
        f"{tomato.age} days, {tomato.harvest_season} harvest"
    )
    print(f"Tomato is rich in vitamin {tomato.nutrition_value}")
