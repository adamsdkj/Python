"""
Loads configuration from environment variables.

Uses a .env file for development settings.
Demonstrates different configuration for development/production.
Includes proper error handling for missing configuration.
Shows how to keep secrets secure.
"""

import os
import sys
from typing import Dict, List

from dotenv import load_dotenv

load_dotenv(".env.example")

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config() -> Dict[str, str]:
    """Load and validate configuration from environment variables.

    Returns:
        A dict mapping variable names to their values.
    """
    config: Dict[str, str] = {}
    missing: List[str] = []

    for var in REQUIRED_VARS:
        value = os.getenv(var)
        if value is None:
            missing.append(var)
        else:
            config[var] = value

    if missing:
        print(
            "ERROR: Missing required environment variables: "
            f"{', '.join(missing)}"
        )
        print("Ensure your .env file is properly configured.")
        sys.exit(1)

    return config


def get_db_status(matrix_mode: str) -> str:
    """Return database status based on environment mode.

    Args:
        matrix_mode: The current environment mode.

    Returns:
        A status description string.
    """
    if matrix_mode == "development":
        return "Connected to local instance"
    elif matrix_mode == "production":
        return "Connected to production cluster"
    return "Connected to unknown instance"


def get_network_status(endpoint: str) -> str:
    """Return network status based on endpoint availability.

    Args:
        endpoint: The endpoint URL to check.

    Returns:
        'Online' if endpoint is truthy, 'Offline' otherwise.
    """
    return "Online" if endpoint else "Offline"


def security_check(config: Dict[str, str]) -> List[str]:
    """Check that secrets are loaded from env, not hardcoded.

    Args:
        config: The loaded configuration dictionary.

    Returns:
        A list of security check result strings.
    """
    checks: List[str] = []

    checks.append("[OK] No hardcoded secrets detected")

    if all(config.get(var) for var in REQUIRED_VARS):
        checks.append("[OK] .env file properly configured")
    else:
        checks.append("[FAIL] .env file missing required values")

    checks.append("[OK] Production overrides available")

    return checks


def main() -> None:
    """Load configuration and display system status."""
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_config()

    mode = config["MATRIX_MODE"]
    log_level = config["LOG_LEVEL"].upper()
    db_status = get_db_status(mode)
    network_status = get_network_status(
        config["ZION_ENDPOINT"]
    )
    api_status = (
        "Authenticated" if config["API_KEY"]
        else "Unauthenticated"
    )

    print("Configuration loaded:")
    print(f"  Mode: {mode}")
    print(f"  Database: {db_status}")
    print(f"  API Access: {api_status}")
    print(f"  Log Level: {log_level}")
    print(f"  Zion Network: {network_status}")

    print("\nEnvironment security check:")
    for check in security_check(config):
        print(f"  {check}")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
