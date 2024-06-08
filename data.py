from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:

    valid_bun_name = 'Banbaleena'
    valid_bun_price = 333.33

    valid_ingredient_type = 'Type'
    valid_ingredient_name = 'Ingredient'
    valid_ingredient_price = 222.22
    valid_ingredient_price_0 = 123.45
    valid_ingredient_price_1 = 678.9

    valid_ingredient_name_0 = 'Ingredient_0'
    valid_ingredient_name_1 = 'Ingredient_1'

    valid_ingredient_type_0 = 'Type_0'
    valid_ingredient_type_1 = 'Type_1'

    database_buns = [(0, "black bun", 100), (1, "white bun", 200), (2, "red bun", 300)]

    database_ingredients = [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]
