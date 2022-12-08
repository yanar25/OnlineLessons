from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = types.ReplyKeyboardMarkup()
us_id = types.KeyboardButton('покажи пользователя')
start.add(us_id)
user_id = types.InlineKeyboardMarkup()
user_id.add(InlineKeyboardButton('мой id', callback_data='getid'))
user_id.add(types.InlineKeyboardButton('вернуться обратно', callback_data='notgetid'))

photo = types.KeyboardButton('фото')
start.add(photo)

# photo_new = types.InlineKeyboardMarkup('заменить фото?')
# photo_new.add(types.InlineKeyboardButton('нет', callback_data='no'))
# photo_new.add(types.InlineKeyboardButton('да', callback_data='yes'))
