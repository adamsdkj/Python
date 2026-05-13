#!/usr/bin/env python3

def main(file: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n\n"
          f"Initializing new storage unit: {file}")
    f = None
    f = open(file, "w")
    f.write("[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n")
    f.close()
    f = None

    try:
        f = open(file, "r")
        content = f.read()
        print(f"\nInscribing preservation data...\n{content}\n"
              "Data inscription complete. Storage unit sealed.\n"
              f"Archive '{file}' ready for long-term preservation.")
    except FileNotFoundError:
        print(f"The file with the name {file} not found")
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    main("new_discovery.txt")
