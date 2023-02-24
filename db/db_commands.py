from asyncpg import UniqueViolationError

from db.dp_gino import db
from db.schemas.user import User


#функция 1.1
async def add_user(user_id: int, first_name: str, last_name: str, city: str, age: int, age_min: int,
                   age_max: int, sex: str):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, city=city, age=age,
                    age_min=age_min, age_max=age_max, sex=sex)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


#функция 1.2
async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user
