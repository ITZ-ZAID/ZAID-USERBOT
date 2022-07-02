from pyrogram import filters, Client
import asyncio
from handlers.help import *
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


add_command_help(
    "antipm",
    [
        [".pmguard [on or off]", " -> Activates or deactivates anti-pm."],
        [".setpmmsg [message or default]", " -> Sets a custom anti-pm message."],
        [".setblockmsg [message or default]", "-> Sets custom block message."],
        [".setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [".allow", " -> Allows a user to PM you."],
        [".deny", " -> Denies a user to PM you."],
    ],
)

