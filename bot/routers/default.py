from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router(name = "default")

@router.message(CommandStart())
async def start(msg: Message):
	await msg.answer("Hello, from bot @atgbuy")

@router.message()
async def ans(msg: Message):
	await msg.answer(msg.text)