from typing import Callable, Awaitable, Dict, Any
import asyncio

from aiogram import BaseMiddleware
from aiogram.types import Message

from database.queries.orm import AsyncORM

import logging

class NewUsers(BaseMiddleware):
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

		return await handler(event, data)
