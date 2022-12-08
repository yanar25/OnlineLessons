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

# Розничный магазин. 20 продавцов. Для быстрого управления персоналом, необходимо сделать кнопки с отделом,
# куда необходимо подойти. Пример:Я вижу, что нужен человек в овощном отделе, нажимаю на кнопку,
# и все сотрудники видят это. И могут принять или отказаться. Кто принимает, пишется сообщение,
# Петя Иванов направляется к овощам.
