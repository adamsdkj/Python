#!/usr/bin/env python3

def test_error_types(error_test, test_case, multiple: int = 0) -> int:
    """
    Test a specific error type and handle exceptions.

    Args:
        error_test (str): Name of the error to test
        test_case (any): Input that may cause an error
        multiple (int): Flag for multiple error testing (default 0)

    Returns:
        int: 1 if an error occurred during multiple tests, else 0
    """
    try:
        if multiple == 0:
            print(f"Testing {error_test}...")
        if error_test == "ValueError":
            int(test_case)
        elif error_test == "ZeroDivisionError":
            1 / test_case
        elif error_test == "FileNotFoundError":
            fl = open(test_case)
            fl.close()
        elif error_test == "KeyError":
            test_case["dic"][test_case["key"]]
    except Exception as err:
        if multiple >= 1:
            return 1
        elif err.__class__.__name__ == "ValueError":
            error_name = err.__class__.__name__
            print(f"Caught {error_name}: invalid literal for int()")
        elif err.__class__.__name__ == "ZeroDivisionError":
            print(f"Caught {err.__class__.__name__}: division by zero")
        elif err.__class__.__name__ == "FileNotFoundError":
            print(
                f"Caught {err.__class__.__name__}: No such file "
                f"'{test_case}'"
            )
        elif err.__class__.__name__ == "KeyError":
            print(
                f"Caught {err.__class__.__name__}: "
                f"'{test_case['key']}'"
            )


def garden_operations(test_case: dict) -> None:
    """
    Run all garden error tests for the given test cases.

    Args:
        test_case (dict): Dictionary mapping error names to test cases
    """
    error_list = (
        "ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError"
    )
    c = 0
    for error_test, test_case in error_dict.items():
        if error_test == "multiple errors together":
            print("Testing multiple errors together...")
            for test in error_list:
                c += test_error_types(test, test_case, 1)
            if c >= 1:
                print("Caught an error, but program continues")
            continue
        test_error_types(error_test, test_case)
        print()


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    error_dict = {
        "ValueError": "abc",
        "ZeroDivisionError": 0,
        "FileNotFoundError": "missing.txt",
        "KeyError": {
            "dic": {"key1": "hi", "key2": "bye"},
            "key": "missing\\_plant"
        },
        "multiple errors together": "abc"
    }
    garden_operations(error_dict)
    print("\nAll error types tested successfully!")
