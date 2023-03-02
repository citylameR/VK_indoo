from asyncpg import UniqueViolationError

from db.dp_gino import db
from db.schemas.user import User, Favorite_person, Favorites, Offer


async def add_user(user_id: int, first_name: str, last_name: str, city: int, age: int, age_min: int,
                   age_max: int, sex: int):

    """
    Функция добавляет пользователя в базу данных
    """

    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, city=city, age=age,
                    age_min=age_min, age_max=age_max, sex=sex)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')



async def select_user(user_id):

    """
    Принимает user_id, возвращает данные о пользователе с таблицы Users
    """

    user = await User.query.where(User.user_id == user_id).gino.first()
    if user == True:
        print('Пользователь есть')

async def add_favorites_person(user_id, favorites_id, url):
    """
    Функция принимает на вход user_id, favorite_id, и url пользователя, которого лайкнули и добавляет его в БД
    """

    user_favorite = await db.scalar(db.exists().where(Favorite_person.user_id == user_id and Favorite_person.favorites_id == favorites_id).select())
    if user_favorite is False:
        favorite_person = Favorite_person(user_id=user_id, favorites_id=favorites_id)
        favorite = Favorites(favorites_id=favorites_id, url=url)
        await favorite.create()
        await favorite_person.create()

        return True


async def list_favorites(user_id):
    """
    Функция принимает user_id и возвращает список избранных пользователей
    """

    user = await Favorite_person.query.where(Favorite_person.user_id == user_id).gino.all()
    favorites_list = []
    for i in user:
        favorites_list.append(i)

    return favorites_list


async def delete_favorites(user_id):
    """
    Функция принимает user_id и удаляет избранного пользователя
    """

    favorite = await  Favorite_person.query.where(Favorite_person.user_id == user_id).gino.all()
    await favorite.delete()

async def add_offer(offered_id, user_id):
    user = await db.scalar(db.exists().where(Offer.user_id == user_id and Offer.offer_id == offered_id).select())
    if user is False:
        offered = Offer(offer_id=offered_id, user_id=user_id)
        await offered.create()
        return 'added'