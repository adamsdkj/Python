#!/usr/bin/env python3

class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when a plant is in an invalid state, e.g., wilting."""
    pass


class WaterError(GardenError):
    """Raised when the water supply in the tank is insufficient."""
    pass


class Plant:
    """Represents a plant in the garden."""
    name: str
    state: str

    def __init__(self, name: str, state: str) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            state (str): State of the plant (e.g., 'healthy', 'wilting').
        """
        self.name = name
        self.state = state


class Tank:
    """Represents a water tank."""
    supply: int

    def __init__(self, supply: int) -> None:
        """
        Initialize a Tank instance.

        Args:
            supply (int): Amount of water in the tank.
        """
        self.supply = supply


def check_plant(plant: Plant) -> None:
    """
    Raise PlantError if the plant is wilting.

    Args:
        plant (Plant): Plant instance to check.

    Raises:
        PlantError: If the plant's state is 'wilting'.
    """
    if plant.state == "wilting":
        raise PlantError()


def check_water(tank: Tank) -> None:
    """
    Raise WaterError if the tank's water supply is zero.

    Args:
        tank (Tank): Tank instance to check.

    Raises:
        WaterError: If the tank supply is 0.
    """
    if tank.supply == 0:
        raise WaterError()


def check_plant_error(plant: Plant) -> None:
    """
    Test handling PlantError with a try/except block.

    Args:
        plant (Plant): Plant instance to test.
    """
    try:
        print("\nTesting PlantError...")
        check_plant(plant)
    except PlantError:
        print(f"Caught PlantError: The {plant.name} plant is wilting!")


def check_tank_error(tank: Tank) -> None:
    """
    Test handling WaterError with a try/except block.

    Args:
        tank (Tank): Tank instance to test.
    """
    try:
        print("\nTesting WaterError...")
        check_water(tank)
    except WaterError:
        print("Caught WaterError: Not enough water in the tank!")


def check_garden(plant: Plant, tank: Tank) -> None:
    """
    Test catching all garden errors using the base GardenError.

    Args:
        plant (Plant): Plant instance to test.
        tank (Tank): Tank instance to test.
    """
    print("\nTesting catching all garden errors...")
    try:
        check_plant(plant)
    except GardenError:
        print(f"Caught a garden error: The {plant.name} plant is wilting!")

    try:
        check_water(tank)
    except GardenError:
        print("Caught a garden error: Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    tomato = Plant("tomato", "wilting")
    tank = Tank(0)
    check_plant_error(tomato)
    check_tank_error(tank)
    check_garden(tomato, tank)
    print("\nAll custom error types work correctly!")
