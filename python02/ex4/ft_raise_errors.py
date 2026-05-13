#!/usr/bin/env python3


class InvalidHandle(Exception):
    """Base class for garden-related validation errors."""

    pass


class InvalidName(InvalidHandle):
    """Raised when a plant name is invalid or empty."""

    pass


class InvalidWaterLevel(InvalidHandle):
    """Raised when the water level is not between 1 and 10."""

    pass


class InvalidSunlightHours(InvalidHandle):
    """Raised when sunlight hours are not between 2 and 12."""

    pass


def check_name(name: str) -> None:
    """
    Check if the plant name is valid.

    Args:
        name (str): The name of the plant.

    Raises:
        InvalidName: If the name is None or empty.
    """
    if not name:
        raise InvalidName("Error: Plant name cannot be empty!")


def check_water_level(level: int) -> None:
    """
    Checks if water level is reasonable (between 1 and 10).

    Args:
        level (int): The water level to check.

    Raises:
        InvalidWaterLevel: If level is outside the [1, 10] range.
    """
    if not (1 <= level <= 10):
        m = f"Error: Water level {level} is too high (max 10)"
        raise InvalidWaterLevel(m)


def check_sunlight_hours(hours: int) -> None:
    """
    Checks if sunlight hours are reasonable (between 2 and 12).

    Args:
        hours (int): The number of sunlight hours to check.

    Raises:
        InvalidSunlightHours: If hours are outside the [2, 12] range.
    """
    if not (2 <= hours <= 12):
        m = f"Error: Sunlight hours {hours} is too low (min 2)"
        raise InvalidSunlightHours(m)


def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int) -> None:
    """
    Validates plant health data and handles custom exceptions.

    Args:
        plant_name (str): Name of the plant.
        water_level (int): Sensor reading for water.
        sunlight_hours (int): Sensor reading for light.
    """
    try:
        check_name(plant_name)
        check_water_level(water_level)
        check_sunlight_hours(sunlight_hours)
    except InvalidHandle as e:
        print(e)
    else:
        print(f"Plant '{plant_name}' is healthy!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    check_plant_health("tomato", 5, 5)

    print("\nTesting empty plant name...")
    check_plant_health("", 5, 5)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 5)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)

    print("\nAll error raising tests completed!")
