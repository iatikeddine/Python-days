def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    splited = ingredients.split()
    for element in splited:
        if element in valid:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
