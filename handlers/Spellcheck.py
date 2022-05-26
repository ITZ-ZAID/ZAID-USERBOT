#~ Ported from Friday[Telethon]
#~ ©FridayUB

import os
from pyrogram import Client, filters
from pyrogram.types import *


try:
    import textblob
except:
    os.system("pip install textblob")
    import textblob

from textblob import TextBlob

from helpers.basic import edit_or_reply, get_text
from handlers.help import *

@Client.on_message(filters.command('spellcheck', ["."]) & filters.me)
async def make_grid(client: Client, message: Message):
    ok = await edit_or_reply(message, "`Checking Text`")
    input_str = get_text(message)
    if not input_str:
        if not message.reply_to_message:
           return await ok.edit("`Nothing To Check...`")
        if not message.reply_to_message.text:
           return await ok.edit("`Nothing To Check...`")
    input_str = input_str or message.reply_to_message.text

    a = input_str
    
    b = TextBlob(a)
    
    c = b.correct()
    await message.edit(
        f"<b><u>Check Completed</b></u> \n\n<b>Original Text</b>:-  <code>{a}</code> \n<b>Corrected Text:-</b> <code>{c}</code>",
        parse_mode="HTML",
    )

add_command_help(
    "spellcheck",
    [
        [".spellcheck", "To Check Your Spell Mistakes."],
    ],
)
