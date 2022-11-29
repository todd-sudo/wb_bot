from aiogram import types
from aiogram.utils.callback_data import CallbackData

from src.handlers.client import get_products, parse_products
from src.loader import dp
from config import DOMAIN


def get_callback_data_r_url():
    _cb = CallbackData("r", "r_url")
    return _cb


def price_keyboard(_cb, _next: str, _previous: str) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    str_replace = DOMAIN + "/api/parser/get-underprice-products/?"

    if _previous:
        _previous = _previous.replace(str_replace, "")
        keyboard.add(
            types.InlineKeyboardButton(
                text="⬅️ Назад", callback_data=_cb.new(r_url=_previous)
            )
        )
    keyboard.add(types.InlineKeyboardButton(text="⏺", callback_data="nil"))
    if _next:
        _next = _next.replace(str_replace, "")
        keyboard.add(
            types.InlineKeyboardButton(
                text="Вперед ➡️", callback_data=_cb.new(r_url=_next)
            )
        )

    return keyboard


# "Заниженная цена WB (<5%)" и "Распродажа WB (>5%)"
cb = get_callback_data_r_url()


@dp.message_handler(commands=["underprice"])
async def get_underprice_products_handler(message: types.Message):
    data = get_products('lt')
    if not data:
        await message.answer("🆘 Произошла ошибка получения данных!")
        return
    _next = data.get("next")
    _previous = data.get("previous")
    products = data.get("results")
    msg = parse_products(products)
    await message.answer(
        text=msg,
        reply_markup=price_keyboard(cb, _next, _previous)
    )


@dp.message_handler(commands=["sale"])
async def get_sale_products_handler(message: types.Message):
    data = get_products('gt')
    if not data:
        await message.answer("🆘 Произошла ошибка получения данных!")
        return
    _next = data.get("next")
    _previous = data.get("previous")
    products = data.get("results")
    msg = parse_products(products)
    await message.answer(
        text=msg,
        reply_markup=price_keyboard(cb, _next, _previous)
    )


@dp.callback_query_handler(cb.filter())
async def new_previous_handler(call: types.CallbackQuery, callback_data: dict):
    await call.answer("Информация загружается")
    url = callback_data["r_url"]
    url = DOMAIN + "/api/parser/get-underprice-products/?" + url

    data = get_products('gt', url)
    if not data:
        await call.message.answer("🆘 Произошла ошибка получения данных!")
        return
    _next = data.get("next")
    _previous = data.get("previous")
    products = data.get("results")
    msg = parse_products(products)
    await call.message.edit_text(
        text=msg,
        reply_markup=price_keyboard(cb, _next, _previous)
    )


@dp.callback_query_handler(text="nil")
async def null_handler(call: types.CallbackQuery):
    await call.answer("тык!")

