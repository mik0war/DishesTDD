from domain.dishes import *
import pytest

def test_dishes_factory():

    # Блок инициализации результата
    expected = Salad()

    # Блок вызова тестируемой функции
    factory = DishFactory()
    actual = factory.create_dish(Salad,0, 0, '')

    # Блок проверки

    assert actual == expected

    # Блок инициализации результата
    expected = Pizza("Пеперони", 10, 0)

    # Блок вызова тестируемой функции
    factory = DishFactory()
    actual = factory.create_dish(Pizza, "Пеперони", 10, 0)

    # Блок проверки

    assert actual == expected

    # Блок инициализации результата
    expected = Pizza("Пеперони", 10, 0)

    # Блок вызова тестируемой функции
    factory = DishFactory()
    actual = factory.create_dish(Pizza, "Пеперони", price=10, discount=0)

    # Блок проверки

    assert actual == expected

    # Блок инициализации результата
    expected = Dessert("Печенье", 10)

    # Блок вызова тестируемой функции
    factory = DishFactory()
    actual = factory.create_dish(Dessert, "Печенье", price=10, discount=1234567)

    # Блок проверки

    assert actual == expected


def test_combo_meal():

    # Блок инициализации результата
    expected = ComboMeal(
        Salad(),
        Dessert("Печенье", 10),
        Drink("Чай", 40)
    )

    # Блок вызова тестируемой функции
    factory = DishFactory()
    actual = factory.create_dish(ComboMeal, "", 0, 0,
                                 Salad(), Dessert("Печенье", 10), drink=Drink("Чай", 40)
                                 )
    # Блок проверки
    assert actual == expected

def test_combo_meal_builder():
    # Блок инициализации результата
    expected = ComboMeal(
        Salad(),
        Dessert("Печенье", 10),
        Drink("Чай", 40)
    )

    # Блок вызова тестируемой функции
    actual = (ComboMealBuilder()
               .set_main_dish(Salad())
               .set_dessert(Dessert("Печенье", 10))
               .set_drink(Drink("Чай", 40))).build()


    # Блок проверки
    assert actual == expected

    # Блок инициализации результата
    expected = ComboMeal(
        Salad(),
        EmptyDish(),
        Drink("Чай", 40)
    )

    # Блок вызова тестируемой функции
    actual = (ComboMealBuilder()
              .set_main_dish(Salad())
              .set_drink(Drink("Чай", 40))).build()

    # Блок проверки
    assert actual == expected

    # Блок инициализации результата
    expected = ComboMeal(
        Salad(),
        EmptyDish(),
        EmptyDish()
    )

    # Блок вызова тестируемой функции
    actual = (ComboMealBuilder()
              .set_main_dish(Salad())).build()

    # Блок проверки
    assert actual == expected

def test_combo_meal_without_main_dish():
    with pytest.raises(ValueError):
        ComboMealBuilder().build()


