import asyncio

import aioschedule
from aiogram import executor

from src.loader import bot, dp
from logger.logger import logger
from src import handlers


# async def test():
#     print("hello")


# async def scheduler_run():
#     aioschedule.every(1).hours.do(test)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)


async def on_startup(_):
    logger.success("Start Bot")
    # asyncio.create_task(scheduler_run())
    await bot.delete_webhook()


async def on_shutdown(dp):
    logger.info("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logger.info("Bot down")


if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True
    )
