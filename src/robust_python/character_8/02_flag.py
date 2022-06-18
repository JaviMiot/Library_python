from enum import Flag, auto


class Allergen(Flag):
    FISH = auto()
    SHELLFISH = auto()
    TREE_NUTS = auto()
    PEANUTS = auto()
    GLUTEN = auto()
    SOY = auto()
    DAIRY = auto()


allergens = Allergen.FISH | Allergen.SHELLFISH

print(list(Allergen))
print(allergens)
print(Allergen.FISH.value)
print(allergens.SHELLFISH.value)
print(allergens.value)

if allergens & Allergen.FISH:
    print("This recipe contains fish.")
