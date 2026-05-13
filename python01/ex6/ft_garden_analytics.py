#!/usr/bin/env python3


class Plant:
    """
    Represents a plant in the garden.

    Attributes:
        name (str): Name of the plant.
        height (int): Height in centimeters.
        age (int): Age in days.
    """

    def __init__(self, name: str, height: int, age: int):
        """Initialize a Plant."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth_per_day: int = 1) -> None:
        """Increase plant height."""
        self.height += growth_per_day

    def __str__(self) -> str:
        """Return readable plant string."""
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    Represents a flowering plant.

    Attributes:
        color (str): Flower color.
        blooming (bool): Blooming state.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        blooming: bool = True,
    ):
        """
        Initialize a FloweringPlant.

        Args:
            blooming (bool): Blooming state (default: True).
        """
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming

    def __str__(self) -> str:
        """Return readable flowering plant string."""
        state = "blooming" if self.blooming else "not blooming"
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers ({state})"
        )


class PrizeFlower(FloweringPlant):
    """
    Represents a prize-winning flower.

    Attributes:
        prize (int): Prize points.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize: int,
        blooming: bool = True,
    ):
        """
        Initialize a PrizeFlower.

        Args:
            blooming (bool): Blooming state (default: True).
        """
        super().__init__(name, height, age, color, blooming)
        self.prize = prize

    def __str__(self) -> str:
        """Return readable prize flower string."""
        state = "blooming" if self.blooming else "not blooming"
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers ({state}), "
            f"Prize points: {self.prize}"
        )


class Garden:
    """Represents a garden."""

    def __init__(self, owner: str, plants=None):
        """Initialize a Garden."""
        self.owner = owner
        self.plants = plants if plants is not None else []

        self.total_growth = 0
        self.plant_count = 0
        self.regular = 0
        self.flowering = 0
        self.prize_flowers = 0
        self.score = 0
        self.growth = 0

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner.capitalize()}'s garden")

    def grow_plants(self, growth: int = 1) -> None:
        """Grow all plants."""
        if growth < 0:
            print("Invalid: growth must be non-negative.")
            return

        print(f"\n{self.owner.capitalize()} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(growth)
            print(f"{plant.name} grew {growth}cm")
            self.growth += growth

    def stats(self) -> int:
        """
        Calculate garden statistics and score.

        Scoring:
        - All plants: +height
        - Blooming Flower: +10
        - Blooming Prize Flower: +20 + prize
        """
        self.total_growth = 0
        self.plant_count = 0
        self.regular = 0
        self.flowering = 0
        self.prize_flowers = 0
        self.score = 0

        for plant in self.plants:
            self.plant_count += 1
            self.total_growth += plant.height
            self.score += plant.height

            if isinstance(plant, PrizeFlower):
                self.prize_flowers += 1
                self.score += plant.prize
                if plant.blooming:
                    self.score += 20

            elif isinstance(plant, FloweringPlant):
                self.flowering += 1
                if plant.blooming:
                    self.score += 10

            else:
                self.regular += 1

        return self.score


class GardenManager:
    """Manages gardens and reports."""

    def __init__(self, garden: Garden):
        """Initialize GardenManager."""
        self.garden = garden
        self.garden.stats()

    def report(self) -> None:
        """Print garden report."""
        print(f"\n=== {self.garden.owner.capitalize()}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.garden.plants:
            print(plant)

    def plant_count(self) -> None:
        """Print garden statistics."""
        print(
            f"\nPlants added: {self.garden.plant_count}, "
            f"Total growth: {self.garden.growth}cm"
        )
        print(
            f"Plant types: {self.garden.regular} regular, "
            f"{self.garden.flowering} flowering, "
            f"{self.garden.prize_flowers} prize flowers"
        )

    @classmethod
    def height_validation_score(cls, gardens: list) -> None:
        """Validate garden height and get scores."""
        for garden in gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    print("\nHeight validation test: False")
                    return
        print("\nHeight validation test: True")
        print("Garden scores -", end="")

        count = 0
        total = 0
        for _ in gardens:
            total += 1

        for garden in gardens:
            garden.stats()
            count += 1
            print(f" {garden.owner}: {garden.score}", end="")
            if count != total:
                print(",", end="")

        print(f"\nTotal gardens managed: {total}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    oak = Plant("Oak Tree", 100, 20)

    rose = FloweringPlant(
        "Rose",
        25,
        20,
        "red",
        True,
    )

    sunflower = PrizeFlower(
        "Sunflower",
        50,
        20,
        "yellow",
        10,
        True,
    )

    alice = Garden("Alice")
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_plants()

    bob = Garden("Bob", [Plant("Oak Tree", 92, 20)])

    alice_manager = GardenManager(alice)
    alice_manager.report()
    alice_manager.plant_count()

    bob_manager = GardenManager(bob)
    GardenManager.height_validation_score([alice, bob])
