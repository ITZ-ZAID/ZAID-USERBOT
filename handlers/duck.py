from pyrogram import Client, filters
from pyrogram.types import Message
from handlers.help import *


@Client.on_message(filters.command("duck", ["."]) & filters.me)
async def duckgo(client: Client, message: Message):
    input_str = " ".join(message.command[1:])
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ", "+"))
    if sample_url:
        link = sample_url.rstrip()
        await message.edit_text(
            "Let me 🦆 DuckDuckGo that for you:\n🔎 [{}]({})".format(input_str, link)
        )
    else:
        await message.edit_text("something is wrong. please try again later.")


add_command_help(
    "duckduckgo",
    [
        [".duck", "To Get Link Of Duck Duck Go."],
    ],
)
