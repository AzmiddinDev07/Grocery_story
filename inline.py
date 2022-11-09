from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import logging
start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍰Shirinliklar",callback_data="🍰Shirinliklar"),
            KeyboardButton(text="🍹Ichimliklar",callback_data="🍹Ichimliklar"),
            KeyboardButton(text="🥩Go'sht mahsulotlari",callback_data="🥩Go'sht mahsulotlari"),
            ],
            [
            KeyboardButton(text="🍎Mevalar",callback_data="🍎Mevalar"),
            KeyboardButton(text="🥕Sabzavotlar",callback_data="🥕Sabzavotlar"),
            KeyboardButton(text="🥛Sut va tuxum🥚",callback_data="🥛Sut va tuxum🥚"),
        ],
    ],
resize_keyboard=True
)
menyuShirin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Shekolad"),
            KeyboardButton(text="Pirog"),
            KeyboardButton(text="Picheyni"),
            KeyboardButton(text="Keykslar"),
        ],
        [
            KeyboardButton(text="Orqaga"),
        ],
    ],
resize_keyboard=True
)
menyuIchim = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Coca Cola"),
            KeyboardButton(text="Moxito"),
            KeyboardButton(text="Fanta"),
            KeyboardButton(text="Red Bull"),
        ],
        [
            KeyboardButton(text="Orqaga")
        ],
    ],
resize_keyboard=True
)
menyuGosht = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mol go'shti"),
            KeyboardButton(text="Qo'y go'shti"),
            KeyboardButton(text="Tovuq go'shti"),
        ],
        [
            KeyboardButton(text="Orqaga"),
        ],
    ],
resize_keyboard=True
)
meval = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Olma"),
            KeyboardButton(text="Banan"),
            KeyboardButton(text="Kivi"),
            ],
        [
            KeyboardButton(text="Mandarin"),
            KeyboardButton(text="Uzum"),
            KeyboardButton(text="Gilos"),
            ],

        [
            KeyboardButton(text="Orqaga"),
        ],
    ],
resize_keyboard=True
)
menyuPoliz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pomidor"),
            KeyboardButton(text="Bodring"),
            ],
        [
            KeyboardButton(text="Karam"),
            KeyboardButton(text="Baqlajon"),
            KeyboardButton(text="Piyoz"),
            ],
        [
            KeyboardButton(text="Orqaga"),
        ],
    ],
resize_keyboard=True
)
menyuSut = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="sut"),
            KeyboardButton(text="tuxum"),
        ],
        [
            KeyboardButton(text="Orqaga"),
        ],
    ],
resize_keyboard=True
)

menuBosh = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️Orqaga",callback_data="⬅️Orqaga"),
        ],
    ],
)

menuzakaz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚚Buyurtma",callback_data="🚚Buyurtma"),
            InlineKeyboardButton(text="⬅️Orqaga",callback_data="⬅️Orqaga"),
        ],
    ],
)
menuzakaz1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗺️Location",request_location=True),
            KeyboardButton(text="📞Contact",request_contact=True),
        ],
    ],
resize_keyboard=True
)
