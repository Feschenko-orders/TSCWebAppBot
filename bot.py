import asyncio
import logging
import sys
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram import types
from config import Config


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    reply_markup: types.ReplyKeyboardMarkup = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                    text="🚀 View as MiniApp",
                    web_app=types.WebAppInfo(url=Config.BOT.BASE_URL),
                )
            ]
        ],
    )

    await message.answer(
        f"Hello, <b>{message.from_user.full_name}</b>!", reply_markup=reply_markup
    )


async def main() -> None:
    bot = Bot(
        token=Config.BOT.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
