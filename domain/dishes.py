import abc

class Dish(abc.ABC):
    @abc.abstractmethod
    def get_name(self):
        pass
    @abc.abstractmethod
    def get_price(self):
        pass

class Pizza(Dish):

    def __init__(self, name, price, discount = 0):
        self.__name = name
        self.__price = price
        self.__discount = discount

    def get_name(self):
        return f"Pizza {self.__name}"

    def get_price(self):
        return self.__price - self.__discount * self.__price

class Burger(Dish):

    def __init__(self, name, price, discount):
        self.__name = name
        self.__price = price
        self.__discount = discount

    def get_name(self):
        return f"Burger {self.__name}"

    def get_price(self):
        return self.__price - self.__discount * self.__price

class Sushi(Dish):

    def __init__(self, data_source):
        self.__dataSource = data_source

    def get_name(self):
        return self.__dataSource["name"]

    def get_price(self):
        return self.__dataSource["price"]

class Salad(Dish):

    def get_name(self):
        return "Salad"

    def get_price(self):
        return 8.92

