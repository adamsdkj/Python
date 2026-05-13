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

    def information(self):
        """
        Return basic plant information.

        Returns:
            str: Plant height and age.
        """
        return f"{self.height}cm, {self.age} days"


class Flower(Plant):
    """
    Represents a flower.

    Attributes:
        color (str): Color of the flower.
    """

    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Initialize a Flower instance.

        Args:
            name (str): Name of the flower.
            height (int): Height in centimeters.
            age (int): Age in days.
            color (str): Color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Display blooming message."""
        print(f"{self.name} is blooming beautifully!")

    def disp(self):
        """Display flower information."""
        print(
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.information()}, {self.color} color"
        )


class Tree(Plant):
    """
    Represents a tree.

    Attributes:
        trunk_diameter (int): Trunk diameter in centimeters.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ):
        """
        Initialize a Tree instance.

        Args:
            name (str): Name of the tree.
            height (int): Height in centimeters.
            age (int): Age in days.
            trunk_diameter (int): Trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculate and display trunk surface area.

        Returns:
            None
        """
        area = (3.14 * self.height * self.trunk_diameter) / 10000
        print(f"{self.name} provides {area:.2f} square meters of shade")

    def disp(self):
        """Display tree information."""
        print(
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.information()}, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """
    Represents a vegetable.

    Attributes:
        harvest_season (str): Harvest season.
        nutritional_value (str): Main vitamin content.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ):
        """
        Initialize a Vegetable instance.

        Args:
            name (str): Name of the vegetable.
            height (int): Height in centimeters.
            age (int): Age in days.
            harvest_season (str): Harvest season.
            nutritional_value (str): Vitamin content.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutrition(self):
        """Display nutritional information."""
        print(
            f"{self.name} is rich in vitamin {self.nutritional_value}"
        )

    def disp(self):
        """Display vegetable information."""
        print(
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.information()}, {self.harvest_season} harvest"
        )


def display(data: dict):
    """
    Create plant objects and display their details.

    Args:
        data (dict): Dictionary containing plant data.
    """
    plants = {}

    for plant_type, info in data.items():
        print()

        if plant_type == "Flower":
            plants[info["object"]] = Flower(
                info["name"],
                info["height"],
                info["age"],
                info["color"],
            )
            plants[info["object"]].disp()
            plants[info["object"]].bloom()

        elif plant_type == "Tree":
            plants[info["object"]] = Tree(
                info["name"],
                info["height"],
                info["age"],
                info["diameter"],
            )
            plants[info["object"]].disp()
            plants[info["object"]].produce_shade()

        else:
            plants[info["object"]] = Vegetable(
                info["name"],
                info["height"],
                info["age"],
                info["harvest"],
                info["vitamin"],
            )
            plants[info["object"]].disp()
            plants[info["object"]].nutrition()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    data = {
        "Flower": {
            "object": "f1",
            "name": "Rose",
            "height": 25,
            "age": 25,
            "color": "red",
        },
        "Tree": {
            "object": "t1",
            "name": "Oak",
            "height": 500,
            "age": 1825,
            "diameter": 50,
        },
        "Vegetable": {
            "object": "v1",
            "name": "Tomato",
            "height": 80,
            "age": 90,
            "harvest": "summer",
            "vitamin": "C",
        },
    }
    display(data)
