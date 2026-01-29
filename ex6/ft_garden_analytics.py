class GardenManager:
    gardens: list = []

    def add_garden(cls, garden) -> None:
        cls.gardens.append(garden)
    add_garden = classmethod(add_garden)

    def garden_report(garden) -> None:
        print(f"\n=== {garden.name}'s Garden Reports ===")
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"- {plant.describe_plant()}")

    class GardenStats:

        def get_stats(garden: "Garden") -> None:
            i: int = 0
            for plant in garden.plants:
                i += 1
            print(f"\nPlants added: {i}, Total growth: {i}cm")
        get_stats = staticmethod(get_stats)

        def get_types(garden) -> tuple:
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
            score: int = 0
            for plant in garden.plants:
                score += plant.get_points()
            return f"{garden.name}: {score}"

        def total_gardens() -> int:
            i: int = 0
            for garden in GardenManager.gardens:
                i += 1
            return i


class Garden:

    def __init__(self, garden_name: str) -> None:
        self.name: str = garden_name
        self.plants: list = []

    def add_plant(self, plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def plants_grow(self) -> None:
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def height_validation(self) -> bool:
        condition: bool = True
        for plant in self.plants:
            if plant.height < 0:Test scenarios:
                condition = False
        return condition


class Plant:

    def __init__(self, plant_name: str, plant_height: int) -> None:
        self.name: str = plant_name
        self.height: int = plant_height
        self.regular: int = 0

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def increment(self) -> tuple:
        self.regular += 1
        return (self.regular, 0, 0)

    def describe_plant(self) -> str:
        return f"{self.name}: {self.height}cm"
    
    def get_points(self):
        return 0


class FloweringPlant(Plant):

    def __init__(self, plant_name: str, plant_height: int,
                 plant_color: str) -> None:
        super().__init__(plant_name, plant_height)
        self.color: str = plant_color
        self.flowering: int = 0

    def describe_plant(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

    def increment(self) -> tuple:
        self.flowering += 1
        return (0, self.flowering, 0)

    def get_points(self):
        return 0


class PrizeFlower(FloweringPlant):
    def __init__(self, plant_name: str, plant_height: int, plant_color: str,
                 plant_points: int) -> None:
        super().__init__(plant_name, plant_height, plant_color)
        self.points: int = plant_points
        self.prize: int = 0

    def increment(self) -> tuple:
        self.prize += 1
        return (0, 0, self.prize)

    def describe_plant(self) -> str:
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
