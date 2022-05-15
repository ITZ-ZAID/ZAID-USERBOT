from pyrogram import Client, filters
from config import SUDO_USERS
from pyrogram.types import *
import asyncio




@Client.on_message(filters.command(["spamban", "spaminfo"], ["."]) & filters.me)
async def spamban(client, message):
    zaid = await message.reply_text("Checking your account for Spamban...")
    await client.unblock_user("spambot")
    await client.send_message("spambot", "/start")
    async for iii in client.get_chat_history("spambot", limit=1):
        await zaid.edit(iii.text)
