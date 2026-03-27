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

    def __eq__(self, other):
        return (isinstance(other, Pizza)
                and self.__name == other.__name
                and self.get_price() == other.get_price())

class Burger(Dish):

    def __init__(self, name, price, discount):
        self.__name = name
        self.__price = price
        self.__discount = discount

    def get_name(self):
        return f"Burger {self.__name}"

    def get_price(self):
        return self.__price - self.__discount * self.__price

    def __eq__(self, other):
        return (isinstance(other, Burger)
                and self.__name == other.__name
                and self.get_price() == other.get_price())

class Sushi(Dish):

    def __init__(self, data_source):
        self.__dataSource = data_source

    def get_name(self):
        return self.__dataSource["name"]

    def get_price(self):
        return self.__dataSource["price"]

    def __eq__(self, other):
        return (isinstance(other, Sushi)
                and self.__dataSource["name"] == other.__dataSource["name"]
                and self.__dataSource["price"] == other.__dataSource["price"])

class Salad(Dish):

    def get_name(self):
        return "Salad"

    def get_price(self):
        return 8.92

    def __eq__(self, other):
        return isinstance(other, Salad)

class Drink(Dish):

    def __init__(self, name, price):
        self.__name = name
        self._price = price


    def get_name(self):
        return self.__name

    def get_price(self):
        return self._price


    def __eq__(self, other):
        return (isinstance(other, Drink)
                and self.__name == other.__name
                and self.get_price() == other.get_price())

class Dessert(Dish):

    def __init__(self, name, price):
        self.__name = name
        self._price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self._price

    def __eq__(self, other):
        return (isinstance(other, Dessert)
                and self.__name == other.__name
                and self.get_price() == other.get_price())

class EmptyDish(Dish):
    def get_name(self):
        return ''
    def get_price(self):
        return 0

    def __eq__(self, other):
        return isinstance(other, EmptyDish)

class ComboMeal(Dish):
    __main_dish : Dish
    __dessert: Dish
    __drink: Dish
    __discount: int

    def __init__(self,
                 main_dish = EmptyDish(),
                 dessert = EmptyDish(),
                 drink = EmptyDish(),
                 discount = 0):
        self.__main_dish = main_dish
        self.__dessert = dessert
        self.__drink = drink
        self.__discount = discount

    def get_name(self):
        names = ', '.join([
            i for i in
            (self.__main_dish.get_name(),
             self.__dessert.get_name(),
             self.__drink.get_name())
            if i
        ])

        return '' if not names else f'Комбо {names}'

    def get_price(self):
        prices = sum([self.__main_dish.get_price(),
                      self.__dessert.get_price(),
                      self.__drink.get_price()]
                     )
        return prices - self.__discount * prices

    def __eq__(self, other):
        return (isinstance(other, ComboMeal)
                and self.__main_dish == other.__main_dish
                and self.__dessert == other.__dessert
                and self.__drink == other.__drink)

class DishFactory:

    def create_dish(self, dish_type, name, price, discount, *args, **kwargs):
        dictionary = {
            Sushi: [{'name': name, 'price': price, 'discount': discount}],
            Salad: [],
            Dessert: [name, price],
            Drink: [name, price],
        }

        if dish_type == ComboMeal:
            return ComboMeal(*args, **kwargs)

        if dish_type in dictionary:
            return dish_type(*dictionary[dish_type])

        return dish_type(name, price, discount)



