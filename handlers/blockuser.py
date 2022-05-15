from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message


@Client.on_message(filters.command("block", ["."]) & filters.me)  
async def block_user(client: Client, message: Message):
    if not message.chat.type == "private":
        await message.reply("Can't block the group LOL !")
    else:
        user_id=message.chat.id
        await message.edit("You have been blocked succesfully due to your sins !!")
        await client.block_user(int(user_id))
