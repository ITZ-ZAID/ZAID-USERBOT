from typing import Tuple
from handlers.help import *
import os
import math
import asyncio
import shutil

from PIL import Image
from pyrogram.types import Message
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName

from helpers.pyrohelper import get_arg


async def convert_to_image(message, client) -> Union[None, str]:
    """
    Convert Most Media Formats To Raw Image
    """
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


@Client.on_message(filters.command("packinfo", ["."]) & filters.me)
async def packinfo(client: Client, message):
    pablo = await message.edit("Processing...")
    if not message.reply_to_message:
        await pablo.edit("`Please Reply to a Sticker!`")
        return
    if not message.reply_to_message.sticker:
        return await pablo.edit("`Please Reply to a Sticker!`")
    if not message.reply_to_message.sticker.set_name:
        await pablo.delete()
        return
    stickerset = await client.send(
        GetStickerSet(
            stickerset=InputStickerSetShortName(
                short_name=message.reply_to_message.sticker.set_name
            ),
            hash=0
        )
    )
    emojis = []
    for stucker in stickerset.packs:
        if stucker.emoticon not in emojis:
            emojis.append(stucker.emoticon)
    output = f"""**Sticker Pack Title **: `{stickerset.set.title}`
**Sticker Pack Short Name:** `{stickerset.set.short_name}`
**Stickers Count:** `{stickerset.set.count}`
**Archived:** `{stickerset.set.archived}`
**Official:** `{stickerset.set.official}`
**Masks:** `{stickerset.set.masks}`
**Animated:** `{stickerset.set.animated}`
**Emojis In Pack:** `{' '.join(emojis)}`
"""
    await pablo.edit(output)


@Client.on_message(filters.command("kang", ["."]) & filters.me)
async def kang_stick(NEXAUB: Client, message: Message):
    kang_msg = await e_or_r(nexaub_message=message, msg_text="`Kanging This Sticker to My Pack...`")
    if not message.reply_to_message:
        return await kang_msg.edit("`Please Reply to a Sticker or a image!`")
#     if not message.reply_to_message.sticker:
#         return await kang_msg.edit("`Please Reply to a Sticker!`")
    a_emoji = get_arg(message)
    pack = 1
    nm = message.from_user.username
    packname = f"@{nm} Kang Pack {pack}"
    packshortname = f"NEXAUB_{message.from_user.id}_{pack}"
    emoji = "🤔"
    try:
        a_emoji = a_emoji.strip()
        if not a_emoji.isalpha():
            if not a_emoji.isnumeric():
                emoji = a_emoji
        else:
            emoji = "🤔"
    except:
        emoji = "🤔"
    exist = None
    is_anim = False
    if message.reply_to_message.sticker:
        if not a_emoji:
            emoji = message.reply_to_message.sticker.emoji or "🤔"
        is_anim = message.reply_to_message.sticker.is_animated
        if is_anim:
            packshortname += "_animated"
            packname += " Animated"
        if message.reply_to_message.sticker.mime_type == "application/x-tgsticker":
            file_name = await message.reply_to_message.download("AnimatedSticker.tgs")
        else:
            cool = await convert_to_image(message, NEXAUB)
            if not cool:
                return await kang_msg.edit("**Error:** `Unsupported Media`")
            file_name = resize_image(cool)
    elif message.reply_to_message.document:
        if message.reply_to_message.document.mime_type == "application/x-tgsticker":
            is_anim = True
            packshortname += "_animated"
            packname += " Animated"
            file_name = await message.reply_to_message.download("AnimatedSticker.tgs")
    else:
        cool = await convert_to_image(message, NEXAUB)
        if not cool:
            return await kang_msg.edit("**Error:** `Unsupported Media`")
        file_name = resize_image(cool)
    try:
        exist = await NEXAUB.send(
            GetStickerSet(
                stickerset=InputStickerSetShortName(
                    short_name=packshortname
                ),
                hash=0
            )
        )
    except StickersetInvalid:
        pass
    if exist:
        try:
            await NEXAUB.send_message("Stickers", "/addsticker")
        except YouBlockedUser:
            await NEXAUB.edit("`Unblocking @Stickers ...`")
            await NEXAUB.unblock_user("Stickers")
            await NEXAUB.send_message("Stickers", "/addsticker")
        await NEXAUB.send_message("Stickers", packshortname)
        await asyncio.sleep(0.2)
        limit = "50" if is_anim else "120"
        messi = (await NEXAUB.get_history("Stickers", 1))[0]
        while limit in messi.text:
            pack += 1
            prev_pack = int(pack) - 1
            await kang_msg.edit(f"He he, Kang Pack Number `{prev_pack}` is Full Of Stickers! Now Switching to `{pack}` Pack!")
            packname = f"@{nm} Kang Pack {pack}"
            packshortname = f"NEXAUB_{message.from_user.id}_{pack}"
            if is_anim:
                packshortname += "_animated"
                packname += " Animated"
            await NEXAUB.send_message("Stickers", packshortname)
            await asyncio.sleep(0.2)
            messi = (await NEXAUB.get_history("Stickers", 1))[0]
            if messi.text == "Invalid pack selected.":
                if is_anim:
                    await NEXAUB.send_message("Stickers", "/newanimated")
                else:
                    await NEXAUB.send_message("Stickers", "/newpack")
                await asyncio.sleep(0.5)
                await NEXAUB.send_message("Stickers", packname)
                await asyncio.sleep(0.2)
                await NEXAUB.send_document("Stickers", file_name)
                await asyncio.sleep(1)
                await NEXAUB.send_message("Stickers", emoji)
                await asyncio.sleep(0.8)
                await NEXAUB.send_message("Stickers", "/publish")
                if is_anim:
                    await NEXAUB.send_message("Stickers", f"<{packname}>")
                await NEXAUB.send_message("Stickers", "/skip")
                await asyncio.sleep(0.5)
                await NEXAUB.send_message("Stickers", packshortname)
                return await kang_msg.edit("**Sticker Kanged!** \n\n**Emoji:** {} \n**Pack:** [Here](https://t.me/addstickers/{})".format(emoji, packshortname))
        await NEXAUB.send_document("Stickers", file_name)
        await asyncio.sleep(1)
        await NEXAUB.send_message("Stickers", emoji)
        await asyncio.sleep(0.5)
        await NEXAUB.send_message("Stickers", "/done")
        await kang_msg.edit("**Sticker Kanged!** \n\n**Emoji:** {} \n**Pack:** [Here](https://t.me/addstickers/{})".format(emoji, packshortname))
    else:
        if is_anim:
            await NEXAUB.send_message("Stickers", "/newanimated")
        else:
            await NEXAUB.send_message("Stickers", "/newpack")
        await NEXAUB.send_message("Stickers", packname)
        await asyncio.sleep(0.2)
        await NEXAUB.send_document("Stickers", file_name)
        await asyncio.sleep(1)
        await NEXAUB.send_message("Stickers", emoji)
        await asyncio.sleep(0.5)
        await NEXAUB.send_message("Stickers", "/publish")
        await asyncio.sleep(0.5)
        if is_anim:
            await NEXAUB.send_message("Stickers", f"<{packname}>")
        await NEXAUB.send_message("Stickers", "/skip")
        await asyncio.sleep(0.5)
        await NEXAUB.send_message("Stickers", packshortname)
        await kang_msg.edit("**Sticker Kanged!** \n\n**Emoji:** {} \n**Pack:** [Here](https://t.me/addstickers/{})".format(emoji, packshortname))
        try:
            if os.path.exists("Kanged_Sticker_NEXAUB.png"):
                os.remove("Kanged_Sticker_NEXAUB.png")
            downname = "./Downloads"
            if os.path.isdir(downname):
                shutil.rmtree(downname)
        except:
            print("Can't remove downloaded sticker files")
            return


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
    file_name = "Kanged_Sticker_NEXAUB.png"
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
