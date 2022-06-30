"""
Set yourself to afk.
When marked as AFK, any mentions will be replied to with a message to say you're not available!
And that mentioned will notify you by your Assistant.

If you're restart your bot, all counter and data in cache will be reset.
But you will still in afk, and always reply when got mentioned.

──「 **Set AFK status** 」── -> `afk (*reason)` Set yourself to afk, give a reason if need. When someone tag you, 
you will says in afk with reason, and that mentioned will sent in your assistant PM. 

To exit from afk status, send anything to anywhere, exclude PM and saved message.

* = Optional
"""

import time
from pyrogram import filters
import asyncio

from main import LOG_GROUP
from config import PREFIX, LOG_CHAT
from helpers.pyrohelper import get_arg
import helpers.mongo.afkdb as Zaid
from helpers.pyrohelper import user_afk
from handlers.alive import get_readable_time
from helpers.utils import get_message_type, Types

LOG_CHAT = LOG_GROUP

MENTIONED = []
AFK_RESTIRECT = {}
DELAY_TIME = 60


@Client.on_message(filters.command("afk", ["."]) & filters.me)
async def afk(app: Client, message):
    afk_time = int(time.time())
    arg = get_arg(message)
    if not arg:
        reason = None
    else:
        reason = arg
    await Zaid.set_afk(True, afk_time, reason)
    await message.edit("**I'm goin' AFK**")


@Client.on_message(filters.mentioned & ~filters.bot & filters.create(user_afk), group=11)
async def afk_mentioned(app: Client, message):
    global MENTIONED
    afk_time, reason = await Zaid.afk_stuff()
    afk_since = get_readable_time(time.time() - afk_time)
    if "-" in str(message.chat.id):
        cid = str(message.chat.id)[4:]
    else:
        cid = str(message.chat.id)

    if cid in list(AFK_RESTIRECT) and int(AFK_RESTIRECT[cid]) >= int(time.time()):
        return
    AFK_RESTIRECT[cid] = int(time.time()) + DELAY_TIME
    if reason:
        await message.reply(
            f"**I'm AFK right now (since {afk_since})\nReason:** __{reason}__"
        )
    else:
        await message.reply(f"**I'm AFK right now (since {afk_since})**")

        _, message_type = get_message_type(message)
        if message_type == Types.TEXT:
            text = message.text or message.caption
        else:
            text = message_type.name

        MENTIONED.append(
            {
                "user": message.from_user.first_name,
                "user_id": message.from_user.id,
                "chat": message.chat.title,
                "chat_id": cid,
                "text": text,
                "message_id": message.message_id,
            }
        )


@Client.on_message(filters.create(user_afk) & filters.outgoing)
async def auto_unafk(app: Client, message):
    await Zaid.set_unafk()
    unafk_message = await app.send_message(message.chat.id, "**I'm no longer AFK**")
    global MENTIONED
    text = "**Total {} mentioned you**\n".format(len(MENTIONED))
    for x in MENTIONED:
        msg_text = x["text"]
        if len(msg_text) >= 11:
            msg_text = "{}...".format(x["text"])
        text += "- [{}](https://t.me/c/{}/{}) ({}): {}\n".format(
            x["user"],
            x["chat_id"],
            x["message_id"],
            x["chat"],
            msg_text,
        )
        await app.send_message(LOG_CHAT, text)
        MENTIONED = []
    await asyncio.sleep(2)
    await unafk_message.delete()

add_command_help(
    "afk",
    [
        [".afk", "Activates AFK mode with reason as anything after .afk\nUsage: ```.afk <reason>```"],
    ],
)
