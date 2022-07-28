# @LEGEND_MUKUND

from pyrogram import Client
from main import SUDO_USERS, LOG_GROUP
from pyrogram import filters
from pyrogram.types import Message

PMPERMIT = "ENABLE"
PMSET = True
OPUSERS = [5068723844, 2006619406]

@Client.on_message(filters.incoming & filters.private)
async def pmlogger(client: Client, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            user = message.chat.id
            if user in OPUSERS:
                return
            await message.forward(
              chat_id = LOG_GROUP
            )
            return
