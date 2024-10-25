from os import getenv

from aiogram import  Bot,Dispatcher,types
from aiogram.filters import Command
import asyncio
from dotenv import load_dotenv
import random
load_dotenv()

token=getenv('TOKEN')
bot = Bot(token=token)
dp=Dispatcher()

recipes=[['plov',['et','ris']],
         ['behbarmak',['et','kamyr']],
         ['samsa',['et','kamyr']]],



@dp.message(Command('start'))
async def start(message: types.Message):
        await message.answer(f'Hello {message.from_user.first_name}')

@dp.message(Command('my_info'))
async def my_info(message: types.Message):
    await message.answer(f'name: {message.from_user.first_name}\n'
                         f'id: {message.from_user.id}\n')


@dp.message(Command('random_recipe'))
async def random_recips(message: types.Message):
    random_recipe=random.choice(recipes)
    await message.answer(f'{random_recipe[0]}\n'
                         f'{random_recipe[1]}\n')
async def main():
    await dp.start_polling(bot)

if  __name__ == '__main__':
    asyncio.run(main())

