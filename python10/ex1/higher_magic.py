from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells into one that returns a tuple of both results."""
    try:
        def combined(*args: Any, **kwargs: Any) -> tuple:
            return (spell1(*args, **kwargs), spell2(*args, **kwargs))
        return combined
    except Exception:
        return None


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplify a spell's numeric result by a multiplier."""
    try:
        def amplified(*args: Any, **kwargs: Any):
            return base_spell(*args, **kwargs) * multiplier
        return amplified
    except Exception:
        return None


def conditional_caster(condition: Callable,
                       spell: Callable) -> Callable:
    """Cast a spell only if the condition returns True."""
    try:
        def caster(*args: Any, **kwargs: Any):
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            return "Spell fizzled"
        return caster
    except Exception:
        return None


def spell_sequence(spells: list[Callable]) -> Callable:
    """Cast all spells in order and return a list of results."""
    try:
        def sequence(*args: Any, **kwargs: Any) -> list:
            return [s(*args, **kwargs) for s in spells]
        return sequence
    except Exception:
        return None


def main() -> None:

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")

    def damage(power):
        return power

    mega = power_amplifier(damage, 3)
    print(f"Original: {damage(10)}, Amplified: {mega(10)}")

    print("\nTesting conditional caster...")

    def has_mana(target):
        return target != "Ghost"

    def blast(target):
        return f"Blast hits {target}"

    conditional = conditional_caster(has_mana, blast)
    print(f"vs Dragon: {conditional('Dragon')}")
    print(f"vs Ghost: {conditional('Ghost')}")

    print("\nTesting spell sequence...")

    def shield(target):
        return f"Shield protects {target}"

    seq = spell_sequence([fireball, heal, shield])
    results = seq("Knight")
    for r in results:
        print(f"  {r}")

    print()


if __name__ == "__main__":
    main()
