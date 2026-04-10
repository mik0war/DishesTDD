import psycopg2
import logging
from psycopg2.extras import LoggingConnection, execute_batch, RealDictCursor

from data.repository import Repository
from domain.dishes import Dish, Pizza, Dessert
from domain.order import Order


class DBRepository(Repository):
    def __init__(self):
        self.connection = psycopg2.connect(
                                           host="localhost",
                                           port="5432",
                                           database="test",
                                           user="postgres",
                                           password="123")

        self.create_table()

    def __del__(self):
        self.connection.close()

    def create_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS "ORDER" (
                                    id SERIAL PRIMARY KEY,
                                    date VARCHAR(50) NOT NULL,
                                    table_number INTEGER NOT NULL,
                                    status VARCHAR(50) CHECK(status IN ('IN PROGRES', 'CREATED', 'READY', 'CLOSED')) NOT NULL
                                )''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS DISH (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                price INTEGER NOT NULL,
                order_id INTEGER REFERENCES "ORDER"(id) NOT NULL
            )'''
            )

            self.connection.commit()

    def add(self, order: Order):
        with self.connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO "ORDER" (date, table_number, status)
                VALUES (%s, %s, %s)
                RETURNING id
                ''', (order.date, order.table_number, order.status)
                )
            order_id =cursor.fetchone()[0]

            dish_array = tuple([
                (dish.get_name(), dish.get_price(), order_id) for dish in order.dishes
            ])

            execute_batch(cursor, '''
                INSERT INTO DISH (name, price, order_id)
                VALUES (%s, %s, %s)
            ''',  dish_array)

            self.connection.commit()



    def get_all(self):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute('''SELECT * 
            FROM "ORDER" JOIN DISH ON DISH.order_id = "ORDER".id''')
            result = cursor.fetchall()

        return result

    def get_by_id(self, id: int):
        pass

if __name__ == '__main__':
    repository = DBRepository()
    repository.add(Order(
        date="2021-09-09",
        table_number=1,
        status='IN PROGRES',
        dishes=[
            Pizza('Пицца пеперони', 123),
            Dessert('Крем-брюле', 124),
            Dessert('Сникерс', 123)
        ]
    ))

    print(repository.get_all())