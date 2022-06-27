from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
from handlers.help import *

@Client.on_message(filters.command("join", ".") & filters.me)
async def join(client: Client, message: Message):
    zaid = message.text[6:]
    count = 0
    if not zaid:
        return await message.reply_text("Need a chat username or invite link to join.")
    if zaid.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(zaid)
        await message.reply_text(f"**Joined**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")

@Client.on_message(filters.command("leave", ".") & filters.me)
async def leave(client: Client, message: Message):
    zaid = message.text[6:]
    count = 0
    if not zaid:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if zaid.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(zaid)
        await message.reply_text(f"**Lefted**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


add_command_help(
    "joinleave",
    [
        [".join", "To Join a Chat Via link else Username ."],
        [".leave", "To leave a Chat Via link else Username."],
        ["/join", "To Join a Chat Via link else Username(Sudo Users)."],
        ["/leave", "To leave a Chat Via link else Username(Sudo Users)."],        
    ],
)
