#!/usr/bin/env python3

def handle_archive(filename: str) -> None:
    """Crisis handler function for archive operations."""
    print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as f:
            data = f.read()
            print(f"SUCCESS: Archive recovered - \"{data}\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {e}")
        print("STATUS: Crisis handled, anomaly logged")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    handle_archive("lost_archive.txt")
    print()
    handle_archive("classified_vault.txt")
    print()
    handle_archive("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully.\nArchives secure.")


if __name__ == "__main__":
    main()
