import pytest
from praktikum.database import Database
from data import Data


class TestDatabase:

    @pytest.mark.parametrize("index, bun_name, bun_price", Data.database_buns)
    def test_database_available_buns_success(self, index, bun_name, bun_price):
        self.database = Database()
        buns = self.database.available_buns()
        name = buns[index].get_name()
        price = buns[index].get_price()

        assert name == bun_name and price == bun_price

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", Data.database_ingredients)
    def test_database_available_ingredients_success(self, index, ingredient_type, ingredient_name, ingredient_price):
        self.database = Database()
        ingredients = self.database.available_ingredients()
        type_ = ingredients[index].get_type()
        name = ingredients[index].get_name()
        price = ingredients[index].get_price()

        assert type_ == ingredient_type and name == ingredient_name and price == ingredient_price
