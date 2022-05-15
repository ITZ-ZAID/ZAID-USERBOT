from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message


mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)

@Client.on_message(filters.command("mute", ["."]) & filters.me)  
async def mute(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        me_m =await client.get_me()
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_restrict_members:
         await message.edit("`You Don't Have Permission! To mute`")
         return
        can_mute= True
        if can_mute:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                else:
                    usr = await client.get_users(message.command[1])
                    user_id = usr.id
            except IndexError:
                await message.edit_text("some ooga booga")
                return
            try:
                await client.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=user_id,
                    permissions=mute_permission,
                )
                await message.delete()
            except Exception as e:
                await message.edit_text("`Error!`\n" f"**Log:** `{e}`")
                return
        else:
            await message.edit_text("denied_permission")
    else:
        await message.delete()
