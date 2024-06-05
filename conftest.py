from data import Data
import pytest
from bun import Bun
from ingredient import Ingredient


@pytest.fixture(scope="function")
def bun():
    bun = Bun(Data.valid_bun_name, Data.valid_bun_price)

    return bun


@pytest.fixture(scope="function")
def ingredient():
    ingredient = Ingredient(Data.valid_ingredient_type, Data.valid_ingredient_name, Data.valid_ingredient_price)

    return ingredient
