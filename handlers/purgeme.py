from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from handlers.help import *

@Client.on_message(filters.command("purgeme", ["."]) & filters.me)  
async def purgeme(client: Client, message: Message):
    msg_text=message.text
    chat_id=message.chat.id
    if " " in msg_text:
        number=msg_text[msg_text.index(" ")+1 : len(msg_text)]
        if(not number.isnumeric()):
            await message.edit_text("Need a number to delete !")
        else:
            number=int(number)
            msg_id=message.message_id - 1
            while number > 0:
                try:
                    print(msg_id)
                    if client.get_messages(chat_id , msg_id).from_user.id == client.get_users("me").id:
                        await client.delete_messages(chat_id , msg_id)
                        print("Zaid")
                        number=number-1
                    msg_id=msg_id-1
                except Exception as e:
                    msg_id=msg_id-1
    else:
        await message.edit_text("Give me a number to delete !!")


add_command_help(
    "purgeme",
    [
        [".purgeme", "To Delete Your messages."],
    ],
)
