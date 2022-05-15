from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import Message



@Client.on_message(filters.command("invitelink", ["."]) & filters.me)
async def invite_link(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        chat_name = message.chat.title
        try:
                link = await client.export_chat_invite_link(message.chat.id)
                await message.reply_text(f"The invite link for chat is {link}")
        except Exception as e:
                print(e)
                await message.reply_text("denied permission")
