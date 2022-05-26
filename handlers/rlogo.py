import os
import wget
import random

from handlers.help import *
from pyrogram import Client, filters
from pyrogram.types import *
from helpers.basic import edit_or_reply, get_text

from PIL import Image, ImageDraw, ImageFont


def choose_random_font():
    fonts_ = [
        "https://github.com/DevsExpo/FONTS/raw/main/Ailerons-Typeface.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/Toxico.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/againts.otf",
        "https://github.com/DevsExpo/FONTS/raw/main/go3v2.ttf",
        "https://github.com/DevsExpo/FONTS/raw/main/vermin_vibes.ttf",
    ]
    random_s = random.choice(fonts_)
    return wget.download(random_s)


@Client.on_message(filters.command('rlogo', ["."]) & filters.me)
async def rlogo(client: Client, message: Message):
    event = await edit_or_reply(message, "`Processing.....`")
    text = get_text(message)
    if not text:
        await event.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    font_ = choose_random_font()
    img = Image.open("./bot_utils_files/image_templates/black_blank_image.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, 220)
    image_widthz, image_heightz = img.size
    w, h = draw.textsize(text, font=font)
    h += int(h * 0.21)
    draw.text(
        ((image_widthz - w) / 2, (image_heightz - h) / 2),
        text,
        font=font,
        fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    file_name = "LogoBy@Zaid.png"
    await client.send_chat_action(message.chat.id, "upload_photo")
    img.save(file_name, "png")
    if message.reply_to_message:
        await client.send_photo(
            message.chat.id,
            photo=file_name,
            caption="Made Using Zaid Userbot",
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_photo(
            message.chat.id, photo=file_name, caption="Made Using Zaid Userbot"
        )
    await client.send_chat_action(message.chat.id, "cancel")
    await event.delete()
    if os.path.exists(file_name):
        os.remove(file_name)

add_command_help(
    "randomlogo",
    [
        [".rlogo", "To make a random logo."],
    ],
)
