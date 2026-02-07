def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import validate_ingredients
    result = validate_ingredients(ingredients)
    splited = result.split()
    for element in splited:
        if element == "VALID":
            return f"Spell recorded: {spell_name} ({result})"
    return f"Spell rejected: {spell_name} ({result})"
