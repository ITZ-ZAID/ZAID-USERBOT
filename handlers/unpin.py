from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from handlers.help import add_command_help



@Client.on_message(filters.command("unpin", ["."]) & filters.me)  
async def unpin_message(client: Client, message: Message):
    msg_id=message.message_id
    chat_id=message.chat.id
    if message.reply_to_message == None:
        await client.edit_message_text(chat_id , msg_id , "Shall I unpin your head from wall ?")
    else:
        if message.chat.type == "private":
            reply_msg_id=message.reply_to_message.message_id
            await client.unpin_chat_message(chat_id , reply_msg_id )
            await client.edit_message_text(chat_id , msg_id , "Done the Job master !")
        else:
            zuzu=await RaiChUB.get_chat_member(chat_id , "me")
            can_pin=zuzu.can_pin_messages
            if can_pin == None:
                await client.edit_message_text(chat_id , msg_id , "Can't pin messages bruh 🥱") 
            else:         
                reply_msg_id=message.reply_to_message.message_id
                await client.unpin_chat_message(chat_id , reply_msg_id)
                await client.edit_message_text(chat_id , msg_id , "Done the Job master !")

add_command_help(
    "admin",
    [
        [".ban | .unban", "Reply to a user to perform ban/unban."],
        [".promote | .demote", "Reply to a user to promote/demote."],
        [
            ".mute | .unmute",
            "Reply to a user to mute/Unmute them forever",
        ],
        [
            ".pin | .unpin",
            "Reply to a message to pin /Unpin",
        ],
        [
            ".setgpic",
            "Reply to a Image to set Your Group Pic",
        ],
    ],
)
