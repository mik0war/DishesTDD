from domain.dishes import Salad, DishFactory, Pizza


def test_dishes_factory():

    # Блок инициализации результата
    expected = Salad()

    # Блок вызова тестируемой функции
    factory = DishFactory()
    actual = factory.create_dish(Salad)

    # Блок проверки

    assert actual == expected

    # Блок инициализации результата
    expected = Pizza("Пеперони", 10)

    # Блок вызова тестируемой функции
    factory = DishFactory()
    actual = factory.create_dish(Pizza, "Пеперони", 10)

    # Блок проверки

    assert actual == expected

    # Блок инициализации результата
    expected = Pizza("Пеперони", 10)

    # Блок вызова тестируемой функции
    factory = DishFactory()
    actual = factory.create_dish(Pizza, "Пеперони", price=10)

    # Блок проверки

    assert actual == expected


