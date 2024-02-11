import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import TOKEN

loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()




