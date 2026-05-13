#!/usr/bin/env python3


def record_spell(spell_name: str, ingredients: str) -> str:
    from . import validator as v

    validation = v.validate_ingredients(ingredients)
    if validation.endswith(" VALID"):
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
