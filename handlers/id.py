from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from handlers.help import *


@Client.on_message(filters.me & filters.command("id", ["."]))
async def id(client: Client, message: Message):
    if message.reply_to_message is None:
        await message.reply(f"This chat's ID is: {message.chat.id}")
    else:
        test = f"This user's ID is: {message.reply_to_message.from_user.id}\n\nThis chat's ID is: {message.chat.id}"
        await message.edit_text(test)


add_command_help(
    "id",
    [
        [".id", "To Get User Id."],
    ],
)
