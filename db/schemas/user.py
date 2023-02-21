from sqlalchemy import Column, BigInteger, String, sql, ForeignKey, Integer
import asyncio

from data import config
from db.dp_gino import TimedBaseModel, db



class User(TimedBaseModel):

    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    city = Column(String(200))
    age = Column(BigInteger)
    age_min = Column(BigInteger)
    age_max = Column(BigInteger)
    sex = Column(String(30))

    query: sql.select

class Favorites(TimedBaseModel):

    __tablename__ = 'favorites'

    favorite_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'))

    query: sql.select


class Black_list(TimedBaseModel):

    __tablename__ = 'black_list'

    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    reason = Column(String)
    status = Column(String)

query: sql.select


class Photo(TimedBaseModel):

    __tablename__ = 'photo'


    user_id = Column(BigInteger, primary_key=True)
    photo_id = Column(String, primary_key=True)

    query: sql.select

# class Offer(TimedBaseModel):
#
#     __tablename__ = 'offer'
#
#     offer_id = Column(BigInteger, primary_key=True)
#     user_id = Column(BigInteger, ForeignKey('users.user_id'))
#     photo_id = Column(String, ForeignKey('photo.photo_id'))

    query: sql.select

async def on_start_up():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()


loop = asyncio.get_event_loop()
loop.run_until_complete(on_start_up())