class GardenManager:
    gardens: list = []

    def create_garden_network(cls, garden: "Garden") -> None:
        cls.gardens.append(garden)
    create_garden_network = classmethod(create_garden_network)

    def garden_report(garden: "Garden") -> None:
        print(f"\n=== {garden.name}'s Garden Reports ===")
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"- {plant.describe_plant()}")
    garden_report = staticmethod(garden_report)

    class GardenStats:

        def get_stats(garden: "Garden") -> None:
            i = 0
            for plant in garden.plants:
                i += 1
            print(f"\nPlants added: {i}, Total growth: {i}cm")
        get_stats = staticmethod(get_stats)

        def get_types(garden: "Garden") -> tuple:
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                r, f, p = plant.increment()
                regular += r
                flowering += f
                prize += p
            return regular, flowering, prize
        get_types = staticmethod(get_types)

        def score_calculator(garden: "Garden") -> str:
            score = 0
            for plant in garden.plants:
                score += plant.get_points()
            return f"{garden.name}: {score}"
        score_calculator = staticmethod(score_calculator)

        def total_gardens() -> int:
            i = 0
            for garden in GardenManager.gardens:
                i += 1
            return i
        total_gardens = staticmethod(total_gardens)


class Garden:

    def __init__(self, garden_name: str) -> None:
        self.name = garden_name
        self.plants = []

    def add_plant(self, plant: "Plant") -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def plants_grow(self) -> None:
        print(f"\n{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def height_validation(self) -> bool:
        condition = True
        for plant in self.plants:
            if plant.height < 0:
                condition = False
        return condition


class Plant:

    def __init__(self, plant_name: str, plant_height: int) -> None:
        self.name = plant_name
        self.height = plant_height
        self.regular = 0

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def increment(self) -> tuple:
        self.regular += 1
        return (self.regular, 0, 0)

    def describe_plant(self) -> str:
        return f"{self.name}: {self.height}cm"

    def get_points(self) -> int:
        return 0


class FloweringPlant(Plant):

    def __init__(self, plant_name: str, plant_height: int,
                 plant_color: str) -> None:
        super().__init__(plant_name, plant_height)
        self.color = plant_color
        self.flowering = 0

    def describe_plant(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

    def increment(self) -> tuple:
        self.flowering += 1
        return (0, self.flowering, 0)

    def get_points(self) -> int:
        return 0


class PrizeFlower(FloweringPlant):
    def __init__(self, plant_name: str, plant_height: int, plant_color: str,
                 plant_points: int) -> None:
        super().__init__(plant_name, plant_height, plant_color)
        self.points = plant_points
        self.prize = 0

    def increment(self) -> tuple:
        self.prize += 1
        return (0, 0, self.prize)

    def describe_plant(self) -> str:
        return (
            f"{self.name}: {self.height}cm, {self.color} "
            f"flowers (blooming), Prize points: {self.points}"
        )

    def get_points(self) -> int:
        return self.points

def garden_summary(garden: Garden) -> None:
    print(f"\nGarden summary for {garden.name}")
    i = 0
    for plant in garden.plants:
        i += 1
    print(f"Plants Total: {i} plants")


if __name__ == "__main__":

    print("=== Garden Management System Demo ===\n")

    Alice = Garden("Alice")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    Alice.add_plant(oak)
    Alice.add_plant(rose)
    Alice.add_plant(sunflower)
    Alice.plants_grow()

    GardenManager.create_garden_network(Alice)
    GardenManager.garden_report(Alice)
    GardenManager.GardenStats.get_stats(Alice)

    Bob = Garden("Bob")
    orchid = PrizeFlower("Orchid", 45, "white", 30)
    Bob.add_plant(orchid)
    GardenManager.create_garden_network(Bob)

    r, f, p = GardenManager.GardenStats.get_types(Alice)

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

    garden_summary(Alice)
