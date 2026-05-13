import functools
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates the first argument >= min_power."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0] if args else kwargs.get('power', 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that retries failed spells up to max_attempts times."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return (
                f"Spell casting failed after "
                f"{max_attempts} attempts"
            )
        return wrapper
    return decorator


class MageGuild:
    """A guild of mages demonstrating staticmethod and decorators."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check if a mage name is valid (3+ chars, letters/spaces)."""
        try:
            if len(name) < 3:
                return False
            return all(c.isalpha() or c == ' ' for c in name)
        except Exception:
            return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power is sufficient (min 10)."""
        try:
            if power < 10:
                return "Insufficient power for this spell"
            return f"Successfully cast {spell_name} with {power} power"
        except Exception:
            return None


def main() -> None:

    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(min_power=10)
    def blast(power: int) -> str:
        return f"Blast with {power} power!"

    print(blast(15))
    print(blast(5))

    print("\nTesting retry spell...")
    call_count = 0

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise Exception("Spell unstable!")
        return "Spell succeeded!"

    print(f"Result: {unstable_spell()}")

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Archmage Zara"))
    print(MageGuild.validate_mage_name("Jo"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Fire", 5))

    print()


if __name__ == "__main__":
    main()
