import asyncio
from pyrogram import Client, filters
from handlers.restarter import restart
from pyrogram.types import *

@Client.on_message(filters.command("online", ["."]) & filters.me)
async def online_now(client: Client, message: Message):
    await message.edit("AutoOnline activated")
    while True:
        iii = await client.send_message("me", "bruh")
        await client.delete_messages("me", iii.id)
        await asyncio.sleep(45)


@Client.on_message(filters.command("offline", ["."]) & filters.me)
async def offline_now(client: Client, message: Message):
    await message.edit("AutoOnline deactivated\nRestart...")
    await restart(message, restart_type="restart")


