from data import Data
from conftest import bun


class TestBun:

    def test_bun_get_name_success(self, bun):

        assert bun.get_name() == Data.valid_bun_name


    def test_bun_get_price_success(self, bun):

        assert bun.get_price() == Data.valid_bun_price
