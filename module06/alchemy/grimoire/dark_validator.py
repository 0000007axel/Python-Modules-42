from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    for ingredient in ingredients.lower().split():
        if ingredient in dark_spell_allowed_ingredients():
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
