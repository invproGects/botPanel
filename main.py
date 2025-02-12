from bot.bot import botMain
from database.queries.orm import AsyncORM
from database.database import create_tables

import asyncio
import logging

logging.basicConfig(
	level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logging.getLogger("aiogram").setLevel(logging.WARNING)



create_tables(recreation = True)

# async def main():
	# await AsyncORM.add_user(12)
	# await AsyncORM.add_user(15)

	# users = await AsyncORM.get_users([12,15])
	# for user in users:
	# 	print(user.tgid)


if __name__ == '__main__':
	asyncio.run(botMain())
