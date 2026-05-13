"""Construct module for demonstrating virtual environment usage."""

import sys
import site


def main() -> None:
    """Check and display virtual environment status."""
    print("\nMATRIX STATUS: You're still plugged in\n")
    if sys.prefix == sys.base_prefix:
        print(
            f"Current Python: {sys.executable}\n"
            "Virtual Environment: None detected\n"
            "\nWARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n"
            "\nTo enter the construct, run:\n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\n"
            "Scripts\n"
            "activate # On Windows\n"
            "\nThen run this program again."
        )
    else:
        print(
            f"Current Python: {sys.executable}\n"
            f"Virtual Environment: {sys.prefix}\n"
            "\nSUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n"
            "\nPackage installation path:\n"
            f"{site.getsitepackages()[0]}"
        )


if __name__ == "__main__":
    main()
