"""Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество,
комментарий. Реализовать CRUD(создание, чтение, обновление по id, удаление
по id) для продуктов. Создать пользовательский интерфейс."""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///products1.db", echo=True)
Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price_products = Column(Float)
    quantity = Column(Integer)
    comment = Column(String)

    def __init__(self, name, price_products, quantity, comment):
        self.name = name
        self.price_products = price_products
        self.quantity = quantity
        self.comment = comment


Base.metadata.create_all(engine)

engine = create_engine("sqlite:///products1.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
session.add_all([Products('Bananas', 1.94, 500, 'Ecuador'), Products('Milk', 2.34, 1200, 'Lida milk factory'),
                Products('Beer', 1.79, 300, 'Heineken')])
session.commit()
