from aiogram import Router
from aiogram.types import Message

msg_router = Router()


@msg_router.message()
async def echo_command(message: Message):
    await message.answer("Невідомий текст, для того щоб розпочати введіть команду /start")

