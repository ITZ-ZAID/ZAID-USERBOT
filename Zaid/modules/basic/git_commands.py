import asyncio
import datetime
import os
from asyncio import sleep
from glob import iglob
from random import randint

import aiofiles
from pyrogram import filters, Client
from pyrogram.types import Message
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg

from Zaid.helper.PyroHelpers import ReplyCheck
from Zaid.helper.aiohttp_helper import AioHttp
from Zaid.modules.help import add_command_help


@Client.on_message(filters.command(["ggraph", "commitgraph"], ".") & filters.me)
async def commit_graph(bot: Client, message: Message):
    if len(message.command) < 2:
        await message.edit(
            "Please provide a github profile username to generate the graph!"
        )
        await sleep(2)
        await message.delete()
        return
    else:
        git_user = message.command[1]

    url = f"https://ghchart.rshah.org/{git_user}"
    file_name = f"{randint(1, 999)}{git_user}"

    resp = await AioHttp.get_raw(url)
    f = await aiofiles.open(f"{file_name}.svg", mode="wb")
    await f.write(resp)
    await f.close()

    try:
        drawing = svg2rlg(f"{file_name}.svg")
        renderPM.drawToFile(drawing, f"{file_name}.png")
    except UnboundLocalError:
        await message.edit("Username does not exist!")
        await sleep(2)
        await message.delete()
        return

    await asyncio.gather(
        bot.send_photo(
            chat_id=message.chat.id,
            photo=f"{file_name}.png",
            caption=git_user,
            reply_to_message_id=ReplyCheck(message),
        ),
        message.delete(),
    )

    for file in iglob(f"{file_name}.*"):
        os.remove(file)


add_command_help(
    "git",
    [
        [".ggraph | .commitgraph", "Gets the commit graph for a Github user."],
    ],
)
