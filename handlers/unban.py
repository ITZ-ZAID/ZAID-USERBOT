from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message


@Client.on_message(filters.group & filters.command("unban", ["."]) & filters.me)  
async def member_unban(client: Client, message: Message):
    msg_id=message.message_id
    chat_msg=message.text
    username=None
     
    if "@" in chat_msg:
        index=chat_msg.index("@")     
        chat_msg=str(chat_msg)
        username=chat_msg[index+1:len(chat_msg)]
    else:                   
        username=message.reply_to_message.from_user.id

    chat_id=message.chat.id
    me_m =await client.get_me()
    me_ = await message.chat.get_member(int(me_m.id))
    user_info=await client.get_users(username)
    if me_.can_restrict_members:      
        await client.unban_chat_member(chat_id , username)
        if(user_info.username):
            usercontact=user_info.username
            reply_string="@"+usercontact+" has been picked up from hell 😈"
            await client.edit_message_text(chat_id , msg_id , reply_string)
        else:
            usercontact=user_info.first_name
            reply_string=usercontact+" has been picked up from 😈"
            await client.edit_message_text(chat_id , msg_id , reply_string)
    else:
        reply_string="Noob,you can't unban members 😂 !"
        await client.edit_message_text(chat_id , msg_id , reply_string )
