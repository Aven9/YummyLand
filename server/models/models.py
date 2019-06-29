from sqlalchemy import Column, String, create_engine, ForeignKey, TIMESTAMP, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

base = declarative_base()


class User(base):
    __tablename__ = 'User'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    email = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP, nullable=False)


class Address(base):
    __tablename__ = 'Address'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    province = Column(String, nullable=False)
    city = Column(String, nullable=False)
    detail = Column(String, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)


class Order(base):
    __tablename__ = 'Order'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    status = Column(INTEGER, nullable=False, default=0)
    createdAt = Column(TIMESTAMP, nullable=False)


class ShopClassification(base):
    __tablename__ = 'ShopClassification'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    text = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP, nullable=False)


class ShopUser(base):
    __tablename__ = 'ShopUser'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP, nullable=False)


class FoodClassification(base):
    __tablename__ = 'FoodClassification'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    text = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP, nullable=False)


class Food(base):
    __tablename__ = 'Food'

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    price = Column(INTEGER, nullable=False)
    name = Column(String, nullable=False)
    imageUrl = Column(String, nullable=False)
    createdAt = Column(TIMESTAMP, nullable=False)


def create(postgres_url):
    engine = create_engine(postgres_url)
    base.metadata.create_all(engine)
    db = scoped_session(sessionmaker(bind=engine))
    return db
