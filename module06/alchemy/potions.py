import elements
from .elements import create_air, create_earth


def healing_potion() -> str:
    return ("Healing potion brewed with " +
            f"’{create_air()}’ and ’{create_earth()}’")


def strength_potion() -> str:
    return ("Strength potion brewed with " +
            f"’{elements.create_fire()}’ and ’{elements.create_water()}’")
