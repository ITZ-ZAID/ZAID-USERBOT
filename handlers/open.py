import os
import re
import json
import requests
from pyrogram import Client, filters
from pyrogram.types import *
from helpers.basic import edit_or_reply
from handlers.help import *

async def s_paste(message, extension="txt"):
    siteurl = "https://spaceb.in/api/v1/documents/"
    try:
        response = requests.post(
            siteurl, data={"content": message, "extension": extension}
        )
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        if response["error"] != "" and response["status"] < 400:
            return {"error": response["error"]}
        return {
            "url": f"https://spaceb.in/{response['payload']['id']}",
            "raw": f"{siteurl}{response['payload']['id']}/raw",
            "bin": "Spacebin",
        }
    return {"error": "Unable to reach spacebin."}


@Client.on_message(filters.command('open', ["."]) & filters.me)
async def open_file(client: Client, m: Message):
    xd = await edit_or_reply(m, "`Reading File!`")
    f = await _.download_media(m.reply_to_message)
    if f:
        # do
        _error = open(f, "r")
        _error_ = _error.read()
        _error.close()
        if len(_error_) >= 4096:
            await xd.edit("`Output is too large pasting to Spacebin!`")
            ext = "py"
            x = await s_paste(_error_, ext)
            s_link = x["url"]
            s_raw = x["raw"]
            pasted = f"**Pasted to Spacebin**\n**Link:** [Spacebin]({s_link})\n**Raw Link:** [Raw]({s_raw})"
            return await xd.edit(pasted, disable_web_page_preview=True)
        else:
            await xd.edit(f"**Output:**\n```{_error_}```")
    else:
        await edit_or_reply(m, "Reply to a File to open it!")
        os.remove(f)


add_command_help(
    "spacebin",
    [
        [".open", "Reply To a Document To Paste in Spacebin."],
    ],
)
