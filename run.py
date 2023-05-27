import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging


from bot.config import BOT_TOKEN

logging.basicConfig(level=logging.INFO)

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
