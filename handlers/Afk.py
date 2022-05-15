import time

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helpers.SQL import DB_AVAILABLE
from helpers.msg_types import Types, get_message_type
from helpers.parser import mention_markdown, escape_markdown
from pyrogram.types import Message

from helpers.SQL.afk_db import set_afk, get_afk
from main import Owner
from handlers.help import add_command_help

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

# Set priority to 11 and 12
MENTIONED = []
AFK_RESTIRECT = {}
DELAY_TIME = 60  # seconds



@Client.on_message(filters.me & (filters.command(["afk"], ["."]) | filters.regex("^brb ")))
async def afk(client: Client, message: Message):
    if len(message.text.split()) >= 2:
        getself = await client.get_me()
        if getself.last_name:
            OwnerName = getself.first_name + " " + getself.last_name
        else:
            OwnerName = getself.first_name 
        set_afk(True, message.text.split(None, 1)[1])
        await message.edit(
            "{} is now AFK!\nBecause of {}".format(mention_markdown(message.from_user.id, message.from_user.first_name),
                                                   message.text.split(None, 1)[1]))
        await client.send_message(Owner, "You are now AFK!\nBecause of {}".format(message.text.split(None, 1)[1]))
    else:
        set_afk(True, "")
        await message.edit(
            "{} is now AFK!".format(mention_markdown(message.from_user.id, message.from_user.first_name)))
        await client.send_message(Owner, "You are now AFK!")
    await message.stop_propagation()


@Client.on_message(filters.mentioned & ~filters.bot, group=11)
async def afk_mentioned(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    getself = await client.get_me()
    if getself.last_name:
        OwnerName = getself.first_name + " " + getself.last_name
    else:
        OwnerName = getself.first_name
    if get and get['afk']:
        if "-" in str(message.chat.id):
            cid = str(message.chat.id)[4:]
        else:
            cid = str(message.chat.id)

        if cid in list(AFK_RESTIRECT):
            if int(AFK_RESTIRECT[cid]) >= int(time.time()):
                return
        AFK_RESTIRECT[cid] = int(time.time()) + DELAY_TIME
        if get['reason']:
            await message.reply(
                "Sorry, {} is AFK!\nBecause of {}".format(mention_markdown(Owner, OwnerName), get['reason']))
        else:
            await message.reply("Sorry, {} is AFK!".format(mention_markdown(Owner, OwnerName)))

        _, message_type = get_message_type(message)
        if message_type == Types.TEXT:
            if message.text:
                text = message.text
            else:
                text = message.caption
        else:
            text = message_type.name

        MENTIONED.append(
            {"user": message.from_user.first_name, "user_id": message.from_user.id, "chat": message.chat.title,
             "chat_id": cid, "text": text, "message_id": message.message_id})
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Go to message", url="https://t.me/c/{}/{}".format(cid, message.message_id))]])
        await client.send_message(Owner, "{} mentioned you in {}\n\n{}\n\nTotal count: `{}`".format(
            mention_markdown(message.from_user.id, message.from_user.first_name), message.chat.title, text[:3500],
            len(MENTIONED)), reply_markup=button)


@Client.on_message(filters.me & filters.group, group=12)
async def no_longer_afk(client: Client, message: Message):
    global MENTIONED
    get = get_afk()
    getself = await client.get_me()
    OwnerName = getself.first_name
    if get and get['afk']:
        await client.send_message(message.from_user.id, "You are no longer afk!")
        set_afk(False, "")
        text = "**Total {} mentioned you**\n".format(len(MENTIONED))
        for x in MENTIONED:
            msg_text = x["text"]
            if len(msg_text) >= 11:
                msg_text = "{}...".format(x["text"])
            text += "- [{}](https://t.me/c/{}/{}) ({}): {}\n".format(escape_markdown(x["user"]), x["chat_id"],
                                                                     x["message_id"], x["chat"], msg_text)
        await client.send_message(message.from_user.id, text)
        MENTIONED = []

add_command_help(
    "afk",
    [
        [".afk", "Activates AFK mode with reason as anything after .afk\nUsage: ```.afk <reason>```"],
    ],
)
