import random

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Салам Алейкум {message.from_user.first_name}")


@dp.message_handler(commands=['mem'])
async def send_image(message: types.Message):
    photo = open('mem/lol.jpg', 'rb')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)
    question = 'Сколько букв в алфавите?'
    answers = [
        '29',
        '32',
        '30',
        '33',
        '20',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Ненадо дядя',
        reply_markup=markup,
        open_period=5,
    )

@dp.callback_query_handler(text="button_call_1")
async def quiz_2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_1)
    question = 'Сколько будет 20 + 5?'
    answers = [
        '4',
        '5',
        '6',
        'НЕЗНАЮ',
        '25',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation='Ненадо дядя',
        reply_markup=markup,
        open_period=5,
    )

@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await bot.send_message(chat_id=message.from_user.id, text=message.text)
    await bot.send_message(chat_id=message.from_user.id, text=int(message.text)**2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
