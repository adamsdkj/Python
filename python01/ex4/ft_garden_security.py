#!/usr/bin/env python3

class SecurePlant:
    """
    Plant with protected attributes.

    Attributes:
        _name (str): Name of the plant.
        _height (int): Height in centimeters.
        _age (int): Age in days.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a plant.

        Args:
            name (str): Plant name.
            height (int): Plant height in centimeters.
            age (int): Plant age in days.
        """
        self._name = name
        self._height = height
        self._age = age
        print(f"Plant created: {name}")

    def get_name(self):
        """
        Get plant name.

        Returns:
            int: Plant name.
        """
        return self._name

    def set_name(self, name: str):
        """
        Set plant name.

        Args:
            name (str): Plant name.
        """
        self._name = name

    def get_height(self):
        """
        Get plant height.

        Returns:
            int: Plant height.
        """
        return self._height

    def set_height(self, height: int):
        """
        Set plant height.

        Args:
            height (int): New height in centimeters.
        """
        if height < 0:
            return print(
                f"\nInvalid operation attempted: height {height}cm [REJECTED]"
                f"\nSecurity: Negative height rejected\n"
                f"\nCurrent plant: {self._name} ({self._height}cm,"
                f" {self._age} days)"
            )
        self._height = height
        print(f"Height updated: {height}cm [OK]")

    def get_age(self):
        """
        Get plant age.

        Returns:
            int: Plant age.
        """
        return self._age

    def set_age(self, age: int):
        """
        Set plant age.

        Args:
            age (int): New age in days.
        """
        if age < 0:
            return print(
                f"\nInvalid operation attempted: age {age} days [REJECTED]"
                f"\nSecurity: Negative age rejected"
                f"\nCurrent plant: {self._name} ({self._height}cm,"
                f" {self._age} days)"
            )
        self._age = age
        print(f"Age updated: {age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("rose", 20, 12)
    plant.set_age(20)
    plant.set_height(20)
    plant.set_height(-5)
