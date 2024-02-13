import os
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from handlers.docx.user import DocxData
from keyboards.docx_kb import expire_date_kb
from keyboards.client_kb import menu_kb
from utils.utils import year_from_today, end_of_year
from utils.templates.royal import royal_doc
from utils.templates.roland import roland_doc

docx_router = Router()


@docx_router.callback_query(DocxData.atp_choice, F.data.startswith("atp_"))
async def atp_start(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]

    if action == "royal":
        await state.update_data(atp_choice="royal")
    elif action == "rolandh":
        await state.update_data(atp_choice="roland_h")
    elif action == "rolandd":
        await state.update_data(atp_choice="roland_d")

    await state.set_state(DocxData.expire_date)
    await callback.message.answer("На скільки складається договір", reply_markup=expire_date_kb)


@docx_router.callback_query(DocxData.expire_date, F.data.startswith("date_"))
async def expire_date(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]

    if action == "year":
        await state.update_data(expire_date=year_from_today())
        await state.set_state(DocxData.vehicle_data)
        await callback.message.answer(f"Введіть всі ТЗ в форматі\n"
                                      f"1) номер, марка, рік;\n"
                                      f"2) номер, марка, рік;\n ...")
    elif action == "endyear":
        await state.update_data(expire_date=end_of_year())
        await state.set_state(DocxData.vehicle_data)
        await callback.message.answer(f"Введіть всі ТЗ в форматі\n"
                                      f"1) номер, марка, рік;\n"
                                      f"2) номер, марка, рік;\n ...")
    elif action == "write":
        await callback.message.answer("Напишіть дату закінчення договору в форматі дд.мм.рррр")

        @docx_router.message(DocxData.expire_date, F.text)
        async def write_expire_date(message: Message):
            await state.update_data(expire_date=message.text)
            await state.set_state(DocxData.vehicle_data)
            await callback.message.answer(f"Введіть всі ТЗ в форматі\n"
                                          f"1) номер, марка, рік;\n"
                                          f"2) номер, марка, рік;\n ...")


@docx_router.message(DocxData.vehicle_data, F.text.startswith("1)"))
async def vehicle_data(message: Message, state: FSMContext):
    await state.update_data(vehicle_data=message.text)
    user_data = await state.get_data()
    await state.clear()
    if user_data["atp_choice"] == "royal":
        file_path = royal_doc(user_data)
    else:
        file_path = roland_doc(user_data)

    file = FSInputFile(file_path)
    await message.reply_document(file, reply_markup=menu_kb)
    os.remove(file_path)

