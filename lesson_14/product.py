from sqlalchemy import Column, Integer, String, Float

from lesson_14.base import Base


class Product(Base):
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
