from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    for ingredient in ingredients.lower().split():
        if ingredient in light_spellbook.light_spell_allowed_ingredients():
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
