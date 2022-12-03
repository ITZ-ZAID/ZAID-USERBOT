import asyncio

import humanize
from pyrogram import filters, Client
from pyrogram.types import Message

from Zaid.modules.help import add_command_help


async def progress_callback(current, total, bot: Client, message: Message):
    if int((current / total) * 100) % 25 == 0:
        await message.edit(f"{humanize.naturalsize(current)} / {humanize.naturalsize(total)}")


@Client.on_message(filters.command('upload', '.') & filters.me)
async def upload_helper(bot: Client, message: Message):
    if len(message.command) > 1:
        await bot.send_document('self', message.command[1], progress=progress_callback, progress_args=(bot, message))
    else:
        await message.edit('No path provided.')
        await asyncio.sleep(3)

    await message.delete()


add_command_help(
    "upload",
    [
        [".upload", "Upload the file to telegram from the given system file path."],
    ],
)
