class GardenManager:
    """
    Manages multiple gardens and provides analytics
    using nested helper class."""
    gardens: list = []

    @classmethod
    def add_garden(cls, garden) -> None:
        """
         Add a garden to the manager's list of gardens.
        """
        cls.gardens.append(garden)

    def garden_report(garden) -> None:
        """
        Print a report of all plants in the given garden.
        """
        print(f"\n=== {garden.name}'s Garden Reports ===")
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"- {plant.describe_plant()}")

    class GardenStats:
        """Nested helper class for calculating garden statistics."""

        def get_stats(garden) -> None:
            """
            Print basic statistics about the plants in a garden.
            """
            i: int = 0
            for plant in garden.plants:
                i += 1
            print(f"\nPlants added: {i}, Total growth: {i}cm")

        def get_types(garden) -> tuple:
            """
            Count the types of plants in a garden.
            """
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            for plant in garden.plants:
                r, f, p = plant.increment()
                regular += r
                flowering += f
                prize += p

            return regular, flowering, prize

        def score_calculator(garden) -> str:
            """
            Calculate a prize score for a garden based on PrizeFlowers.
            """
            score: int = 0
            for plant in garden.plants:
                score += plant.get_points()
            return f"{garden.name}: {score}"

        def total_gardens() -> int:
            """
            Count the total number of gardens managed.
            """
            i: int = 0
            for garden in GardenManager.gardens:
                i += 1
            return i


class Garden:
    """Represents a garden containing multiple plants."""

    def __init__(self, garden_name: str) -> None:
        """
        Initialize a garden with a name and empty plant list.
        """
        self.name: str = garden_name
        self.plants: list = []

    def add_plant(self, plant) -> None:
        """
        Add a plant to the garden.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def plants_grow(self) -> None:
        """Increase the height of all plants in the garden by 1cm."""
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def height_validation(self) -> bool:
        """Validate that all plant heights are non-negative."""
        condition: bool = True
        for plant in self.plants:
            if plant.height < 0:
                condition = False
        return condition


class Plant:
    """Represents a basic plant with a name and height."""

    def __init__(self, plant_name: str, plant_height: int) -> None:
        """Initialize a plant with a name and height."""
        self.name: str = plant_name
        self.height: int = plant_height
        self.regular: int = 0

    def grow(self) -> None:
        """Increase the height of the plant by 1cm and print a message."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def increment(self) -> tuple:
        """Increment the plant type count for analytics."""
        self.regular += 1
        return (self.regular, 0, 0)

    def describe_plant(self) -> str:
        """Describe the plant for reporting."""
        return f"{self.name}: {self.height}cm"
    
    def get_points(self):
        return 0


class FloweringPlant(Plant):
    """Represents a flowering plant with a color."""

    def __init__(self, plant_name: str, plant_height: int,
                 plant_color: str) -> None:
        """Initialize a flowering plant with a color."""
        super().__init__(plant_name, plant_height)
        self.color: str = plant_color
        self.flowering: int = 0

    def describe_plant(self) -> str:
        """Describe the flowering plant."""
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

    def increment(self) -> tuple:
        """Increment the plant type count for analytics."""
        self.flowering += 1
        return (0, self.flowering, 0)

    def get_points(self):
        return 0


class PrizeFlower(FloweringPlant):
    """Represents a prize-winning flower with points."""
    def __init__(self, plant_name: str, plant_height: int, plant_color: str,
                 plant_points: int) -> None:
        """Initialize a prize flower with points."""
        super().__init__(plant_name, plant_height, plant_color)
        self.points: int = plant_points
        self.prize: int = 0

    def increment(self) -> tuple:
        """Increment the plant type count for analytics."""
        self.prize += 1
        return (0, 0, self.prize)

    def describe_plant(self) -> str:
        """Describe the prize flower."""
        return (
            f"{self.name}: {self.height}cm, {self.color} "
            f"flowers (blooming), Prize points: {self.points}"
        )

    def get_points(self):
        return self.points


if __name__ == "__main__":

    print("=== Garden Management System Demo ===\n")
    Alice: Garden = Garden("Alice")
    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)
    Alice.add_plant(oak)
    Alice.add_plant(rose)
    Alice.add_plant(sunflower)
    Alice.plants_grow()
    GardenManager.add_garden(Alice)
    GardenManager.garden_report(Alice)
    GardenManager.GardenStats.get_stats(Alice)
    r, f, p = GardenManager.GardenStats.get_types(Alice)
    Bob: Garden = Garden("Bob")
    orchid: PrizeFlower = PrizeFlower("Orchid", 45, "white", 30)
    Bob.add_plant(orchid)
    GardenManager.add_garden(Bob)
    print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers\n")
    print(f"Height Validation test: {Bob.height_validation()}")
    print(
        f"Garden scores - "
        f"{GardenManager.GardenStats.score_calculator(Alice)}, "
        f"{GardenManager.GardenStats.score_calculator(Bob)}"
    )
    print(
        f"Total gardens managed: "
        f"{GardenManager.GardenStats.total_gardens()}"
    )
