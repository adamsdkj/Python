#!/usr/bin/env python3

class Plant:
    """
    Represents a plant in the garden.

    Attributes:
        name (str): Name of the plant.
        height (int): Height of the plant in centimeters.
        age (int): Age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height in centimeters.
            age (int): Age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        """
        Display the plant's information in a readable format.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def disp(data: dict) -> dict:
    """
    Create Plant instances from a dictionary and display them.

    Args:
        data (dict): Dictionary where each key maps to a dictionary
                     containing plant attributes (name, height, age).

    Returns:
        dict: A dictionary mapping the same keys to Plant objects.
    """
    plants = {}
    print(" === Garden Plant Registry ===")
    for key, attrs in data.items():
        plants[key] = Plant(attrs["name"], attrs["height"], attrs["age"])
        plants[key].display()

    return plants


if __name__ == "__main__":
    data = {
        "plant1": {"name": "Rose", "height": 25, "age": 30},
        "plant2": {"name": "Sunflower", "height":  80, "age": 45},
        "plant3": {"name": "Cactus", "height":  15, "age": 120}
    }
    disp(data)
