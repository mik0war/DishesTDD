from domain.order import Order


def test_in_memory_repository():

    #Вызов пустого репозитория
    expected = []

    repo = InMemoryOrderRepository()
    actual = repo.get_all()

    assert actual == expected

    #Добавление заказа и вызов списка заказов
    order = Order(1, '12.01.2000 14:43', 1, [Salad()], 'processed')
    expected = [order]

    repo.add(order)

    actual = repo.get_all()

    assert actual == expected

    #Добавление второго блюда
    order_1 = Order(2, '12.01.2000 14:43', 1, [Salad()], 'processed')
    expected = [order, order_1]

    repo.add(order_1)

    actual = repo.get_all()

    assert actual == expected

    #получение заказа по id

    expected = order
    actual = repo.get_by_id(1)
    assert actual == expected


def test_in_file_repository():
    # Вызов пустого репозитория
    expected = []

    repo = FileOrderRepository()
    actual = repo.get_all()

    assert actual == expected

    # Добавление заказа и вызов списка заказов
    order = Order(1, '12.01.2000 14:43', 1, [Salad()], 'processed')
    expected = [order]

    repo.add(order)

    actual = repo.get_all()

    assert actual == expected

    # Добавление второго блюда
    order_1 = Order(2, '12.01.2000 14:43', 1, [Salad()], 'processed')
    expected = [order, order_1]

    repo.add(order_1)

    actual = repo.get_all()

    assert actual == expected

    # получение заказа по id

    expected = order
    actual = repo.get_by_id(1)
    assert actual == expected