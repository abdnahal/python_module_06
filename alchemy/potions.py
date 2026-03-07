from .elements import create_fire, create_water, create_earth, create_air


def healing_potion():
    fire = create_fire()
    water = create_water()
    return f"Healing potion brewed with {fire} and {water}"


def wisdom_potion():
    f, w, e, a = create_fire(), create_water(), create_earth(), create_air()
    return f"Wisdom potion brewed with all elements: {f}, {w}, {e}, {a}"
