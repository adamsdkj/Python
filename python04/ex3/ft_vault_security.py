#!/usr/bin/env python3

def main(file1: str, file2: str):
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open(file1, "r") as f1, open(file2, "w") as f2:
            print("Vault connection established with failsafe protocols\n")
            content1 = f1.read()
            f2.write("[CLASSIFIED] New security protocols archived")
            print("SECURE EXTRACTION:\n"
                  f"{content1}\n"
                  f"\nSECURE PRESERVATION:\n"
                  "[CLASSIFIED] New security protocols archived\n"
                  "Vault automatically sealed upon completion\n")
    except FileNotFoundError:
        print(f"no such a files called {file1}, {file2}")
    except Exception as e:
        print(f"unexpected error {e}")
    else:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main("classified_data.txt", "security_protocols.txt")
