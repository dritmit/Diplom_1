from unittest.mock import Mock
from burger import Burger
from data import Data


class TestBurger:

    def test_burger_set_buns_success(self):
        self.burger = Burger()
        mock_bun = Mock()
        self.burger.set_buns(mock_bun)

        assert self.burger.bun == mock_bun

    def test_burger_add_ingredient_success(self):
        self.burger = Burger()
        mock_ingredient = Mock()
        self.burger.add_ingredient(mock_ingredient)

        assert self.burger.ingredients[0] == mock_ingredient

    def test_burger_remove_ingredient_success(self):
        self.burger = Burger()
        mock_ingredient = Mock()
        self.burger.add_ingredient(mock_ingredient)
        add_ingredient_count = len(self.burger.ingredients)
        self.burger.remove_ingredient(0)
        del_ingredient_count = len(self.burger.ingredients)

        assert add_ingredient_count - del_ingredient_count == 1

    def test_burger_move_ingredients_success(self):
        self.burger = Burger()
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        self.burger.add_ingredient(mock_ingredient_0)
        self.burger.add_ingredient(mock_ingredient_1)
        self.burger.move_ingredient(1, 0)

        assert self.burger.ingredients[0] == mock_ingredient_1

    def test_burger_get_price_success(self):
        self.burger = Burger()
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        mock_bun = Mock()
        mock_bun.get_price.return_value = Data.valid_bun_price
        mock_ingredient_0.get_price.return_value = Data.valid_ingredient_price_0
        mock_ingredient_1.get_price.return_value = Data.valid_ingredient_price_1
        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient_0)
        self.burger.add_ingredient(mock_ingredient_1)

        assert self.burger.get_price() == Data.valid_bun_price * 2 \
               + Data.valid_ingredient_price_0 + Data.valid_ingredient_price_1

    def test_burger_get_receipt_success(self):
        self.burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = Data.valid_bun_name
        mock_bun.get_price.return_value = Data.valid_bun_price
        mock_ingredient_0 = Mock()
        mock_ingredient_1 = Mock()
        mock_ingredient_0.get_name.return_value = Data.valid_ingredient_name_0
        mock_ingredient_1.get_name.return_value = Data.valid_ingredient_name_1
        mock_ingredient_0.get_type.return_value = Data.valid_ingredient_type_0
        mock_ingredient_1.get_type.return_value = Data.valid_ingredient_type_1
        mock_ingredient_0.get_price.return_value = Data.valid_ingredient_price_0
        mock_ingredient_1.get_price.return_value = Data.valid_ingredient_price_1
        price = Data.valid_bun_price * 2 + Data.valid_ingredient_price_0 + Data.valid_ingredient_price_1
        receipt = [f'(==== {Data.valid_bun_name} ====)',
                   f'= {str(Data.valid_ingredient_type_0).lower()} {Data.valid_ingredient_name_0} =',
                   f'= {str(Data.valid_ingredient_type_1).lower()} {Data.valid_ingredient_name_1} =',
                   f'(==== {Data.valid_bun_name} ====)\n', f'Price: {price}']
        receipt_result = '\n'.join(receipt)
        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_ingredient_0)
        self.burger.add_ingredient(mock_ingredient_1)

        assert self.burger.get_receipt() == receipt_result
