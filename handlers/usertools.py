import os
from asyncio import sleep

from pyrogram import filters, Client
from pyrogram.raw import functions
from pyrogram.types import Message

from helpers.SQL.cloner_db import backup_indentity, restore_identity
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


@Client.on_message(filters.me & filters.command(["clone"], ["."]))
async def clone(client: Client, message: Message):
    if message.reply_to_message:
        target = message.reply_to_message.from_user.id
    elif len(message.text.split()) >= 2 and message.text.split()[1].isdigit():
        await message.edit("Select target user to clone their identity!")
    else:
        await message.edit("Select target user to clone their identity!")
    if "origin" in message.text:
        my_self = await app.get_me()
        my_self = await client.send(functions.users.GetFullUser(id=await client.resolve_peer(my_self['id'])))

        # Backup my first name, last name, and bio
        backup_indentity(my_self['user']['first_name'], my_self['user']['last_name'], my_self['about'])
    q = await client.get_profile_photos(target)
    await client.download_media(q[0], file_name="handlers/cache/pp.png")
    await client.set_profile_photo("handlers/cache/pp.png")
    t = await client.get_users(target)
    t = await client.send(functions.users.GetFullUser(id=await client.resolve_peer(t['id'])))
    p_file = functions.account
    await client.send(
        p_file.UpdateProfile(first_name=t['user']['first_name'] if t['user']['first_name'] is not None else "",
                             last_name=t['user']['last_name'] if t['user']['last_name'] is not None else "",
                             about=t['about'] if t['about'] is not None else ""))
    await message.edit("`New identity has changed!`")
    await sleep(5)
    await message.delete()


@Client.on_message(filters.me & filters.command(["revert"], ["."]))
async def revert(client: Client, message: Message):
    first_name, last_name, bio = restore_identity()

    await client.send(functions.account.UpdateProfile(first_name=first_name if first_name is not None else "",
                                                      last_name=last_name if last_name is not None else "",
                                                      about=bio if bio is not None else ""))

    photos = await client.get_profile_photos("me")

    await client.delete_profile_photos(photos[0].file_id)

    await message.edit("`Identity Reverted`")
    await sleep(5)
    await message.delete()


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
