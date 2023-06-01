import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from bot.config import BOT_TOKEN


logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="22:00", compression="zip")

loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, loop=loop, storage=storage)

async def shutdown(dp):
    await storage.close()
    await bot.close()


if __name__=="__main__":
    from bot.heandler import dp
    executor.start_polling(dp, on_shutdown=shutdown, skip_updates=True)
