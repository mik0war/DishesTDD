from dataclasses import dataclass
from dish import Dish


@dataclass
class Order:
    order_id: int = None
    date: str = None
    table_number: int = None
    dishes: list[Dish] = []
    status: str = ''


