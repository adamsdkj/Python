#!/usr/bin/env python3

class Plant:
    """
    Represents a plant in the garden.

    Attributes:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """

    def __init__(self, name: str, height: int, ages: int):
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height in centimeters.
            age (int): Age in days.
        """
        self.name = name
        self.height = height
        self.ages = ages

    def grow(self, growth_per_day: int = 1):
        """
        Grows the plant's height

        Args:
            growth_per_day (int): growth in one day
        """
        self.height += growth_per_day

    def age(self, days: int, growth_per_day: int):
        """
        Ages the plant

        Args:
            days (int): how many days passed
            growth_per_day (int): growth in one day
        """
        growth = 0
        for i in range(days - 1):
            self.grow(growth_per_day)
            self.ages += 1
            growth += growth_per_day
        print(f"=== Day {days} ===")
        self.display()
        print(f"Growth this week: +{growth}cm")

    def get_info(self, days: int, growth_per_day):
        """
        Get the stats after passing an n days on the plant

        Args:
            days (int): how many days passed
            growth_per_day (int): growth in one day
        """
        print("=== Day 1 ===")
        self.display()
        self.age(days, growth_per_day)

    def display(self):
        """
        Display the plant's information in a readable format.
        """
        print(f"{self.name}: {self.height}cm, {self.ages} days old")


def disp(data: dict) -> dict:
    """
    Create and display thet stats of many plants

    Args:
        data (dict): the data of the plants
    """
    plants = {}
    i = 0
    print("=== Plant Factory Output ===")
    for key, attr in data.items():
        plants[key] = Plant(attr['name'], attr['height'],
                            attr['ages'])
        print(f"Created: {attr['name']} ({attr['height']}cm,", end='')
        print(f" {attr['ages']} days)")
        i += 1
    print(f"\nTotal plants created: {i}")
    return plants


if __name__ == "__main__":
    data = {
        "plant1": {"name": "Rose", "height": 25, "ages": 25},
        "plant2": {"name": "Sunflower", "height": 80, "ages": 20},
        "plant3": {"name": "Cactus", "height": 15, "ages": 120},
        "plant4": {"name": "Tulip", "height": 30, "ages": 15},
        "plant5": {"name": "Daisy", "height": 20, "ages": 10},
        "plant6": {"name": "Orchid", "height": 35, "ages": 18},
        "plant7": {"name": "Lavender", "height": 40, "ages": 22},
        "plant8": {"name": "Marigold", "height": 28, "ages": 12},
    }
    disp(data)
