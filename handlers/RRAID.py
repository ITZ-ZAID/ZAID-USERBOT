""" 
Dear Kangers Don't Kang This Code.
This Code Maded By Meh First On Telegram
I have Spent My Lots of Time on That to make
It successfull.
So Uh Are Still Thinking To kang?
Don't kang Without Creadits
© https://github.com/ITZ-ZAID/ZAID-USERBOT and @Timesisnotwaiting
"""


from pyrogram import filters

from typing import Tuple
from handlers.help import *
import random
from handlers.cache.data import *
from main import SUDO_USERS
from pyrogram import filters, Client
from helpers.mongo.rraid import *
from helpers.pyrohelper import get_arg
from helpers.adminhelpers import CheckAdmin

@Client.on_message(filters.command("gban", ["."]) & filters.me)
async def gban(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I gban?**")
            return
    get_user = await app.get_users(user)
    mee= await app.get_me()
    if get_user.id == mee.id:
        await Zaid.edit("`Jaa Na Lawde Kahe Dimag Kha rha? Khudpe Raid kyu laga rha?`")
        return
    if await zaidub_info(get_user.id):
        await Zaid.edit("`Who So Noob? Reply Raid Already Activated on that User:/`")
        return
    if int(get_user.id) in VERIFIED_USERS:
        await Zaid.edit("Chal Chal baap Ko mat sikha")
        return
    elif int(get_user.id) in SUDO_USERS:
        await Zaid.edit("Abe Lawde that guy part of my devs.")
        return
    await rraid_user(get_user.id)
    await message.edit(f"**Successfully Gbanned {get_user.first_name}!**")


@Client.on_message(filters.command("ungban", ["."]) & filters.me)
async def gbam(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I ungban?**")
            return
    get_user = await app.get_users(user)
    await unrraid_user(get_user.id)
    await message.edit(f"**Ungbanned {get_user.first_name}, enjoy!**")


@Client.on_message(filters.group & filters.incoming)
async def check_and_del(app: Client, message):
    if not message:
        return
    try:
        if not message.from_user.id in (await get_rraid_users()):
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await message.reply_text("{random.choice(RAID)}")
    except:
        pass

add_command_help(
    "replyraid",
    [
        [".replyraid", "Reply To User\n To Raid on Someone."],
        [".dreplyraid", "To Disable ReplyRaid."],
    ],
)
