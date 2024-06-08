from data import Data
from conftest import ingredient


class TestIngredient:

    def test_ingredient_get_type_success(self, ingredient):
        assert ingredient.get_type() == Data.valid_ingredient_type

    def test_ingredient_get_name_success(self, ingredient):
        assert ingredient.get_name() == Data.valid_ingredient_name

    def test_ingredient_get_price_success(self, ingredient):
        assert ingredient.get_price() == Data.valid_ingredient_price

