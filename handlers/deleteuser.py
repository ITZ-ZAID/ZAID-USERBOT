from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from handlers.help import *

@Client.on_message(filters.group & filters.command(["deleteuserhistory", "deletehistory"], ["."]) & filters.me)  
async def delete_user_history(client: Client, message: Message):
    chat_id=message.chat.id
    msg_id=message.message_id
    chat_msg=message.text
    username=None

    if "@" in chat_msg:
        index=chat_msg.index("@")     
        chat_msg=str(chat_msg)
        username=chat_msg[index+1:len(chat_msg)]
    else:                   
        username=message.reply_to_message.from_user.id
    zuzu= await client.get_chat_member(chat_id , "me")
    can_delete=zuzu.can_delete_messages
    if(can_delete):      
        await client.delete_user_history(chat_id , username)
    else:
        reply_string="Noob,you can't delete their existence !"
        await client.edit_message_text(chat_id , msg_id , reply_string )


add_command_help(
    "deletehistory",
    [
        [".deletehistory", "To find history"],
    ],
)
