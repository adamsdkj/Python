#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print("\n[STANDARD] Archive status from "
          f"{archivist_id}: {status}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication "
          "channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete",
          file=sys.stdout)
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
