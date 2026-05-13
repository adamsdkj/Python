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


class GardenError(Exception):
    """Base exception for all garden-related errors."""

    pass


class WaterError(GardenError):
    """Raised when the water supply in the tank is insufficient."""

    pass


def check_water(tank: int) -> None:
    """
    Raise WaterError if the tank's water supply is zero.

    Args:
        tank (int): Current water level in the tank.

    Raises:
        WaterError: If the tank supply is 0.
    """
    if tank == 0:
        raise WaterError()


def check_name(name: str) -> None:
    """
    Check if the plant name is valid.

    Args:
        name (str): The name of the plant.

    Raises:
        InvalidName: If the name is None or empty.
    """
    if not name:
        raise InvalidName("Plant name cannot be empty!")


def check_water_level(level: int, name: str) -> None:
    """
    Check if water level is reasonable (between 1 and 10).

    Args:
        level (int): The water level to check.
        name (str): Name of the plant for error reporting.

    Raises:
        InvalidWaterLevel: If level is outside the [1, 10] range.
    """
    if not (1 <= level <= 10):
        m = f"Error checking {name}: Water level {level} is too high (max 10)"
        raise InvalidWaterLevel(m)


def check_sunlight_hours(hours: int, name: str) -> None:
    """
    Check if sunlight hours are reasonable (between 2 and 12).

    Args:
        hours (int): The number of sunlight hours to check.
        name (str): Name of the plant for error reporting.

    Raises:
        InvalidSunlightHours: If hours are outside the [2, 12] range.
    """
    if not (2 <= hours <= 12):
        m = f"Error checking {name}: Sunlight hours {hours} is too low (min 2)"
        raise InvalidSunlightHours(m)


class Plant:
    """
    Represents a plant with specific environmental needs.

    Attributes:
        plant_name (str): Name of the plant species.
        water_level (int): Current water saturation.
        sunlight_hours (int): Daily hours of sunlight received.
    """

    def __init__(self, plant_name: str, water_level: int, sunlight_hours: int):
        """Initialize a Plant instance."""
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """
    Manages a collection of plants and monitors their health.

    Attributes:
        plants (list): List of Plant objects.
        tank (int): Current water tank level.
    """

    def __init__(self, tank: int):
        """Initialize the GardenManager with a water tank level."""
        self.plants = []
        self.tank = tank

    def add_plant(self, plant: Plant):
        """
        Validate and add a plant to the garden.

        Args:
            plant (Plant): The plant object to add.
        """
        try:
            check_name(plant.plant_name)
            self.plants.append(plant)
            print(f"Added {plant.plant_name} successfully")
        except InvalidName as e:
            print(f"Error adding plant: {e}")

    def water_plant(self):
        """
        Simulate watering all plants in the garden.

        Prints status messages for the watering process and handles
        cases where plant names might be invalid.
        """
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                check_name(plant.plant_name)
                print(f"Watering {plant.plant_name} - success")
        except InvalidName:
            print("Error: Cannot water None - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_tank_error(self):
        """
        Test tank water levels and handle empty tank scenarios.

        Raises:
            WaterError: Handled internally if tank is 0.
        """
        try:
            print("\nTesting error recovery...")
            check_water(self.tank)
        except WaterError:
            print("Caught GardenError: Not enough water in tank")
        finally:
            print("System recovered and continuing...")

    def check_plant_health(self) -> None:
        """
        Validate health data for all plants and report issues.

        Checks water levels and sunlight hours, triggering a tank check
        if validation fails.
        """
        print("Checking plant health...")
        for plant in self.plants:
            try:
                check_name(plant.plant_name)
                check_water_level(plant.water_level, plant.plant_name)
                check_sunlight_hours(plant.sunlight_hours, plant.plant_name)
            except InvalidHandle as e:
                print(e)
                self.check_tank_error()
            else:
                status = (f"{plant.plant_name}: healthy "
                          f"(water: {plant.water_level}, "
                          f"sun: {plant.sunlight_hours})")
                print(status)


if __name__ == "__main__":
    print("=== Garden Management System ===\n")

    garden_manager = GardenManager(0)

    print("Adding plants to garden...")
    garden_manager.add_plant(Plant("tomato", 5, 8))
    garden_manager.add_plant(Plant("lettuce", 15, 8))
    garden_manager.add_plant(Plant("", 15, 8))

    print("")
    garden_manager.water_plant()
    print("")
    garden_manager.check_plant_health()
    print("")

    print("Garden management system test complete!")
