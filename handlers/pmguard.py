from pyrogram import filters, Client
import asyncio

from pyrogram.methods import messages
from helpers.pyrohelper import get_arg, denied_users
import helpers.mongo.pmpermitdb as Zaid

@Client.on_message(filters.command("pmguard", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**I only understand on or off**")
        return
    if arg == "off":
        await Zaid.set_pm(False)
        await message.edit("**PM Guard Deactivated**")
    if arg == "on":
        await Zaid.set_pm(True)
        await message.edit("**PM Guard Activated**")
