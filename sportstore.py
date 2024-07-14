from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import text
from datetime import datetime

Base = declarative_base()

class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String, nullable=False)
    dat_reg = Column(DateTime, default=datetime.utcnow)
    sum_sale = Column(Float, nullable=False)
    date_sale = Column(DateTime, default=datetime.utcnow)
    seller_name = Column(String, nullable=False)
    products = relationship('Products', back_populates='sales')

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sales_id = Column(Integer, ForeignKey('sales.id'), nullable=False)
    product_type = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    manufacturer = Column(String, nullable=False)
    sales = relationship('Sales', back_populates='products')

DATABASE_URL = 'postgresql+psycopg2://koyeb-adm:b5lj0ipxmgsW@ep-patient-voice-a28tsil8.eu-central-1.pg.koyeb.app/sportsstore?sslmode=require'
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def create_sales(session, customer_name, sum_sale, seller_name):
   sales = Sales(customer_name=customer_name, sum_sale=sum_sale, seller_name=seller_name)
   session.add(sales)
   session.commit()
   return sales 

def create_products(session, sales_id, product_type, product_name, quantity, manufacturer):
   products = Products(sales_id=sales_id,product_type=product_type, product_name=product_name, quantity=quantity, manufacturer=manufacturer)
   session.add(products)
   session.commit()
   return products 


if __name__ == '__main__':


    
    sales = create_sales(session, 'Olda Novak', 1400, 'Ota')
    print(f'Created sale: {sales.customer_name}, {sales.sum_sale}, {sales.seller_name} ')

    products = create_products(session, sales.id, 'shirt', 'Basic1', 35, 'Adidas')
    print(f'Created product: {products.sales_id}, {products.product_type}, {products.product_name}, {products.quantity}, {products.manufacturer}')
    
    
session.close()

