from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from handlers.docx.user import DocxData
from keyboards.docx_kb import is_email_kb, is_phone_kb, is_address_kb, atp_kb

docx_router = Router()


@docx_router.callback_query(DocxData.user_choice, F.data == "xpdf_write")
async def pdf_file_answer(callback: CallbackQuery, state: FSMContext):
    await state.update_data(user_choice="write")
    await state.set_state(DocxData.code)
    await callback.message.answer("Введіть індификаційний код")

    @docx_router.message(DocxData.code, F.text)
    async def code_write(message: Message):
        await state.update_data(code=message.text)
        if len(message.text) == 8:
            await state.set_state(DocxData.name)
            await message.answer("Введіть іʼмя керівника ТОВ")

            @docx_router.message(DocxData.name, F.text)
            async def name_write(message2: Message):
                await state.update_data(name=message2.text)
                name = message2.text
                await state.set_state(DocxData.tov_name)
                await message2.answer(f"Введіть іʼмя {name} в родовому відмінку")

                @docx_router.message(DocxData.tov_name, F.text)
                async def tov_name_write(message3: Message):
                    await state.update_data(tov_name=message3.text)
                    await state.set_state(DocxData.company)
                    await message3.answer(f"Введіть назву ТОВ (без скобок та слова ТОВ)")

                    @docx_router.message(DocxData.company, F.text)
                    async def company_write(message4: Message):
                        await state.update_data(company=message4.text)
                        await state.set_state(DocxData.email)
                        await message4.answer("Введіть емейл", reply_markup=is_email_kb)

        elif len(message.text) == 10:
            await state.set_state(DocxData.name)
            await message.answer("Введіть іʼмя керівника ФОП")

            @docx_router.message(DocxData.name, F.text)
            async def fop_name_write(message2: Message):
                await state.update_data(name=message2.text)
                await state.set_state(DocxData.email)
                await message2.answer("Введіть емейл", reply_markup=is_email_kb)

        else:
            await state.clear()
            await message.answer("Неправильно введено код, починайте все з початку")

    @docx_router.message(DocxData.email, F.text.endswith(".com"))
    @docx_router.message(DocxData.email, F.text.endswith(".net"))
    @docx_router.message(DocxData.email, F.text.endswith(".ru"))
    @docx_router.message(DocxData.email, F.text.endswith(".ua"))
    async def email_write(message: Message):
        await state.update_data(email=message.text)
        await state.set_state(DocxData.phone)
        await message.answer("Введіть телефон", reply_markup=is_phone_kb)

        @docx_router.message(DocxData.phone, F.text)
        async def e_phone_write(message2: Message):
            await state.update_data(phone=message2.text)
            await state.set_state(DocxData.address)
            await message2.answer("Введіть адресу", reply_markup=is_address_kb)

        @docx_router.message(DocxData.address, F.text)
        async def e_address_write(message2: Message):
            await state.update_data(address=message2.text)
            await state.set_state(DocxData.atp_choice)
            await message2.answer("Виберіть один з варіантів", reply_markup=atp_kb)

    @docx_router.callback_query(DocxData.email, F.data == "email")
    async def without_email_write(callback2: CallbackQuery):
        await state.update_data(email=None)
        await state.set_state(DocxData.phone)
        await callback2.message.answer("Введіть телефон", reply_markup=is_phone_kb)

        @docx_router.message(DocxData.phone, F.text)
        async def em_phone_write(message2: Message):
            await state.update_data(phone=message2.text)
            await state.set_state(DocxData.address)
            await message2.answer("Введіть адресу", reply_markup=is_address_kb)

        @docx_router.message(DocxData.address, F.text)
        async def em_address_write(message2: Message):
            await state.update_data(address=message2.text)
            await state.set_state(DocxData.atp_choice)
            await message2.answer("Виберіть один з варіантів", reply_markup=atp_kb)

    @docx_router.callback_query(DocxData.phone, F.data == "phone")
    async def phone_write(callback2: CallbackQuery):
        await state.update_data(phone=None)
        await state.set_state(DocxData.address)
        await callback2.message.answer("Введіть адресу", reply_markup=is_address_kb)

        @docx_router.message(DocxData.address, F.text)
        async def address_write(message2: Message):
            await state.update_data(phone=message2.text)
            await state.set_state(DocxData.atp_choice)
            await message2.answer("Виберіть один з варіантів", reply_markup=atp_kb)

    @docx_router.callback_query(DocxData.address, F.data == "address")
    async def no_address_write(callback2: CallbackQuery):
        await state.update_data(address=None)
        await state.set_state(DocxData.atp_choice)
        await callback2.message.answer("Виберіть один з варіантів", reply_markup=atp_kb)


# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------


@docx_router.callback_query(DocxData.foo_choice, F.data.startswith("docx_"))
async def docx_foo(callback: CallbackQuery, state: FSMContext):
    action = callback.data.split("_")[1]

    if action == "atp":
        await state.update_data(foo_choice="ATP")
        await state.set_state(DocxData.atp_choice)
        await callback.message.answer("Виберіть один з варіантів", reply_markup=atp_kb)
    elif action == "mreo":
        await state.update_data(foo_choice="MREO")
        await state.clear()
        await callback.message.answer("Функція в розробці")
    elif action == "tov":
        await state.update_data(foo_choice="TOV")
        await state.clear()
        await callback.message.answer("Функція в розробці")


