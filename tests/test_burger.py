from praktikum.burger import Burger
import random

from tests.conftest import full_ingredient_burger


class TestBurger:

    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun == bun


    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients


    def test_remove_ingredient(self, full_ingredient_burger):
        burger = full_ingredient_burger
        len_src = len(burger.ingredients)
        ind = random.randint(0, len(full_ingredient_burger.ingredients) - 1)
        burger.remove_ingredient(ind)

        assert len(burger.ingredients) == len_src - 1


    def test_move_ingredient(self, full_ingredient_burger, ingredient_indexes):
        burger = full_ingredient_burger

        moved_ingredient = full_ingredient_burger.ingredients[ingredient_indexes[0]]
        burger.move_ingredient(ingredient_indexes[0], ingredient_indexes[1])

        assert (moved_ingredient == burger.ingredients[ingredient_indexes[1]])


    def test_get_price(self, full_ingredient_burger):
        burger = full_ingredient_burger

        price = burger.bun.get_price() * 2

        for ingrt in burger.ingredients:
            price += ingrt.get_price()

        assert burger.get_price() == price


    def test_get_receipt(self, full_ingredient_burger):
        burger = full_ingredient_burger
        receipt = burger.get_receipt()
        receipt_strs = receipt.split('\n')

        assert burger.bun.name in receipt_strs[0]
        i = 0
        for ingrt in burger.ingredients:
            i += 1
            assert ingrt.name in receipt_strs[i]

        assert f"(==== {burger.bun.name} ====)" == receipt_strs[i + 1]
        assert f"Price: {burger.get_price()}" == receipt_strs[i + 3]
