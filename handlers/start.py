from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command('start'))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us"),
            ],
            [
                types.InlineKeyboardButton(text='отзывы', callback_data="review"),
            ],
            [
                types.InlineKeyboardButton(text='jobs', callback_data="jobs"),
            ],
            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data="feedback"),
            ]
        ]
    )
    await message.answer('hello', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def about_us(call: types.CallbackQuery):
        await call.answer('nothing yet')


@start_router.callback_query(F.data == 'review')
async def review(call: types.CallbackQuery):
        await call.answer('nothing yet')


@start_router.callback_query(F.data == 'jobs')
async def jobs(call: types.CallbackQuery):
        await call.answer('nothing yet')