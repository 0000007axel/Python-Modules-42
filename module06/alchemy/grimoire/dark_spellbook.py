from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["eyeball", "bats", "frogs", "arsenic"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if validate_ingredients(ingredients).split()[-1] == "VALID":
        return (f"Spell recorded: {spell_name} ({ingredients + ' - VALID'})")
    return f"Spell recorded: {spell_name} ({ingredients + ' - INVALID'})"
