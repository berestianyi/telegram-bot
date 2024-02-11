from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

docx_start_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [InlineKeyboardButton(text="Є файл", callback_data="pdf_file")],
    [InlineKeyboardButton(text="Ввести код ЄДРПО", callback_data="pdf_edrpo")],
    [InlineKeyboardButton(text="Вводити все вручну", callback_data="xpdf_write")]
])

docx_foo_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [InlineKeyboardButton(text="Д АТП", callback_data="docx_atp")],
    [InlineKeyboardButton(text="ЗАЯВА МРЕО ТА НАКАЗ", callback_data="docx_mreo")],
    [InlineKeyboardButton(text="ЗМІНИ ТОВ", callback_data="docx_tov")]
])

atp_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [InlineKeyboardButton(text="РОЯЛ", callback_data="atp_royal")],
    [InlineKeyboardButton(text="РОЛАНД ХМЕЛЬ", callback_data="atp_rolandh")],
    [InlineKeyboardButton(text="РОЛАНД ДАЧНА", callback_data="atp_rolandd")]
])

expire_date_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=[
    [InlineKeyboardButton(text="З СЬОГОДНІШНЬОЇ ДАТИ НА РІК", callback_data="date_year")],
    [InlineKeyboardButton(text="З СЬОГОДНІШНЬОЇ ДАТИ ДО КІНЦЯ РОКУ", callback_data="date_endyear")],
    [InlineKeyboardButton(text="ВВЕСТИ САМОМУ", callback_data="date_write")]
])

is_email_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="немає емайлу", callback_data="email")]
])

is_phone_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="немає телефону", callback_data="phone")]
])

is_address_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="немає адреси", callback_data="address")]
])
