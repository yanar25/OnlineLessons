from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True)

info = KeyboardButton('info')
stats = KeyboardButton('stats')
raz = KeyboardButton('разработчик')
start.add(stats, info, raz)

stats = InlineKeyboardMarkup()
stats.add(InlineKeyboardButton('yes', callback_data='join'))
stats.add(InlineKeyboardButton('no', callback_data='cancle'))

inf = InlineKeyboardMarkup()
inf.add(InlineKeyboardButton('about bot', callback_data='bot'))
inf.add(InlineKeyboardButton('about python', callback_data='py'))

rsp = types.ReplyKeyboardMarkup(resize_keyboard=True)

rock = types.KeyboardButton('rock')
scissors = types.KeyboardButton('scissors')
paper = types.KeyboardButton('paper')
rsp.add(rock, scissors, paper)
