from bot.bot import botMain
from database.queries.orm import AsyncBotORM
from database.database import create_tables
from bot.backend.server import app

import asyncio
import uvicorn
import threading

create_tables()

if __name__ == '__main__':
	server_th = threading.Thread(
		target = uvicorn.run,
		args=[app],
		kwargs={"port": 8000},
		daemon=True
	)
	
	server_th.start()

	asyncio.run(botMain())