import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import config


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message()
async def any(message: types.Message):
    if type(message.text) != str:
        await message.answer(text=message.text)
    else:
        await message.send_copy(chat_id=message.chat.id)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
