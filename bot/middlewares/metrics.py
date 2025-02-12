from typing import Callable, Awaitable, Dict, Any
import asyncio

from aiogram import BaseMiddleware
from aiogram.types import Message

from database.queries.orm import AsyncORM

import logging

from config import log_queue

class MetricsMiddleware(BaseMiddleware):
	async def __call__(
			self,
			handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
			event: Message,
			data: Dict[str, Any]
    ) -> Any:
		tgid = event.from_user.id
		
		if event.text.startswith("/start"):
			user = await AsyncORM.get_user(tgid)
			if not user:
				await AsyncORM.add_user(tgid)

				logging.info(f"New User {tgid=}")

		log_entry = f"{event.date} | {event.from_user.id} | {event.text}\n"
		log_queue.put(log_entry)

		return await handler(event, data)
