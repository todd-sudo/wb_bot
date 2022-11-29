from aiogram.types import Message
from aiogram.dispatcher.filters import BoundFilter

import config
from src.loader import bot


class IsAdmin(BoundFilter):

    async def check(self, message: Message):
        member = await bot.get_chat_member(config.CHAT_ID, message.from_user.id)
        if member.status == "left":
            return False
        return True
