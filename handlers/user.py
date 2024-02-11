from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.client_kb import user_kb, menu_kb

user_router = Router()


@user_router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(f"Привіт, {message.from_user.first_name}, я твій бот-помічник.\n"
                         f" Для того щоб розпочати роботу, натисніть на одну з кнопок", reply_markup=user_kb)


@user_router.message(F.text == "Допомога")
@user_router.message(Command("help"))
async def command_help(message: Message):
    await message.answer("Поки що, цей розділ недопрацьований, тому введіть команду /menu для подальшої роботи")


@user_router.message(F.text == "Відкрити меню")
@user_router.message(Command("menu"))
async def command_menu(message: Message):
    await message.answer("Ось всі функції які доступні в боті", reply_markup=menu_kb)


