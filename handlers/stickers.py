from typing import Tuple
from handlers.help import *
import io
import os
import random
import time
from pyrogram.types import Message
from PIL import Image
from pyrogram import emoji, filters, Client
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.errors import YouBlockedUser, StickersetInvalid
from helpers.pyrohelper import get_args


@Client.on_message(filters.command(["kang", "steal"], ["."]) & filters.me)
async def kang(app: Client, message):
    user = await app.get_me()
    replied = message.reply_to_message
    photo = None
    emoji_ = None
    is_anim = False
    resize = False
    if replied and replied.media:
        if replied.photo:
            resize = True
        elif replied.document and "image" in replied.document.mime_type:
            resize = True
        elif replied.document and "tgsticker" in replied.document.mime_type:
            is_anim = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                await message.edit("`Sticker has no Name!`")
                return
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            if not replied.sticker.file_name.endswith(".tgs"):
                resize = True
        else:
            await message.edit("`Unsupported File!`")
            return
        await message.edit(f"`{random.choice(KANGING_STR)}`")
        photo = await app.download_media(message=replied)
    else:
        await message.edit("`I can't kang that...`")
        return
    if photo:
        args = get_args(message)
        pack = 1
        if len(args) == 2:
            emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric():
                pack = int(args[0])
            else:
                emoji_ = args[0]

        if emoji_ and emoji_ not in (
            getattr(emoji, a) for a in dir(emoji) if not a.startswith("_")
        ):
            emoji_ = None
        if not emoji_:
            emoji_ = "🤔"

        u_name = user.username
        if u_name:
            u_name = "@" + u_name
        else:
            u_name = user.first_name or user.id
        packname = f"a{user.id}_by_zect_{pack}"
        custom_packnick = f"{u_name}'s kang pack"
        packnick = f"{custom_packnick} Vol.{pack}"
        cmd = "/newpack"
        if resize:
            photo = resize_photo(photo)
        if is_anim:
            packname += "_anim"
            packnick += " (Animated)"
            cmd = "/newanimated"
        exist = False
        try:
            exist = await app.send(
                GetStickerSet(stickerset=InputStickerSetShortName(short_name=packname), hash=0)
            )
        except StickersetInvalid:
            pass
        if exist is not False:
            try:
                await app.send_message("Stickers", "/addsticker")
            except YouBlockedUser:
                await message.edit("first **unblock** @Stickers")
                return
            await app.send_message("Stickers", packname)
            limit = "50" if is_anim else "120"
            while limit in await get_response(message):
                pack += 1
                packname = f"a{user.id}_by_zect_{pack}"
                packnick = f"{custom_packnick} Vol.{pack}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (Animated)"
                await message.edit(
                    "`Switching to Pack " + str(pack) + " due to insufficient space`"
                )
                await app.send_message("Stickers", packname)
                if await get_response(message) == "Invalid pack selected":
                    await app.send_message("Stickers", cmd)
                    await get_response(message)
                    await app.send_message("Stickers", packnick)
                    await get_response(message)
                    await app.send_document("Stickers", photo)
                    await get_response(message)
                    await app.send_message("Stickers", emoji_)
                    await get_response(message)
                    await app.send_message("Stickers", "/publish")
                    if is_anim:
                        await get_response(message)
                        await app.send_message(
                            "Stickers", f"<{packnick}>", parse_mode=None
                        )
                    await get_response(message)
                    await app.send_message("Stickers", "/skip")
                    await get_response(message)
                    await app.send_message("Stickers", packname)
                    out = f"[kanged](t.me/addstickers/{packname})"
                    await message.edit(
                        f"**Sticker** {out} __in a Different Pack__**!**"
                    )
                    return
            await app.send_document("Stickers", photo)
            time.sleep(0.2)
            rsp = await get_response(message)
            if "Sorry, the file type is invalid." in rsp:
                await message.edit(
                    "`Failed to add sticker, use` @Stickers "
                    "`bot to add the sticker manually.`"
                )
                return
            await app.send_message("Stickers", emoji_)
            await get_response(message)
            await app.send_message("Stickers", "/done")
        else:
            await message.edit("`Brewing a new Pack...`")
            try:
                await app.send_message("Stickers", cmd)
            except YouBlockedUser:
                await message.edit("first **unblock** @Stickers")
                return
            await app.send_message("Stickers", packnick)
            await get_response(message)
            await app.send_document("Stickers", photo)
            await get_response(message)
            rsp = await get_response(message)
            if "Sorry, the file type is invalid." in rsp:
                await message.edit(
                    "`Failed to add sticker, use` @Stickers "
                    "`bot to add the sticker manually.`"
                )
                return
            await app.send_message("Stickers", emoji_)
            await get_response(message)
            await app.send_message("Stickers", "/publish")
            if is_anim:
                await get_response(message)
                await app.send_message("Stickers", f"<{packnick}>", parse_mode=None)
            await get_response(message)
            await app.send_message("Stickers", "/skip")
            await get_response(message)
            await app.send_message("Stickers", packname)
        out = f"[kanged](t.me/addstickers/{packname})"
        await message.edit(f"**Sticker** {out}**!**")
        await app.read_history("Stickers")
        if os.path.exists(str(photo)):
            os.remove(photo)


@Client.on_message(filters.command("packinfo", ["."]) & filters.me)
async def sticker_pack_info_(app: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.edit("`I can't fetch info from nothing, can I ?!`")
        return
    if not replied.sticker:
        await message.edit("`Reply to a sticker to get the pack details`")
        return
    await message.edit("`Fetching details of the sticker pack, please wait..`")
    get_stickerset = await app.send(
        GetStickerSet(
            stickerset=InputStickerSetShortName(short_name=replied.sticker.set_name)
        )
    )
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)
    out_str = (
        f"**Sticker Title:** `{get_stickerset.set.title}\n`"
        f"**Sticker Short Name:** `{get_stickerset.set.short_name}`\n"
        f"**Archived:** `{get_stickerset.set.archived}`\n"
        f"**Official:** `{get_stickerset.set.official}`\n"
        f"**Masks:** `{get_stickerset.set.masks}`\n"
        f"**Animated:** `{get_stickerset.set.animated}`\n"
        f"**Stickers In Pack:** `{get_stickerset.set.count}`\n"
        f"**Emojis In Pack:**\n{' '.join(pack_emojis)}"
    )
    await message.edit(out_str)


def resize_photo(photo: str) -> io.BytesIO:
    """Resize the given photo to 512x512"""
    image = Image.open(photo)
    maxsize = 512
    scale = maxsize / max(image.width, image.height)
    new_size = (int(image.width * scale), int(image.height * scale))
    image = image.resize(new_size, Image.LANCZOS)
    resized_photo = io.BytesIO()
    resized_photo.name = "sticker.png"
    image.save(resized_photo, "PNG")
    os.remove(photo)
    return resized_photo


async def get_response(message):
    return [x async for x in app.iter_history("Stickers", limit=1)][0].text


KANGING_STR = (
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "hehe me stel ur stikér\nhehe.",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pacc looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal Your Sticker is stealing this sticker... ",
)



add_command_help(
    "sticker",
    [
        [".kang | .steal", "This command helps you to kang Stickers."],
        [".packinfo", "Get Sticker Pack details."],
    ],
)
