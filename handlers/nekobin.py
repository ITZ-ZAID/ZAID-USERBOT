from handlers.help import add_command_help
import asyncio
import requests
import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message




@Client.on_message(
    filters.command(["pasty"], ["."]) & filters.me
)
async def paste(app: Client, message: Message):
    text = message.reply_to_message.text
    try:
        params = {"content": text}
        headers = {'content-type' : 'application/json'}
        url = "https://pasty.lus.pm/api/v2/pastes/"
        paste = requests.post(url, json=params, headers=headers)
        key = paste.json()["id"]
    except Exception:
        await message.edit_text("`API is down try again later`")
        await asyncio.sleep(2)
        await message.delete()
        return
    else:
        url = f"https://pasty.lus.pm/{key}"
        reply_text = f"**Pasted to: [Pasty]({url})\nRaw link: [Raw]({url}/raw)**"
        delete = (
            True
            if len(message.command) > 1
            and message.command[1] in ["d", "del"]
            and message.reply_to_message.from_user.is_self
            else False
        )
        if delete:
            await asyncio.gather(
                app.send_message(
                    message.chat.id, reply_text, disable_web_page_preview=True
                ),
                message.reply_to_message.delete(),
                message.delete(),
            )
        else:
            await message.edit_text(
                reply_text,
                disable_web_page_preview=True,
            )

@Client.on_message(
    filters.command(["neko", "paste", "nekobin"], ["."]) & filters.me
)
async def neko(app: Client, message: Message):
    text = message.reply_to_message.text
    try:
        params = {"content": text}
        headers = {'content-type' : 'application/json'}
        url = "https://nekobin.com/api/documents"
        neko = requests.post(url, json=params, headers=headers)
        key = neko.json()["result"]["key"]
    except Exception:
        await message.edit_text("`API is down try again later`")
        await asyncio.sleep(2)
        await message.delete()
        return
    else:
        url = f"https://nekobin.com/{key}"
        reply_text = f"**Pasted to: [Nekobin]({url})**"
        delete = (
            True
            if len(message.command) > 1
            and message.command[1] in ["d", "del"]
            and message.reply_to_message.from_user.is_self
            else False
        )
        if delete:
            await asyncio.gather(
                app.send_message(
                    message.chat.id, reply_text, disable_web_page_preview=True
                ),
                message.reply_to_message.delete(),
                message.delete(),
            )
        else:
            await message.edit_text(
                reply_text,
                disable_web_page_preview=True,
            )

add_command_help(
    "paste",
    [
        [
            ".paste `or` .bin `or` .neko `or` .nekobin",
            "Create a Nekobin paste using replied to message.",
        ],
    ],
)
