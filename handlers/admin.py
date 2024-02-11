from create_bot import bot, dp
from config import admin_id


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

