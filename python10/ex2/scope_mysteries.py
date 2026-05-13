from typing import Callable


def mage_counter() -> Callable:
    """Create a closure that counts how many times it's been called."""
    try:
        count = 0

        def counter() -> int:
            nonlocal count
            count += 1
            return count
        return counter
    except Exception:
        return None


def spell_accumulator(initial_power: int) -> Callable:
    """Create a closure that accumulates power over time."""
    try:
        total = initial_power

        def accumulate(amount: int) -> int:
            nonlocal total
            total += amount
            return total
        return accumulate
    except Exception:
        return None


def enchantment_factory(enchantment_type: str) -> Callable:
    """Create a function that applies the specified enchantment."""
    try:
        def enchant(item_name: str) -> str:
            return f"{enchantment_type} {item_name}"
        return enchant
    except Exception:
        return None


def memory_vault() -> dict[str, Callable]:
    """Create a memory management system with store and recall."""
    try:
        storage: dict = {}

        def store(key: str, value) -> None:
            storage[key] = value

        def recall(key: str):
            return storage.get(key, "Memory not found")

        return {'store': store, 'recall': recall}
    except Exception:
        return None


def main() -> None:

    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(50)
    print(f"Add 10: {acc(10)}")
    print(f"Add 20: {acc(20)}")
    print(f"Add 5: {acc(5)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']("secret_spell", "Arcane Blast")
    vault['store']("power_level", 9001)
    print(f"Recall secret_spell: {vault['recall']('secret_spell')}")
    print(f"Recall power_level: {vault['recall']('power_level')}")
    print(f"Recall unknown: {vault['recall']('unknown')}")

    print()


if __name__ == "__main__":
    main()
