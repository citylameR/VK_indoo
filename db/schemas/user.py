from sqlalchemy import Column, BigInteger, String, sql, ForeignKey
import asyncio

from data import config
from db.dp_gino import TimedBaseModel, db


class User(TimedBaseModel):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    city = Column(BigInteger)
    age = Column(BigInteger)
    age_min = Column(BigInteger)
    age_max = Column(BigInteger)
    sex = Column(BigInteger)

    query: sql.select


class Black_list(TimedBaseModel):
    __tablename__ = "black_list"

    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    reason = Column(String)
    status = Column(String)


query: sql.select


class Favorites(TimedBaseModel):
    __tablename__ = "favorites"

    user_id = Column(BigInteger, ForeignKey("users.user_id"))
    favorite_id = Column(BigInteger)

    query: sql.select

    def __str__(self):
        return f"{self.favorites_id}"


class Offer(TimedBaseModel):
    __tablename__ = "offer"

    offer_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"))

    query: sql.select
