import os

from aiogram import F, Router
from create_bot import Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.docx_kb import docx_start_kb, docx_foo_kb, atp_kb
from utils.atp_file_extraction import extraction_of_tov_name, is_tov, pdf_extraction


docx_router = Router()


class DocxData(StatesGroup):
    user_choice = State()
    pdf_path = State()
    foo_choice = State()
    atp_choice = State()
    expire_date = State()
    vehicle_data = State()
    name = State()
    tov_name = State()
    company = State()
    code = State()
    address = State()
    email = State()
    phone = State()


@docx_router.message(F.text == "Зробити документ")
@docx_router.message(Command("docx_file"))
async def docx_file_start(message: Message, state: FSMContext):
    await state.set_state(DocxData.user_choice)
    await message.answer("Що з переліченого у вас є?", reply_markup=docx_start_kb)


@docx_router.callback_query(DocxData.user_choice, F.data.startswith("pdf_"))
async def pdf_file_answer(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]

    if action == "file":
        await state.update_data(user_choice="file")
        await state.set_state(DocxData.pdf_path)
        await callback.message.answer("Скиньте файл")

    elif action == "edrpo":
        await state.update_data(user_choice="code")

        await state.clear()
        await callback.message.answer("Фукція в розробці")

    # elif action == "write":
    #     await state.update_data(user_choice="write")
    #     await state.clear()
    #     await callback.message.answer("Фукція в розробці")

    else:
        await state.clear()
        await callback.message.answer("Помилка")

# ------------------------------------------------------------------------


@docx_router.message(DocxData.pdf_path, F.document)
async def pdf_file_docx(message: Message, state: FSMContext, bot: Bot):
    os.remove("user_file.pdf")
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = "user_file.pdf"
    await state.update_data(pdf_path=file_path)
    await bot.download_file(file_path, file_name)

    name = extraction_of_tov_name(file_name)
    info_dict = pdf_extraction(file_name)

    await state.set_state(DocxData.name)
    await state.update_data(name=info_dict["name"])

    await state.set_state(DocxData.code)
    await state.update_data(code=info_dict["code"])

    await state.set_state(DocxData.company)
    await state.update_data(company=info_dict["company"])

    await state.set_state(DocxData.email)
    await state.update_data(email=info_dict["email"])

    await state.set_state(DocxData.address)
    await state.update_data(address=info_dict["address"])

    await state.set_state(DocxData.phone)
    await state.update_data(phone=info_dict["phone"])

    if is_tov(file_name):
        await state.set_state(DocxData.tov_name)
        await message.answer(f"Введіть це іʼмя в родовому відмінку\n\n {name}\n\n будь ласка")

        @docx_router.message(DocxData.tov_name, F.text)
        async def tov_name_check(message2: Message):
            await state.update_data(tov_name=message2.text)
            await state.set_state(DocxData.foo_choice)
            await message2.answer("Дякую", reply_markup=docx_foo_kb)
    else:
        await state.set_state(DocxData.foo_choice)
        await message.answer("Дякую", reply_markup=docx_foo_kb)
    #
    # for i in range(30):
    #     if os.path.exists(file_name):
    #         await state.set_state(DocxData.tov_name)
    #         name = extraction_of_tov_name(file_name)
    #         await message.answer(f"Введіть це іʼмя в родовому відмінку\n\n {name}\n\n будь ласка")
    #
    #         @docx_router.message(DocxData.tov_name, F.text)
    #         async def tov_name_check():
    #             await state.update_data(tov_name=message.text)
    #             await state.set_state(DocxData.foo_choice)
    #             await message.answer("Дякую", reply_markup=docx_foo_kb)
    #     else:
    #         await asyncio.sleep(2)
    #         await state.set_state(DocxData.foo_choice)
    #         await message.answer("Зачекайте відбувається загрузка файлу")

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


# @docx_router.callback_query(DocxData.foo_choice, F.data.startswith("docx_"))
# async def docx_foo(callback: CallbackQuery, state: FSMContext):
#     action = callback.data.split("_")[1]
#
#     if action == "atp":
#         await state.update_data(foo_choice="ATP")
#         await state.set_state(DocxData.atp_choice)
#         await callback.message.answer("Виберіть один з варіантів", reply_markup=atp_kb)
#     elif action == "mreo":
#         await state.update_data(foo_choice="MREO")
#         await state.clear()
#         await callback.message.answer("Функція в розробці")
#     elif action == "tov":
#         await state.update_data(foo_choice="TOV")
#         await state.clear()
#         await callback.message.answer("Функція в розробці")



