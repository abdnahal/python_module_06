if __name__ == "__main__":
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    from alchemy.grimoire import validate_ingredients
    print(f"validate_ingredients('fire air'): \
{validate_ingredients("fire air")}")
    print(f"validate_ingredients('dragon scales'): \
{validate_ingredients("dragon scales")}\n")

    print("Testing spell recording with validation:")
    from alchemy.grimoire import record_spell
    print(f"record_spell('Fireball', 'fire air'): \
{record_spell('Fireball', 'fire air')}")
    print(f"record_spell('Dark Magic', 'shadow'): \
{record_spell("Dark Magic", "shadow")}\n")

    print("Testing late import technique:")
    from alchemy.grimoire import record_spell
    print(f"record_spell('Lightning', 'air'): \
{record_spell("Lightning", "air")}\n")

    print("Testing Dependency injection technique:")
    from alchemy.grimoire import record_spell2, validate_ingredients
    print(f"record_spell('Lightning', 'air'): \
{record_spell2("Lightning", "air", validate_ingredients)}\n")

    print("Circular dependency curse avoided using late \
imports and Dependency injection!")
    print("All spells processed safely!")
