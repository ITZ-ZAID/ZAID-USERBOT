from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from handlers.help import *

@Client.on_message(filters.command("purge", ["."]) & filters.me)  
async def purge(client: Client, message: Message):
    start_time = time.time()
    message_ids = []
    purge_len = 0
    event = await message.edit_text("`Starting To Purge Messages!`")
    me_m =await client.get_me()
    if message.chat.type in ["supergroup", "channel"]:
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_delete_messages:
            await event.edit("`I Need Delete Permission To Do This!`")
            return
    if not message.reply_to_message:
        await event.edit("`Reply To Message To Purge!`")
        return
    async for msg in client.iter_history(
        chat_id=message.chat.id,
        offset_id=message.reply_to_message.message_id,
        reverse=True,
    ):
        if msg.message_id != message.message_id:
            purge_len += 1
            message_ids.append(msg.message_id)
            if len(message_ids) >= 100:
                await client.delete_messages(
                    chat_id=message.chat.id, message_ids=message_ids, revoke=True
                )
                message_ids.clear()
    if message_ids:
        await client.delete_messages(
            chat_id=message.chat.id, message_ids=message_ids, revoke=True
        )
    end_time = time.time()
    u_time = round(end_time - start_time)
    await event.edit(
        f"**>> Fast Purge Done!** \n**>> Total Message Purged :** `{purge_len}` \n**>> Time Taken :** `{u_time}`",
    )
    await asyncio.sleep(3)
    await event.delete()



add_command_help(
    "purge",
    [
        [".purge", "Reply To Message."],
    ],
)
