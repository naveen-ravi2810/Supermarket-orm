from .Config import Base, engine
from sqlalchemy import Column, Integer, String, Float


class Products(Base):
    __tablename__ = "products"
    product_id = Column(Integer, name='product_id', primary_key=True, autoincrement=True)
    product_name = Column(String(40), name='product_name', index=True)
    product_desc = Column(String(400), name='product_desc')
    product_price = Column(Float, name="product_price")
    product_tax = Column(Float, name="product_tax")
    product_seller_id = Column(Integer, name="product_seller_id")
    product_category = Column(String, name="product_category")

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

