# import asyncio
# from db import quick_commands as commands
# from data import config
# from db.dp_gino import db
#
#
# async def db_test():
#     await db.set_bind(config.POSTGRES_URI)
#     # await db.gino.drop_all()
#     # await db.gino.create_all()
#     print("избранное")
#     await commands.add_favorites_person(11, 12, "xx")
#     await commands.list_favorites(1)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(db_test())
