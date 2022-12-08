import logging
import asyncio
from aiogram import Bot, types
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
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%levelname-8s [%(asctime)s] %(message)s',
                    level=logging.INFO)


@dp.message_handler(Command="start", state=None)
async def welcome(message):
    joinedFie = open('user.txt', 'r')
    joinedUsers = set()
    for line in joinedUsers:
        joinedUsers.add(line.strip())
    if not str(message.chat.id) in joinedUsers:
        joinedFie = open('user.txt', 'a')
        joinedFie.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)
    await bot.send_message(message.chat.id, f'hello, {message.from_user.first_name}, bot ok',
                           reply_markup=keyboard.start, parse_mode='Mackdown')


if __name__ == '__main__':
    print('bot is working')
executor.start_polling(dp)
