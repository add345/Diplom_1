import pytest
import random
from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient

@pytest.fixture
def bun():
    db: Database = Database()
    buns: List[Bun] = db.available_buns()

    ind = random.randint(0, len(buns) - 1)

    return buns[ind]

@pytest.fixture
def ingredient():
    db: Database = Database()
    ingredients: List[Ingredient] = db.available_ingredients()

    ind = random.randint(0, len(ingredients) - 1)

    return ingredients[ind]

@pytest.fixture
def full_ingredient_burger():
    burger: Burger = Burger()

    db: Database = Database()
    buns: List[Bun] = db.available_buns()
    ingredients: List[Ingredient] = db.available_ingredients()

    ind = random.randint(0, len(buns) - 1)

    burger.set_buns(buns[ind])

    for ingredient in ingredients:
        burger.add_ingredient(ingredient)

    return burger

@pytest.fixture
def ingredient_indexes():
    db: Database = Database()
    ingredients: List[Ingredient] = db.available_ingredients()
    ind1 = random.randint(0, len(ingredients) - 1)
    ind2 = random.randint(0, len(ingredients) - 1)

    while ind1 == ind2:
        ind2 = random.randint(0, len(ingredients) - 1)

    return ind1, ind2
