from pyrogram import Client, filters
from config import SUDO_USERS
from pyrogram.types import *
from pyrogram.types import get_chat_history
import asyncio
from pyrogram import *



@Client.on_message(filters.command(["spamban", "spaminfo"], ["."]) & filters.me)
async def spamban(client: Client, message: Message):
    zaid = await message.reply_text("Checking your account for Spamban...")
    await client.unblock_user("spambot")
    await client.send_message("spambot", "/start")
    async for iii in client.get_chat_history("spambot", limit=1):
        await zaid.edit(iii.text)
