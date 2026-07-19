import elements
from .elements import create_air, create_earth

def healing_potion() -> str:
    return f"Healing potion brewed with ’{create_air()}’ and ’{create_earth()}’"


def strength_potion() -> str:
    return f"Strength potion brewed with ’{elements.create_fire()}’ and ’{elements.create_water()}’"
