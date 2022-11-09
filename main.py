from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp, bot

import logging

from inline import start_btn, menyuShirin, menyuIchim, menyuGosht, meval, menyuPoliz, menyuSut, menuzakaz, menuzakaz1,menuBosh


@dp.message_handler(commands='start')
async def start(message: Message):
    txt = f" Bismillah \n Assalomu-alaykum {message.from_user.full_name}!\n" \
          f" Grocery Story Botiga Hush kelibsiz.\n" \
          f" Bu yerda siz halol oziq-ovqat mahsulotlarini topishingiz mumkin.\n" \
          f" Siz bizdan qilgan xaridingiz orqali tekin yetkazib berish xizmatidan foydalanishingiz mumkin!\n" \
          f" Xarid qilish uchun👇"
    await message.answer_photo(open("image/Grocery.jpg", "rb"), txt, reply_markup=start_btn,)


@dp.message_handler(text="🍰Shirinliklar")
async def shirin(message: Message):
    txt = f"Bismillah:\n" \
          f"Sizga shirinliklarimiz yoqadi degan umiddamiz!\n"
    await message.answer_photo(open("image/shirinlik.jpeg", "rb"), txt, reply_markup=menyuShirin)
    await message.answer(reply_markup=menuBosh)

@dp.message_handler(text="🍹Ichimliklar")
async def ichim(message: Message):
    await message.answer_photo(open("image/ichimliklar.jpeg", "rb"), reply_markup=menyuIchim)
    await message.answer(reply_markup=menuBosh)

@dp.message_handler(text="🥩Go'sht mahsulotlari")
async def gosht(message: Message):
    txt = f"Halol Go'sht Alhamdulillah:\n"
    await message.answer_photo(open("image/Gosht.jpeg", "rb"), txt, reply_markup=menyuGosht)
    await message.answer(reply_markup=menuBosh)

@dp.message_handler(text='🍎Mevalar')
async def meva(message: Message):
    txt = f"Sifatli mevalar:\n"
    await message.answer_photo(open("image/Mevalar.jpg", "rb"), txt, reply_markup=meval)
    await message.answer(reply_markup=menuBosh)

@dp.message_handler(text='🥕Sabzavotlar')
async def sabza(message: Message):
    txt = f"Sabzavotlar:\n"
    await message.answer_photo(open("image/Sabzavot.jpeg", "rb"), txt, reply_markup=menyuPoliz)
    await message.answer(reply_markup=menuBosh)

@dp.message_handler(text='🥛Sut va tuxum🥚')
async def sut(message: Message):
    txt = f"salom:\n"
    await message.answer_photo(open("image/sutuxm.jpeg", "rb"), txt, reply_markup=menyuSut)
    await message.answer(reply_markup=menuBosh)

@dp.message_handler(text='Shekolad')
async def shirin(message: Message):
    txt = f"Chokotella\n Narxi = 25000 so'm:\n"
    await message.answer_photo(open("image/Chokotella.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text='Pirog')
async def shirin(message: Message):
    txt = f"Pirog\n Narxi = 37000 so'm:\n"
    await message.answer_photo(open("image/Pirog.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text='Picheyni')
async def shirin(message: Message):
    txt = f"Picheyni\n Narxi = 55000 so'm:\n"
    await message.answer_photo(open("image/Picheyni.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text='Keykslar')
async def shirin(message: Message):
    txt = f"Keykslar\n Narxi = 78000 so'm:\n"
    await message.answer_photo(open("image/keyks.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text='Pepsi')
async def ichim(message: Message):
    txt = f"Pepsi" \
          f"1 L Narxi = 8000 so'm:\n" \
          f"1,5 L Narxi = 10000 so'm:\n" \
          f"2 L Narxi = 12000 so'm"
    await message.answer_photo(open("image/Pepsi.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text='Coca Cola')
async def ichim(message: Message):
    txt = f"Coca Cola" \
          f"1l Narxi = 7000 so'm:\n" \
          f"1,5l Narxi = 11000 so'm:\n" \
          f"2l Narxi = 13000 so'm:\n"
    await message.answer_photo(open("image/Coca Cola.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text='Moxito')
async def ichim(message: Message):
    txt = f"Moxito" \
          f"Narxi = 12000 so'm:\n"
    await message.answer_photo(open("image/ moxito.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text='Fanta')
async def ichim(message: Message):
    txt = f"Fanta" \
          f"1l Narxi = 8000 so'm:\n" \
          f"1,5l Narxi = 11000 so'm:\n" \
          f"2l Narxi = 12000 so'm:\n"
    await message.answer_photo(open("image/Fanta.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text='Red Bull')
async def ichim(message: Message):
    txt = f"Red Bull" \
          f"Narxi = 24000 so'm:\n"
    await message.answer_photo(open("image/Red Bull.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Mol go'shti")
async def gosht(message: Message):
    txt = f"Laxim\n" \
          f" Narxi = 90 000 so'm:\n"
    await message.answer_photo(open("image/mol gosht.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Qo'y go'shti")
async def gosht(message: Message):
    txt = f"Qovurg'a\n" \
          f"Narxi 60 000 so'm\n" \
          f" Narxi = 90000 so'm:\n"
    await message.answer_photo(open("image/qovurga.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Tovuq go'shti")
async def gosht(message: Message):
    txt = f"Tovuq go'shti 1 kg\n" \
          f" Narxi = 40000 so'm:\n"
    await message.answer_photo(open("image/tovuq.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Olma")
async def meva(message: Message):
    txt = f"Olma 1 kg\n" \
          f" Narxi = 9000 so'm:\n"
    await message.answer_photo(open("image/olma.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Banan")
async def meva(message: Message):
    txt = f"Banan 1 kg\n" \
          f" Narxi = 25000 so'm:\n"
    await message.answer_photo(open("image/Banan.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Kivi")
async def meva(message: Message):
    txt = f"Kivi 1 kg\n" \
          f" Narxi = 47000 so'm:\n"
    await message.answer_photo(open("image/kivi-mevasi-foydasi.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Mandarin")
async def meva(message: Message):
    txt = f"Mandarin 1 kg\n" \
          f" Narxi = 38000 so'm:\n"
    await message.answer_photo(open("image/mandarin.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Uzum")
async def meva(message: Message):
    txt = f"Uzum 1 kg\n" \
          f" Narxi = 30000 so'm:\n"
    await message.answer_photo(open("image/uzum.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Gilos")
async def meva(message: Message):
    txt = f"Gilos 1 kg\n" \
          f" Narxi = 33700 so'm:\n"
    await message.answer_photo(open("image/Gilos.jpg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Pomidor")
async def sabza(message: Message):
    txt = f"Pomidor 1 kg\n" \
          f" Narxi = 5400 so'm:\n"
    await message.answer_photo(open("image/pomidor.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Bodring")
async def sabza(message: Message):
    txt = f"Bodring 1 kg\n" \
          f" Narxi = 3000 so'm:\n"
    await message.answer_photo(open("image/bodring.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Karam")
async def sabza(message: Message):
    txt = f"Karam 1 kg\n" \
          f" Narxi = 7000 so'm:\n"
    await message.answer_photo(open("image/karam.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Baqlajon")
async def sabza(message: Message):
    txt = f"Baqlajon 1 kg\n" \
          f" Narxi = 17000 so'm:\n"
    await message.answer_photo(open("image/Baqlajon.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="Piyoz")
async def sabza(message: Message):
    txt = f"Piyoz 1 kg\n" \
          f" Narxi = 4000 so'm:\n"
    await message.answer_photo(open("image/piyoz.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="sut")
async def sut(message: Message):
    txt = f"Sut 1 Litr\n" \
          f" Narxi = 17000 so'm:\n"
    await message.answer_photo(open("image/sut.jpeg", "rb"), txt, reply_markup=menuzakaz)


@dp.message_handler(text="tuxum")
async def sut(message: Message):
    txt = f"Tuxum 1 dona\n" \
          f" Narxi = 2000 so'm:\n"
    await message.answer_photo(open("image/tuxum.jpeg", "rb"), txt, reply_markup=menuzakaz)

@dp.callback_query_handler(text="🚚Buyurtma")
async def buyurtma(call: CallbackQuery):
    txt = f"Buyurtmanigiz qabul qilindi\n" \
          f"Iltimos bizga locatin yoki contactingizni yuuboring\n"
    await call.message.answer(txt, reply_markup=menuzakaz1)
    await call.аnswer(cache_time=60)

@dp.callback_query_handler(text="⬅️Orqaga")
async def orqa(call: CallbackQuery):
    txt = f"GO BACK\n"
    await call.message.answer(txt, reply_markup=start_btn)
    await call.аnswer(cache_time=60)

@dp.message_handler(text="Orqaga")
async def orqaga(message: Message):
    await message.answer("Bosh bo'lim", reply_markup=start_btn)


if __name__ == '__main__':
    executor.start_polling(dp)
