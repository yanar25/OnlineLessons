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

import time

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


# logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%levelname-8s [%(asctime)s] %(message)s',
#                     level=logging.INFO)


# logging.basicConfig(filename='log.txt', level=logging.INFO)
# format=u'%(filename)s [LINE:%(lineno)d] #%levelname-8s [%(asctime)s] %(message)s'

# @dp.message_handler(commands=['start'])
# async def welcome(message: types.Message):
#     sti = open('D:\лох\реф\sticker.webp', 'rb')
#     await message.reply(f'hello, {message.from_user.first_name}, bot ok', reply_markup=keyboard.start,
#                         reply=keyboard.info)
#     await bot.send_sticker(message.chat.id, sti)
@dp.message_handler(Command('start'), state=None)  # start i privetstvie
async def welcome(message):
    joinedFile = open('user.txt', 'r')
    joinedUsers = set()
    for line in joinedFile:
        joinedUsers.add(line.strip())
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open('user.txt', 'a')
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)
    sti = open('D:\лох\реф\sticker.webp', 'rb')
    await message.reply(f'hello, *{message.from_user.first_name}*, bot ok', reply_markup=keyboard.start,
                        reply=keyboard.info, parse_mode='Markdown')
    await bot.send_sticker(message.chat.id, sti)


@dp.message_handler(Command('game'))  # камень ножницы бумага. НЕ ЗАКОНЧЕНО
async def rsp(message):
    await bot.send_message(message.chat.id, 'dfdfd')
    await bot.send_message(message.chat.id, 'dfdf', reply_markup=keyboard.rsp)
    if message == 'rock':
        message = 1
    elif message == 'scissor':
        message = 2
    elif message == 'paper':
        message = 3
    if message == 'rock':
        await bot.send_message(message.chat.id, 'dfd')
    x = random.randint(1, 3)
    if message == x:
        await message.chat.id('noone')
    elif message == 1:
        if x == 2:
            await bot.send_message(message.chat.id, text='u win!')
        else:
            message.chat.id('im win!')


@dp.message_handler(content_types=['text'])
async def inf(message):
    if message.text == 'разработчик':
        await bot.send_message(message.from_user.id, 'разработчик: yana rudzenko\nhttps://t.me/yanarudzenko')


@dp.message_handler(content_types=['text'])  # knopki start i info
async def get_message(message):
    if message.text == 'info':
        await bot.send_message(message.chat.id, text='hm..', reply_markup=keyboard.inf)
        # await bot.send_message(message.chat.id, text='info\nits learning bot', parse_mode='Markdown')
    elif message.text == 'stats':
        sti = open('D:\лох\реф\sticker.webp3.webp', 'rb')
        await bot.send_message(message.chat.id, text='im too cool for that.')
        await bot.send_sticker(message.chat.id, sti)

        await bot.send_message(message.chat.id, text='well... ok\n are you an admin?', reply_markup=keyboard.stats)


@dp.message_handler(commands=['dustred'])
async def dustred(message: types.message):
    sti2 = open('D:\лох\реф\sticker.webp2.webp', 'rb')
    await message.reply(f'dustred canon')
    await bot.send_sticker(message.chat.id, sti2)


@dp.callback_query_handler(text_contains='join')
async def join(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:
        d = sum(1 for line in open('user.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'bot stats: *{d}* people', parse_mode='Markdown')
    else:
        # s1 = open('D:\лох\реф\sticker.webp4.webp')
        # s2 = open('D:\лох\реф\sticker.webp5.webp')
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f'you are not the admin. go away')


@dp.callback_query_handler(text_contains='bot')
async def inf(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text='it is bot.')


@dp.callback_query_handler(text_contains='py')
async def py(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.message.chat.id, text='''info:
    1. https://habr.com/ru/post/421993/
    2. https://habr.com/ru/post/422311/''')


# @dp.callback_query_handler(text_contains='join')
# async def join(call: types.CallbackQuery):
#     if call.message.chat.id == config.admin:
#         d = sum(1 for line in open('user.txt'))
#         await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                     text=f'bot stats: *{d}* people', parse_mode='Markdown')
#     else:
#         # s1 = open('D:\лох\реф\sticker.webp4.webp')
#         # s2 = open('D:\лох\реф\sticker.webp5.webp')
#         await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                     text=f'you are not the admin. go away')

#
# @dp.message_handler(commands=['rassilka'])
# async def rassylka(message):
#     if message.chat.id == config.admin:
#         await bot.send_message(message.chat.id, f'*rassilka was started*', parse_mode='Markdown')
#     rec_users, block_users = 0, 0
#     joinned_file = open('user.txt', 'r')
#     joined_users = set()
#     for line in joinned_file:
#         joined_users.add(line.strip())
#         joinned_file.close()
#     for user in joined_users:
#         try:
#             await bot.send_photo(user, 'D:\\лох\\реф\\tyrty.png.jpg', 'rb'), message.text[message.text.find(' '):])
#             rec += 1
# joinedFile = open('user.txt', 'r')
# joinedUsers = set()
# for line in joinedFile:
#     joinedUsers.add(line.strip())
#
# if not str(message.chat.id) in joinedUsers:
#     joinedFile = open('user.txt', 'a')
#     joinedFile.write(str(message.chat.id) + '\n')
#     joinedUsers.add(message.chat.id)


#
# @dp.callback_query_handler(func=lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
#
#
# @dp.message_handler(commands=['links'])
# async def links(message: types.message):
#     botton1 = InlineKeyboardButton('литература', callback_data='button1')
#     kb = InlineKeyboardMarkup().add(botton1)
#     await message.reply("возможно будет полезно", reply_markup=kb)


if __name__ == '__main__':
    print('bot is working')
executor.start_polling(dp)
