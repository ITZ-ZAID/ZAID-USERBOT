from pyrogram import filters, Client
from pyrogram.types import Message
import asyncio
from handlers.help import *

@Client.on_message(filters.me & filters.command("invite", ["."]))
async def inviteee(client: Client, message: Message):
    mg = await message.edit_text("`Adding Users!`")
    user_s_to_add = message.text.split(" ",1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"`Sucessfully Added {len(user_list)} To This Group / Channel!`")


add_command_help(
    "invite",
    [
        [".invite", "Usage: \n /invite @Username of User."],
    ],
)
