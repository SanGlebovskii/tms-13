from base import Session, engine, Base
from product import Product

session = Session()


def create_product():
    product = Product(name=str(input('Название:')), price_products=float(input('Цена:')),
                      quantity=int(input('Количество:')), comment=str(input('Комментарий:')))
    session.add(product)
    session.commit()

def read_product():


