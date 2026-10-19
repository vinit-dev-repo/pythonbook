from sqlalchemy import Column, Float, Integer, String, create_engine, select
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(Product(name="Kettle", price=24.99))
    session.commit()
    product = session.scalar(select(Product).where(Product.name == "Kettle"))
    print(product.name, product.price)
