import os
import shutil
import asyncio
from config import SUDO_USERS
from pyrogram.types import Message
from pyrogram import filters, Client

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["eye"], ["."]))
async def eye(client, m: Message):
    sex = await m.reply_text("👁👁\n  👄  =====> Abey Ja Na Gandu")    
    await asyncio.sleep(0.09)
    await sex.edit("👁👁\n  💋  =====> Abey Ja Na Randi") 
    await asyncio.sleep(0.09)
    await sex.edit("👁👁\n  👄  =====> Abey Ja Na Betichod") 
    await asyncio.sleep(0.09)
    await sex.edit("👁👁\n  👅  =====> Abey Ja Na Behenchod") 
    await asyncio.sleep(0.09)
    await sex.edit("👁👁\n  💋  =====> Abey Ja Na Na Mard") 
    await asyncio.sleep(0.09)
    await sex.edit("👁👁\n  👄  =====> Abey Ja Na Randi") 
    await asyncio.sleep(0.09)
    await sex.edit("👁👁\n  👅  =====> Abey Ja Na Bhosdk") 
    await asyncio.sleep(0.09)
    await sex.edit("👁👁\n  💋  =====> Abey Ja Na Chutiye") 
    await asyncio.sleep(0.09)
    await sex.edit("👁👁\n  👄  =====> Hi All, How Are You Guys...") 
    await asyncio.sleep(0.10)  
    return
