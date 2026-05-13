#!/usr/bin/env python3

from . import elements as e


def healing_potion() -> str:
    return f"Healing potion brewed with {e.create_fire()} and"
    f" {e.create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {e.create_earth()} and"
    f" {e.create_fire()}"


def invisibility_potion() -> str:
    return f"Invisibility potion brewed with {e.create_air()} and"
    f" {e.create_water()}"


def wisdom_potion() -> str:
    return (
        f"Wisdom potion brewed with all elements: {e.create_water()}"
        f" {e.create_air()} "
        f"{e.create_earth()} {e.create_fire()}"
    )
