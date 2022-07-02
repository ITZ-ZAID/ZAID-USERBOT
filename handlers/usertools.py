import os
from asyncio import sleep

from pyrogram import filters, Client
from pyrogram.raw import functions
from pyrogram.types import Message

from handlers.help import add_command_help

profile_photo = "handlers/cache/pfp.jpg"


@Client.on_message(filters.me & filters.command(["setpfp"], ["."]))
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (replied and replied.media and (
            replied.photo or (
            replied.document and "image" in replied.document.mime_type
    )
    )
    ):
        await client.download_media(
            message=replied,
            file_name=profile_photo
        )
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.edit(
            "<code>Profile picture changed.</code>",
            parse_mode='html'
        )
    else:
        await message.edit("```Reply to any photo to set as pfp```")
        await sleep(3)
        await message.delete()


@Client.on_message(filters.me & filters.command(["vpfp"], ["."]))
async def view_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if replied:
        user = await client.get_users(replied.from_user.id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.edit("profile photo not found!")
        return
    await client.download_media(
        user.photo.big_file_id,
        file_name=profile_photo
    )
    await client.send_photo(message.chat.id, profile_photo)
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)



add_command_help(
    "usertools",
    [
        [".setpfp", "Reply to any photo to set as pfp."],
        [".vpfp", "View current pfp of user."],
        [
            ".clone",
            "clone user identity without original backup",
        ],
        [
            ".clone origin",
            "clone user identity with original backup",
        ],
        [
            ".revert",
            "revert to original identity",
        ],
    ],
)
