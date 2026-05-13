#!/usr/bin/env python3

def main(file: str) -> None:
    f = None
    try:
        f = open(file, "r")
        content = f.read()
        print("Connection established...\n\n"
              "RECOVERED DATA:\n"
              f"{content}\n")
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(f"The file with the name {file} not found")
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
    main("ancient_fragment.txt")
