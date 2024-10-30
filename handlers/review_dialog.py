from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class RestourantReview(StatesGroup):
    name=State()
    instagram_username=State()
    visit_date=State()
    food_rating=State()
    cleanliness_rating=State()
    extra_comments=State()

review_router=Router()

@review_router.callback_query(F.data=='feedback')
async def start_review(call:types.CallbackQuery,state:FSMContext):
    await state.set_state(RestourantReview.name)
    await call.message.answer("ur name: ")

@review_router.message(RestourantReview.name)
async def process_name(message:types.Message,state:FSMContext):
    await message.answer("ur inst name: ")
    await state.set_state(RestourantReview.instagram_username)


@review_router.message(RestourantReview.instagram_username)
async def process_instagram(message: types.Message, state: FSMContext):
    await message.answer("ur visit date: ")
    await state.set_state(RestourantReview.visit_date)


@review_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='bad')],
            [types.KeyboardButton(text='good')],
        ]
    )
    await message.answer("ur food rating: ", reply_markup=kb)


@review_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.cleanliness_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='bad')],
            [types.KeyboardButton(text='good')],
        ]
    )
    await message.answer("ur cleanliness rating: ", reply_markup=kb)
@review_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.extra_comments)
    kb = types.ReplyKeyboardRemove()
    await message.answer('do u have any comments: ', reply_markup=kb)
@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await message.answer("ur review has been accepted")
    await state.clear()