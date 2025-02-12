import asyncio

from aiogram import Bot,Dispatcher

from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
from bot.routers.default import router as main_router
from bot.middlewares.newUsers import NewUsers as NewUsersMiddleware

import logging


async def main():
	bot = Bot(settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
	dp = Dispatcher()

	dp.message.middleware(NewUsersMiddleware())

	dp.include_router(main_router)

	logging.info("Bot started")

	await dp.start_polling(bot)