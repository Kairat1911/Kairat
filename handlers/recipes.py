from config import bot,dp
from aiogram import types,Router,F
from aiogram.filters import Command
import random

recipe_router=Router()

recipes=[['manty',['et','kamyr']],
         ['plov',['et','morkovka']],
         ['kuurdak',['et','kartoshka']]]

@recipe_router.message(Command('random_recipe'))
async def random_recipe(message: types.Message):
    random_recipee=random.choice(recipes)
    await message.answer(f'{random_recipee[0]}\n'
                         f'{random_recipee[1]}\n')