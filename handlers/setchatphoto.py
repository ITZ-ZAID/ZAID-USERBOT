from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from handlers.help import *


@Client.on_message(filters.group & filters.command(["setchatphoto", "setgpic"], ["."]) & filters.me)  
async def set_chat_photo(client: Client, message: Message):
    msg_id=message.message_id
    chat_id=message.chat.id
    zuzu=await client.get_chat_member(chat_id , "me")
    can_change_admin=zuzu.can_change_info
    can_change_member=message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("You don't have enough permission")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(chat_id , photo=message.reply_to_message.photo.file_id)
            return
    else:
        await message.edit_text("Reply to a photo to set it !")


add_command_help(
    "setchatphoto",
    [
        [".setchatphoto", "Reply to a image To set Your Group Chat Pic."],
    ],
)
