from bot.bot import botMain
from database.queries.orm import AsyncORM
from database.database import create_tables
from backend.server import app

import asyncio
import logging
import uvicorn
import threading

logging.basicConfig(
	level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logging.getLogger("aiogram").setLevel(logging.WARNING)



create_tables()

# async def main():
	# await AsyncORM.add_user(12)
	# await AsyncORM.add_user(15)

	# users = await AsyncORM.get_users([12,15])
	# for user in users:
	# 	print(user.tgid)

def run_uvicon():
	uvicorn.run(app, host = "127.0.0.1", port = 8000)


if __name__ == '__main__':
	main_thread = threading.Thread(target=run_uvicon, daemon=True)
	main_thread.start()

	asyncio.run(botMain())

