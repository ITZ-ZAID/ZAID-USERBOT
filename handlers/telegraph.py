import os
from telegraph import upload_file

from pyrogram import filters, Client
from pyrogram.types import Message
from handlers.help import *

@Client.on_message(filters.command(["tm", "tgm", "telegraph"], ".") & filters.me) 
async def telegraph(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4")
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply_text("not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message, file_name="root/nana/"
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await client.send_message(message.chat.id, document)
    else:
        await message.reply_text(
            f"**Document passed to: [Telegra.ph](https://telegra.ph{response[0]})**",
        )
    finally:
        os.remove(download_location)


add_command_help(
    "www",
    [
        [".tm", "Reply to Media as args to upload it to telegraph."],
    ],
)
