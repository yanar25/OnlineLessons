import random

from aiogram import Bot, types, executor, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

import config
import keyboard

import logging

storage = MemoryStorage()
bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(
    # указываем название с логами
    filename='log.txt',
    # указываем уровень логирования
    level=logging.INFO,
    # указываем формат сохранения логов
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s')


@dp.message_handler(Command('start'))
async def start(message):
    await bot.send_message(message.chat.id, reply_markup=keyboard.start, text='hello', parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def show(message):
    if message.text == 'покажи пользователя':
        await bot.send_message(message.chat.id, text='вы уверены?', reply_markup=keyboard.user_id,
                               parse_mode='Markdown')
    elif message.text == 'фото':
        photo = open('D:\лох\реф\kotzra.png', 'rb')
        await bot.send_photo(message.chat.id, photo)


@dp.callback_query_handler(text_contains='notgetid')
async def nasad(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='вы отменили выбор')


@dp.callback_query_handler(text_contains='getid')
async def getid(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f'ваш id: {call.from_user.id}')


if __name__ == '__main__':
    print('bot is working')
executor.start_polling(dp)

# await bot.send_message(message.chat.id, 'dfdfdf', message.from_user.id)
