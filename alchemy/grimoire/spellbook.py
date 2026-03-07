def record_spell(spell_name: str, ingredients: str) -> str:
    # ✅ Late import: imported INSIDE the function, not at the top
    # This delays the import until the function is actually called,
    # by which point both modules are fully loaded
    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
