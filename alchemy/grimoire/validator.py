def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "earth", "air"]
    if any(v in ingredients.lower() for v in valid):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"