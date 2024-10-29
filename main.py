from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from config import bot,dp
import asyncio
from os import getenv
from dotenv import load_dotenv
import random
load_dotenv()
from handlers.recipes import recipe_router
from handlers.start import start_router
from handlers.my_info import my_info_router
from handlers.dishes import dishes_router

token=getenv('TOKEN')
bot = Bot(token=token)
dp=Dispatcher()

recipes=[['manty',['et','kamyr']],
         ['plov',['et','morkovka']],
         ['kuurdak',['et','kartoshka']]]

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(f'hello {message.from_user.first_name}')
@dp.message(Command('my_info'))
async def my_info(message: types.Message):
    await message.answer(f'name: {message.from_user.first_name}\n'
                         f'id : {message.from_user.id}')
@dp.message(Command('random_recipe'))
async def random_recipe(message: types.Message):
    random_recipee=random.choice(recipes)
    await message.answer(f'{random_recipee[0]}\n'
                         f'{random_recipee[1]}\n')


async def main():
    dp.include_router(start_router)
    dp.include_router(recipe_router)
    dp.include_router(my_info_router)
    dp.include_router(dishes_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())