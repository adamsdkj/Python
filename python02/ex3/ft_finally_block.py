#!/usr/bin/env python3


class InvalidName(Exception):
    """Raised when a plant name is invalid or empty."""
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
        raise InvalidName()


def water_plants(plant_list: list[str]) -> None:
    """
    Simulate watering a list of plants with exception handling.

    Args:
        plant_list (list): List of plant names.

    Prints:
        Status messages for opening/closing watering system,
        watering plants, and errors if names are invalid.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            check_name(plant)
            print(f"Watering {plant}")
    except InvalidName:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Test the watering system with normal and invalid plant lists.

    Prints:
        Messages showing successful watering and error handling.
    """
    good_list: list[str] = ["tomato", "lettuce", "carrots"]
    bad_list: list[str] = ["tomato", ""]

    print("Testing normal watering...")
    water_plants(good_list)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(bad_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
