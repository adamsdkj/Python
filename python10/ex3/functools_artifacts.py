import functools
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using the specified operation."""
    try:
        ops = {
            "add": operator.add,
            "multiply": operator.mul,
            "max": lambda a, b: a if a > b else b,
            "min": lambda a, b: a if a < b else b,
        }
        if operation not in ops:
            return None
        return functools.reduce(ops[operation], spells)
    except Exception:
        return None


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create partial applications of a base enchantment function."""
    try:
        return {
            'fire_enchant': functools.partial(
                base_enchantment, 50, "fire"),
            'ice_enchant': functools.partial(
                base_enchantment, 50, "ice"),
            'lightning_enchant': functools.partial(
                base_enchantment, 50, "lightning"),
        }
    except Exception:
        return None


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate the nth fibonacci number with memoization."""
    try:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    except Exception:
        return None


def spell_dispatcher() -> Callable:
    """Create a single dispatch spell system for different types."""
    try:
        @functools.singledispatch
        def cast(spell) -> str:
            return f"Unknown spell type: {type(spell).__name__}"

        @cast.register(int)
        def _(spell: int) -> str:
            return f"Damage spell: {spell} damage dealt"

        @cast.register(str)
        def _(spell: str) -> str:
            return f"Enchantment: {spell} applied"

        @cast.register(list)
        def _(spell: list) -> str:
            return f"Multi-cast: {len(spell)} spells launched"

        return cast
    except Exception:
        return None


def main() -> None:

    print("\nTesting spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")

    print("\nTesting partial enchanter...")

    def enchant(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} enchantment ({power}) on {target}"

    enchants = partial_enchanter(enchant)
    print(enchants['fire_enchant']("Sword"))
    print(enchants['ice_enchant']("Shield"))
    print(enchants['lightning_enchant']("Staff"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(20): {memoized_fibonacci(20)}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("Fireball"))
    print(cast(["heal", "shield", "blast"]))

    print()


if __name__ == "__main__":
    main()
