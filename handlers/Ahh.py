 
from pyrogram import *
from pyrogram.types import *
from helpers.basic import edit_or_reply
 
import asyncio
from handlers.help import *
 
 

@Client.on_message(filters.me & (filters.command(["ahh"], ["."]) | filters.regex("^ahh "))) 
async def hello_world(client: Client, message: Message):
    mg = await edit_or_reply(message, "ahh")
    await asyncio.sleep(0.2)
    await mg.edit("aahh")
    await asyncio.sleep(0.2)
    await mg.edit("aahhh")
    await asyncio.sleep(0.2) 
    await mg.edit("aahhhh")
    await asyncio.sleep(0.2) 
    await mg.edit("aahhhhh")
    await asyncio.sleep(0.2) 
    await mg.edit("aahhhhhh") 
    await asyncio.sleep(0.2) 
    await mg.edit("aahhhhhhh") 
    await asyncio.sleep(0.2) 
    await mg.edit("aaahhhhhhhh")


add_command_help(
    "ahh",
    [
        [".ahh", "Random editing Reply."],
    ],
)
