# Own

from pyrogram.types import Message
import asyncio
import asyncio
from pyrogram import filters, Client
from handlers.help import *
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from handlers.cache.data import *
from config import SUDO_USERS


usage = f"** ❌ Wrong Usage ❌** \n Type `.help delayspam`"


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["fspam", "fastspam"], [".", "!"]))
@Client.on_message(filters.me & filters.command(["fspam", "fastspam"], ["."]))
async def spam(xspam: Client, e: Message):
    warn = await e.reply_text("**Note:** Don't Blame to @ZaidUserBot If IDs Get ban -!")
    await asyncio.sleep(3)
    await warn.delete()
    Zaid = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    if len(Zaid) == 2:
       counts = int(Zaid[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Zaid[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply("**Sorry !!**")
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await xspam.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(0.002)
          return
       for _ in range(counts):
           await xspam.send_message(e.chat.id, msg)
           await asyncio.sleep(0.002)
    else:
        await xspam.reply(usage)



add_command_help(
    "delayspam",
    [
        [".delayspam", "Spam Slowly (Sudo User also)."],
    ],
)
