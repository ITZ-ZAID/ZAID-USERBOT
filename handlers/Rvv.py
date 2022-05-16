from pyrogram import filters
from traceback import format_exc
from typing import Tuple
import random
from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message)
from helpers.SQL.rraid import zaidub_info, rzaid, runzaid
from handlers.cache.data import RAID
from main import SUDO_USERS

@Client.on_message(filters.text & filters.private & ~filters.group)
async def jaana(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user = message.from_user.id
    zaid = random.choice(RAID)
    if await zaidub_info(user):
        if message.chat.type != "supergroup":
            pass
        try:
            me_ = await message.chat.get_member(int(client.me.id))
        except:
            pass
        await message.reply_text(zaid)
