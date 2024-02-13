# from aiogram import Dispatcher
# from create_bot import bot, dp
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
#
#
# class FSMtest(StatesGroup):
#     name = State()
#     car_info = State()
#     phone = State()
#
#
# @dp.message_handler(commands="test", state=None)
# async def test_start(message: Message):
#     await FSMtest.name.set()
#     await message.reply('Напиши имя человека')
#
#git help

# @dp.message_handler(content_types=['text'], state=FSMtest.name)
# async def load_name(message: Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await FSMtest.next()
#     await message.reply("Напиши имя машины")
#
#
# def register_handlers_test(dp: Dispatcher):
#     dp.register_message_handler(test_start, commands=['test'])
