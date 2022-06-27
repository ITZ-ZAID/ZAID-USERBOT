#from Rexoma SpamBot
#©By Rizoel
import asyncio
from pyrogram import filters, Client
from handlers.help import *
from pyrogram.types import *
from pyrogram import __version__
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from handlers.cache.data import *

from config import SUDO_USERS
from main import ALIVE_PIC

Zaid = f"**꧁ 𒈞zαι∂ υѕєявσт𒈞꧂**\n\n"
Zaid += f"━───────╯•╰───────━\n"
Zaid += f"➠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.5`\n"
Zaid += f"➠ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{__version__}`\n"
Zaid += f"➠ **ᴠᴇʀsɪᴏɴ**  : `{2.0}`\n"
Zaid += f"➠ **ᴄʜᴀɴɴᴇʟ** : [❝𝐂𝐥𝐢𝐜𝐤❞](https://t.me/TheUpdatesChannel)\n"
Zaid += f"━───────╮•╭───────━\n\n"
Zaid += f"➠ **𒆜ʍǟӄɛ ʏօʊʀ օառ 𒆜:** [❝𝐂𝐥𝐢𝐜𝐤❞](https://gitHub.com/Itz-Zaid/Zaid-Userbot)"


usage = f"** ❌ Wrong Usage ❌** \n Type `.help advanced`"

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["delayspam"], [".", "!", "/"]))
@Client.on_message(filters.me & filters.command(["delayspam"], ["."]))
async def delayspam(xspam: Client, e: Message): 
    kkk = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    Zaid = kkk[1:]
    if len(Zaid) == 2:
       counts = int(Zaid[0])
       if int(e.chat.id) in GROUP:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
       msg = str(Zaid[1])
       if re.search(Owners.lower(), msg.lower()):
            return await e.reply("**Sorry !!**")
       sleeptime = float(Zaid[0])
       if e.reply_to_message:
          reply_to_id = e.reply_to_message.message_id
          for _ in range(counts):
              await xspam.send_message(e.chat.id, msg, reply_to_message_id=reply_to_id)
              await asyncio.sleep(sleeptime)
          return
       for _ in range(counts):
           await xspam.send_message(e.chat.id, msg)
           await asyncio.sleep(sleeptime)
    else:
        await e.reply_text("Usage: .delayspam time count message")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["pornspam"], [".", "!", "/"]))
@Client.on_message(filters.me & filters.command(["pornspam"], ["."]))
async def pornspam(xspam: Client, e: Message): 
    counts = e.command[0]
    if not counts:
        return await e.reply_text(usage)
    if int(e.chat.id) in GROUP:
         return await e.reply_text("**Sorry !! i Can't Spam Here.**")
    kkk = "**#Pornspam**"
    count = int(counts)
    for _ in range(count):
         prn = choice(PORM)
         if ".jpg" in prn or ".png" in prn:
              await xspam.send_photo(e.chat.id, prn, caption=kkk)
              await asyncio.sleep(0.4)
         if ".mp4" in prn or ".MP4," in prn:
              await xspam.send_video(e.chat.id, prn, caption=kkk)
              await asyncio.sleep(0.4)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], [".", "!", "/"]))
async def oahgfg(xspam: Client, e: Message):
      await e.reply_text(f"═══════════════════\n ꧁ 𒈞zαι∂ υѕєявσт𒈞꧂ \n═══════════════════")


@Client.on_message(filters.user(SUDO_USERS) & filters.command("alive"), [".", "!"])
async def hello(client: Client, message: Message):
    buttons = [
           [
                InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/TheUpdatesChannel"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/TheSupportChat"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=Zaid, reply_markup=reply_markup)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], [".", "!", "/"]))
@Client.on_message(filters.me & filters.command(["raid"], ["."]))
async def raid(xspam: Client, e: Message):  
      Zaid = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Zaid) == 2:
          counts = int(Zaid[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await xspam.get_users(Zaid[1])
          id = ok.id
#          try:
#              userz = await xspam.get_users(id)
#          except:
#              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
#              return #remove # to enable this
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          #msg_id = e.reply_to_message.message_id
          counts = int(Zaid[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          #RiZoeL = xspam.get_messages(e.chat.id, msg_id)
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          try:
              userz = await xspam.get_users(id)
          except:
              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
              return
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text("Usage: .raid count username")


add_command_help(
    "advanced",
    [
        [".delayspam", "<count and text>`."],
        [".raid", "<user id and count>`."],
        [".pornspam", "<count>`."],
    ],
)
