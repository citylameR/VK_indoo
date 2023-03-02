from asyncpg import UniqueViolationError

from db.dp_gino import db
from db.schemas.user import User, Favorites


async def add_user(
    user_id: int,
    first_name: str,
    last_name: str,
    city: int,
    age: int,
    age_min: int,
    age_max: int,
    sex: int,
):
    """
    Функция добавляет пользователя в базу данных
    """

    try:
        user = User(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            city=city,
            age=age,
            age_min=age_min,
            age_max=age_max,
            sex=sex,
        )
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")


async def add_fav(user_id: int, fav_id: int):
    try:
        favorite = Favorites(user_id=user_id, favorite_id=fav_id)
        await favorite.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")


async def select_user(user_id):
    """
    Принимает user_id, возвращает данные о пользователе с таблицы Users
    """

    user = await User.query.where(User.user_id == user_id).gino.first()
    if user == None:
        return None
    else:
        usr = {}
        usr["id"] = user.user_id
        usr["first_name"] = user.first_name
        usr["last_name"] = user.last_name
        usr["city"] = user.city
        usr["sex"] = user.sex
        usr["age"] = user.age
        usr["age_min"] = user.age_min
        usr["age_max"] = user.age_max
        return usr


async def list_favorites(user_id):
    """
    Функция принимает user_id и возвращает список избранных пользователей
    """

    user = await Favorites.query.where(Favorites.user_id == user_id).gino.all()
    favorites_list = []
    for i in user:
        favorites_list.append(i.favorite_id)
    return favorites_list


# async def delete_favorites(user_id):
#     """
#     Функция принимает user_id и удаляет избранного пользователя
#     """
#
#     favorite = await  Favorite_person.query.where(Favorite_person.user_id == user_id).gino.all()
#     await favorite.delete()
