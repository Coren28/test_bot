from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove
from aiogram import executor
from logging import basicConfig, INFO

from data.config import ADMINS
from loader import dp, db, bot

import handlers

async def user_mode(message: types.Message):
    await message.answer('Включен пользовательский режим.',
                         reply_markup=ReplyKeyboardRemove())

async def on_startup(dp):
    basicConfig(level=INFO)
    db.create_tables()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)