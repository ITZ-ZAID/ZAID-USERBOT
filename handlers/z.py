from pyrogram import filters

from typing import Tuple
from handlers.help import *
import random
from handlers.cache.data import *
from config import SUDO_USERS
from pyrogram import filters, Client
from helpers.mongo.rraid import *
from helpers.pyrohelper import get_arg
from helpers.adminhelpers import CheckAdmin

@Client.on_message(filters.group & filters.private & filters.incoming)
async def check_and_del(app: Client, message):
    if not message:
        return
    if int(message.chat.id) in GROUP:
        return
    try:
        if not message.from_user.id in (await get_rraid_users()):
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await message.reply_text(f"{random.choice(RAID)}")
    except:
        pass
