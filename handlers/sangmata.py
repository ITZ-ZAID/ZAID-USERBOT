	
import asyncio
from pyrogram import filters

from helpers.basic import edit_or_reply
from pyrogram.errors import RPCError
from pyrogram import * 
from pyrogram.types import *
from handlers.help import *
 
@Client.on_message(filters.command(['sg', "sangmata"], ["."]) & filters.me)
async def sg(client: Client, message: Message):
    lol = await edit_or_reply(message, "Processing please wait")
    if not message.reply_to_message:
        await lol.edit("reply to any message")
    reply = message.reply_to_message
    if not reply.text:
        await lol.edit("reply to any text message")
    chat = message.chat.id
    try:
        await client.send_message("@SangMataInfo_bot","/start")
    except RPCError:
        await lol.edit("Please unblock @SangMataInfo_bot and try again")
        return
    await reply.forward("@SangMataInfo_bot")
    await asyncio.sleep(2)
    async for opt in client.iter_history("@SangMataInfo_bot", limit=3):
        hmm = opt.text
        if hmm.startswith("Forward"):
            await lol.edit("Can you kindly disable your privacy settings for good")
            return
        else:
            await lol.delete()
            await opt.copy(chat)


add_command_help(
    "sangmata",
    [
        [".sg", "Reply to a user to find name history."],
    ],
)
