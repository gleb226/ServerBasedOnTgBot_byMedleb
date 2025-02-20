import asyncio
import time
from collections import defaultdict

from aiogram import Bot, Dispatcher, BaseMiddleware
from aiogram.dispatcher.event.bases import CancelHandler

from databases.user_database import user_database
from handlers.user_handlers import user_router
from common.token import TOKEN
from tabulate import tabulate

bot = Bot(token=TOKEN)
dp = Dispatcher()
db = user_database()

dp.include_router(user_router)

user_messages = defaultdict(list)
spam_users = {}


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, rate_limit=2.0):
        super().__init__()
        self.rate_limit = rate_limit
        self.user_timers = {}

    async def on_process_message(self, message, data):
        user_id = message.from_user.id
        if user_id in self.user_timers:
            raise CancelHandler()
        self.user_timers[user_id] = True
        await asyncio.sleep(self.rate_limit)
        del self.user_timers[user_id]


async def limit_messages(message):
    user_id = message.from_user.id
    current_time = time.time()

    if user_id in spam_users and current_time < spam_users[user_id]:
        await message.answer("You are temporarily blocked for spamming.")
        return

    user_messages[user_id] = [t for t in user_messages[user_id] if current_time - t < 60]

    if len(user_messages[user_id]) >= 80:
        spam_users[user_id] = current_time + 900
        await message.answer("Too many messages! You are blocked for 5 minutes.")
        return

    user_messages[user_id].append(current_time)
    await message.answer("Message saved.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
