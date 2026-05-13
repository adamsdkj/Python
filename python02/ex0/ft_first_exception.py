#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int:
    """
    Convert a temperature string to an integer and check if it is suitable
    for plants.

    Args:
        temp_str (str): Temperature input as a string.

    Returns:
        int: The temperature as an integer if valid and within range.
             None if the input is invalid or out of range.

    Prints:
        Messages indicating whether the temperature is perfect, too cold,
        too hot, or invalid.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        elif temp > 0:
            print(f"Error: {temp} is too cold for plants (min 0°C)")
        else:
            print(f"Error: {temp} is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_cases = (25, "abc", 100, -50)
    for i in test_cases:
        check_temperature(i)
        print()
    print("All tests completed - program didn't crash!")
