
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


# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!




import os
import sys


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], [".", "!"]))
async def help(_, e: Message):
        RiZoeL = e.text.split(" ")
        if len(RiZoeL) > 1:
            helping = RiZoeL[1]
            if helping.lower() == "spam":
                await e.reply(spam_help)
            elif helping.lower() == "dm":
                await e.reply(dm_help)
            elif helping.lower() == "userbot":
                await e.reply(userbot_help)
            elif helping.lower() == "join":
                await e.reply(join_help)
            elif helping.lower() == "leave":
                await e.reply(leave_help)
            elif helping.lower() == "owner":
                await e.reply(owner_help)
            else:
                await e.reply(help_menu)
        else:
            await e.reply(help_menu)


spam_help = f"""
**• Spam Cmds •**

**spam**: Spams a message for given counter (no Count limit)
syntax:
 .spam <count> <message to spam> 

**delayspam**: Delay spam a text for given counter after given time.
syntax:
 .delayspam <delay time(seconds)> <count> <message to spam> 

**Fast Spam**: Fast Spam a message for given counter (no Count limit)
syntax:
 .fspam <count> <message to spam>
 

**pornspam**: Porn Spam for given counter.
syntax:
 .pornspam <counter>

**raid:** Activates raid on any individual user for given range.
syntax:
 .raid <count> <username or user id>

**Hang:** Hang Message Spam
syntax:
.hang <counts>


**꧁ 𒈞zαι∂ υѕєявσт𒈞꧂**
"""


dm_help = f"""
**• Dm Cmds •**

**Dm:** Dm to any individual using spam bots
command:
  .dm <username or user id> <message>

**Dm Spam:** Spam in Dm of Any individual Users
command:
  .dmspam <username or user id> <count>  <message to spam>

**Dm Raid:** raid in Dm of Any individual Users
command:
  .dmraid <count> <username or user id>

**꧁ 𒈞zαι∂ υѕєявσт𒈞꧂**
"""


join_help = f"""
**• Join Cmds •**

**join:** Join any Public Channel and group
command:
  .join <private/public Chat invite link or username>


**꧁ 𒈞zαι∂ υѕєявσт𒈞꧂**
"""

leave_help = f"""
**• Leave Cmds •**

**leave:** Leave any Public/private Group or Channel
syntax:
i) .leave <group Username or chat user id>
ii) .leave

**꧁ 𒈞zαι∂ υѕєявσт𒈞꧂**
"""

userbot_help = f"""
**• Userbot Cmds •**

- .ping : To check Ping 

- .alive : To check Bot Version and Other info

- .restart : To Restart Your Spam Bots

**꧁ 𒈞zαι∂ υѕєявσт𒈞꧂**
"""


owner_help = f"""
**Profile:** Profile And Other Cmds
commands:

1) .setname <Profile Name>
2) .setbio <coustom Bio>
3) .setpic <reply to media>

**꧁ 𒈞zαι∂ υѕєявσт𒈞꧂**
"""

help_menu = f"""
**There are following categories**

`owner` : Get all owner commands and its usage
`spam` : Get all spam commands and its usage
`dm` : Get all dm commands and its usage
`join` : Get join commands and its usage
`leave` : Get leave commands and its usage
`userbot` : Get all userbot commands

**Type** .help <category> **to get all syntax in that category and its usage**
**Example**: `.help spam`

**꧁ 𒈞zαι∂ υѕєявσт𒈞꧂**
"""

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


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], [".", "!"]))
async def hello(client: Client, message: Message):
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=Zaid)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["join"], [".", "!", "/"]))
async def jhoin(client: Client, message: Message):
    zaid = message.text[6:]
    count = 0
    if not zaid:
        return await message.reply_text("Need a chat username or invite link to join.")
    if zaid.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(zaid)
        await message.reply_text(f"**Joined**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["leave", "left"], [".", "!", "/"]))
async def leasse(client: Client, message: Message):
    zaid = message.text[6:]
    count = 0
    if not zaid:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if zaid.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(zaid)
        await message.reply_text(f"**Lefted**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["spam", "spamming"], [".", "!", "/"]))
async def skkkspam(client: Client, message: Message):
    sex  = await message.reply_text("⚡ Usage:\n /spam 10 Kkkk ")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    if re.search(Owners.lower(), msg.lower()):
        return await e.reply("**Sorry !!**")
    if int(message.chat.id) in GROUP:
        await sex.edit("<b>Sorry Kid!! You Can't Spam In My Creator Groups</b>") 
        return

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await sex.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


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
