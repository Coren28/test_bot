from aiogram import types
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove
from aiogram import executor
from logging import basicConfig, INFO
from filters import IsAdmin
from data.config import ADMINS
from handlers.user.menu import usermode
from loader import dp, db, bot

import handlers

catalog = '🛍️ Каталог'
cart = '🛒 Корзина'
delivery_status = '🚚 Статус заказа'

@dp.message_handler(IsAdmin(), text=usermode)
async def process_catalog(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    markup.add(cart)
    markup.add(delivery_status)
    await message.answer('Включен пользовательский режим.(для возвращения в меню админа воспользуйтесь командой /menu)',
                         reply_markup=markup)


async def on_startup(dp):
    basicConfig(level=INFO)
    db.create_tables()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)