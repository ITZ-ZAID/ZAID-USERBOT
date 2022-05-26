import asyncio
import datetime
import math
import os
import zipfile
from collections import defaultdict
from io import BytesIO
import os
import subprocess
import textwrap
from json import JSONDecodeError
import numpy as np
from PIL import Image, ImageDraw
from PIL import Image, ImageDraw, ImageFont
from pyrogram import emoji
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram import filters, Client
from typing import Tuple
from pyrogram.types import Message
from handlers.help import *

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def convert_to_image(message: Message, client: Client) -> [None, str]:
    """Convert Most Media Formats To Raw Image"""
    if not message:
        return None
    if not message.reply_to_message:
        return None
    final_path = None
    if not (
        message.reply_to_message.video
        or message.reply_to_message.photo
        or message.reply_to_message.sticker
        or message.reply_to_message.media
        or message.reply_to_message.animation
        or message.reply_to_message.audio
    ):
        return None
    if message.reply_to_message.photo:
        final_path = await message.reply_to_message.download()
    elif message.reply_to_message.sticker:
        if message.reply_to_message.sticker.mime_type == "image/webp":
            final_path = "webp_to_png_s_proton.png"
            path_s = await message.reply_to_message.download()
            im = Image.open(path_s)
            im.save(final_path, "PNG")
        else:
            path_s = await client.download_media(message.reply_to_message)
            final_path = "lottie_proton.png"
            cmd = (
                f"lottie_convert.py --frame 0 -if lottie -of png {path_s} {final_path}"
            )
            await run_cmd(cmd)
    elif message.reply_to_message.audio:
        thumb = message.reply_to_message.audio.thumbs[0].file_id
        final_path = await client.download_media(thumb)
    elif message.reply_to_message.video or message.reply_to_message.animation:
        final_path = "fetched_thumb.png"
        vid_path = await client.download_media(message.reply_to_message)
        await run_cmd(f"ffmpeg -i {vid_path} -filter:v scale=500:500 -an {final_path}")
    return final_path

@Client.on_message(filters.command(["packinfo", "mydetails"], [".", ""]) & filters.me)
async def packinfo(client: Client, message: Message):
    rep = await message.edit_text("`Processing...`")
    if not message.reply_to_message:
        await rep.edit("Please Reply To Sticker...")
        return
    if not message.reply_to_message.sticker:
        await rep.edit("Please Reply To A Sticker...")
        return
    if not message.reply_to_message.sticker.set_name:
        await rep.edit("`Seems Like A Stray Sticker!`")
        return
    stickerset = await client.send(
        GetStickerSet(
            stickerset=InputStickerSetShortName(
                short_name=message.reply_to_message.sticker.set_name
            )
        )
    )
    emojis = []
    for stucker in stickerset.packs:
        if stucker.emoticon not in emojis:
            emojis.append(stucker.emoticon)
    output = f"""**Sticker Pack Title **: `{stickerset.set.title}`
**Sticker Pack Short Name **: `{stickerset.set.short_name}`
**Stickers Count **: `{stickerset.set.count}`
**Archived **: `{stickerset.set.archived}`
**Official **: `{stickerset.set.official}`
**Masks **: `{stickerset.set.masks}`
**Animated **: `{stickerset.set.animated}`
**Emojis In Pack **: `{' '.join(emojis)}`
"""
    await rep.edit(output)


@Client.on_message(filters.command(["steal", "kang"], [".", ""]) & filters.me)
async def kang(client: Client, message: Message):
    rep= await message.edit_text("`Using Megic To Kang This Sticker...`")
    if not message.reply_to_message:
        await rep.edit("Please Reply To Sticker...")
        return
    Hell = get_text(message)
    name = ""
    pack = 1
    nm = message.from_user.username
    if nm:
        nam = message.from_user.username
        name = nam[1:]
    else:
        name = message.from_user.first_name
    packname = f"@{nm} Kang Pack {pack}"
    packshortname = f"Zaid_{message.from_user.id}_{pack}"
    non = [None, "None"]
    emoji = "🤴"
    try:
        Hell = Hell.strip()
        if not Hell.isalpha():
            if not Hell.isnumeric():
                emoji = Hell
        else:
            emoji = "🤴"
    except:
        emoji = "🤴"
    exist = None
    is_anim = False
    if message.reply_to_message.sticker:
        if not Hell:
            emoji = message.reply_to_message.sticker.emoji or "😁"
        is_anim = message.reply_to_message.sticker.is_animated
        if is_anim:
            packshortname += "_animated"
            packname += " Animated"
        if message.reply_to_message.sticker.mime_type == "application/x-tgsticker":
            file_name = await message.reply_to_message.download("AnimatedSticker.tgs")
        else:
            cool = await convert_to_image(message, client)
            if not cool:
                await rep.edit("`Reply to a valid media first.`")
                return
            file_name = resize_image(cool)
    elif message.reply_to_message.document:
        if message.reply_to_message.document.mime_type == "application/x-tgsticker":
            is_anim = True
            packshortname += "_animated"
            packname += " Animated"
            file_name = await message.reply_to_message.download("AnimatedSticker.tgs")
    else:
        cool = await convert_to_image(message, client)
        if not cool:
            await rep.edit("`Reply to a valid media first.`")
            return
        file_name = resize_image(cool)
    try:
        exist = await client.send(
            GetStickerSet(stickerset=InputStickerSetShortName(short_name=packshortname))
        )
    except StickersetInvalid:
        pass
    if exist:
        try:
            await client.send_message("stickers", "/addsticker")
        except YouBlockedUser:
            await rep.edit("`Please Unblock @Stickers`")
            await client.unblock_user("stickers")
        await client.send_message("stickers", packshortname)
        await asyncio.sleep(0.2)
        limit = "50" if is_anim else "120"
        messi = (await client.get_history("stickers", 1))[0]
        while limit in messi.text:
            pack += 1
            prev_pack = int(pack) - 1
            await rep.edit(f"Kang Pack Vol __{prev_pack}__ is Full! Switching To Vol __{pack}__ Kang Pack")
            packname = f"@{nm} Kang Pack {pack}"
            packshortname = f"Zaid_{message.from_user.id}_{pack}"
            if is_anim:
                packshortname += "_animated"
                packname += " Animated"
            await client.send_message("stickers", packshortname)
            await asyncio.sleep(0.2)
            messi = (await client.get_history("stickers", 1))[0]
            if messi.text == "Invalid pack selected.":
                if is_anim:
                    await client.send_message("stickers", "/newanimated")
                else:
                    await client.send_message("stickers", "/newpack")
                await asyncio.sleep(0.5)
                await client.send_message("stickers", packname)
                await asyncio.sleep(0.2)
                await client.send_document("stickers", file_name)
                await asyncio.sleep(1)
                await client.send_message("stickers", emoji)
                await asyncio.sleep(0.5)
                await client.send_message("stickers", "/publish")
                if is_anim:
                    await client.send_message("stickers", f"<{packname}>")
                await client.send_message("stickers", "/skip")
                await asyncio.sleep(0.5)
                await client.send_message("stickers", packshortname)
                await rep.edit(
                    f"Sticker Added To Your Pack With Emoji - {emoji}. You Can Find It [Here](https://t.me/addstickers/{packshortname})"
                )
                return
        await client.send_document("stickers", file_name)
        await asyncio.sleep(1)
        await client.send_message("stickers", emoji)
        await asyncio.sleep(0.5)
        await client.send_message("stickers", "/done")
        await rep.edit(
            f"`Sticker Added To Your Pack With Emoji - {emoji}. You Can Find It` [Here](https://t.me/addstickers/{packshortname})"
        )
    else:
        if is_anim:
            await client.send_message("stickers", "/newanimated")
        else:
            await client.send_message("stickers", "/newpack")
        await client.send_message("stickers", packname)
        await asyncio.sleep(0.2)
        await client.send_document("stickers", file_name)
        await asyncio.sleep(1)
        await client.send_message("stickers", emoji)
        await asyncio.sleep(0.5)
        await client.send_message("stickers", "/publish")
        await asyncio.sleep(0.5)
        if is_anim:
            await client.send_message("stickers", f"<{packname}>")
        await client.send_message("stickers", "/skip")
        await asyncio.sleep(0.5)
        await client.send_message("stickers", packshortname)
        await rep.edit(
            f"`Sticker Added To Your Pack With Emoji - {emoji}. You Can Find It` [Here](https://t.me/addstickers/{packshortname})"
        )
        if os.path.exists(file_name):
            os.remove(file_name)


def resize_image(image):
    im = Image.open(image)
    maxsize = (512, 512)
    if (im.width and im.height) < 512:
        size1 = im.width
        size2 = im.height
        if im.width > im.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        im = im.resize(sizenew)
    else:
        im.thumbnail(maxsize)
    file_name = "Sticker.png"
    im.save(file_name, "PNG")
    if os.path.exists(image):
        os.remove(image)
    return file_name


add_command_help(
    "sticker",
    [
        [".kang | .steal", "This command helps you to kang Stickers."],
        [".packinfo", "Get Sticker Pack details."],
    ],
)
