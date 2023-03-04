from asyncpg import UniqueViolationError
from pprint import pprint

from db.dp_gino import db
from db.schemas.user import User, Favorites, Offer, Black_list



async def add_user(
    user_id: int,
    first_name: str,
    last_name: str,
    city: int,
    age: int,
    age_min: int,
    age_max: int,
    sex: int,
    city_title: str
):

    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, city=city, age=age,
                    age_min=age_min, age_max=age_max, sex=sex, city_title=city_title)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')

async def upd_user(
    user_id: int,
    first_name: str,
    last_name: str,
    city: int,
    age: int,
    age_min: int,
    age_max: int,
    sex: int,
    city_title: str
    ):

    updated_user = await User.query.where(User.user_id == user_id).gino.first()
    await updated_user.update(first_name=first_name,
                              last_name=last_name,
                              city=city, age=age,
                              age_min=age_min,
                              age_max=age_max,
                              sex=sex,
                              city_title=city_title).apply()
async def add_fav(user_id: int, fav_id: int):
    try:
        favorite = Favorites(user_id=user_id, favorite_id=fav_id)
        await favorite.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")

    return updated_user

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    if user == None:
        return None
    else:
        info = {}
        info['first_name'] = user.first_name
        info['last_name'] = user.last_name
        info['age'] = user.age
        info['age_min'] = user.age_min
        info['age_max'] = user.age_max
        info['sex'] = user.sex
        info['city'] = user.city
        info['id'] = user.user_id
        info['city_title'] = user.city_title
        return info


async def add_fav(user_id, favorite_id, name):
    favorite = Favorites(user_id=user_id, favorite_id=favorite_id, name=name)
    await favorite.create()
    return 'added'


async def list_favorites(user_id):
    user = await Favorites.query.where(Favorites.user_id == user_id).gino.all()
    favorites_list = []
    for i in user:
        favorites_list.append({"name": i.name, "id": i.favorite_id})
    return favorites_list


async def delete_favorite(user_id, fav_id):

    await Favorites.delete.where(Favorites.favorite_id == fav_id).gino.first()


async def add_offer(user_id, offered_id):
    user = await db.scalar(db.exists().where(Offer.offer_id == offered_id).select())
    offered = Offer(offer_id=offered_id, user_id=user_id)
    if user is False:
        await offered.create()
        return 'added'


async def offers(user_id):
    user = await Offer.query.where(Offer.user_id == user_id).gino.all()
    offer_list = []
    for i in user:
        offer_list.append(i.offer_id)
    return offer_list

async def add_bl(user_id, reason, status):
    block = Black_list(user_id=user_id, reason=reason, status=status)
    await block.create()
    return 'added'

async def chk_bl(user_id):
    user = await db.scalar(db.exists().where(Black_list.user_id == user_id).select())
    return user