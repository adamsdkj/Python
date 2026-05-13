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


def disp_stats(data: dict) -> dict:
    """
    Create and display thet stats of many plants

    Args:
        data (dict): the data of the plants
    """
    plants = {}
    for key, attr in data.items():
        plants[key] = Plant(attr['name'], attr['height'], attr['ages'])
        plants[key].get_info(attr['days'], attr['growth'])


if __name__ == "__main__":
    data = {
        "plant1": {
                    "name": "Rose",
                    "height": 25,
                    "ages": 25,
                    "days": 7,
                    "growth": 1}
    }
    disp_stats(data)
