from typing import Callable, Awaitable, Dict, Any
import asyncio

from aiogram import BaseMiddleware
from aiogram.types import Message

from database.queries.orm import AsyncBotORM

import logging

from config import log_queue
from log_config import bot_logger



class MetricsMiddleware(BaseMiddleware):
	async def __call__(
			self,
			handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
			event: Message,
			data: Dict[str, Any]
    ) -> Any:
		tgid = event.from_user.id


		if event.text:
			if event.text.startswith("/start"):
				user = await AsyncBotORM.get_user(tgid)
				if not user:
					await AsyncBotORM.add_user(tgid)

					logging.info(f"New User {tgid=}")

		log_entry = f"{event.date} | {event.from_user.id} | {event.from_user.first_name} | {event.text}\n"
		log_queue.put(log_entry)

		log_msg = f"{event.from_user.id} | {event.from_user.username} | {event.text}"
		bot_logger.info(log_msg)

		
		return await handler(event, data)
