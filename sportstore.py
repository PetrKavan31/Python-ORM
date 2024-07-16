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

def get_product():
    allproducts = session.query(Products).all()
    for product in allproducts:
        print(f'Product: {product.id} , {product.product_name}, {product.product_type}, {product.quantity} pcs, {product.manufacturer}') 

def search_in_products(name_query):
    items = session.query(Products).filter(Products.product_type.ilike(f'%{name_query}%')).all()
    if items:
        for item in items:
            print(f"ID: {item.id}, Product Name: {item.product_name}, Quantity: {item.quantity}, Type: {item.product_type}")
    else:
        print("No products found")

def get_top_3_clients(session):
    sql = text('''
        SELECT customer_name FROM sales ORDER BY dat_reg LIMIT 3
    ''')
    return session.execute(sql).fetchall()

def most_successful_seller(session):
    sql = text('''
         SELECT seller_name, SUM(sum_sale) AS totalsum FROM sales GROUP BY seller_name ORDER BY totalsum DESC LIMIT 1
    ''')
    return session.execute(sql).fetchall()


def main():
    while True:
        print("\nOptions:")
        print("1. Displays information about all products")
        print("2. Displays information about a specific product type")
        print("3. Shows the top 3 regular clients by the registration date")
        print("4. Displays information about the most successful seller")
        print("5. Exit")
        

        choice = input("Choose an option: ")

        if choice == '1':
            get_product()
        elif choice == '2':
            name = input("Enter the product type: ")            
            search_in_products(name)
        elif choice == '3':           
            customers = get_top_3_clients(session)
            for customer in customers:
                print(f'Custormer: {customer.customer_name}')
        elif choice == '4':
            sellers = most_successful_seller(session)
            for seller in sellers:
                print(f'Seller: {seller.seller_name}')
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == '__main__':
    main()
    
    #sales = create_sales(session, 'Alan Rukaa', 2000, 'Ota')
    #print(f'Created sale: {sales.customer_name}, {sales.sum_sale}, {sales.seller_name} ')

    #products = create_products(session, sales.id, 'shoes', 'Standard3', 25, 'Blackandwhite')
    #print(f'Created product: {products.sales_id}, {products.product_type}, {products.product_name}, {products.quantity}, {products.manufacturer}')
    
    session.close()


