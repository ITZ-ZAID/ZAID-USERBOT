import asyncio
import os
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message
from telegraph import exceptions, upload_file

from config import BOT_VER, CHANNEL
from config import CMD_HANDLER
from config import GROUP, OWNER_ID
from X import CMD_HELP, StartTime
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import ReplyCheck
from X.helpers.SQL.globals import gvarstatus
from X.helpers.tools import convert_to_image
from X.utils import get_readable_time
from X.utils.misc import restart

from .help import *

modules = CMD_HELP
alivemodules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or ""
)
emoji = gvarstatus("ALIVE_EMOJI") or "✧"
alive_text = gvarstatus("ALIVE_TEKS_CUSTOM") or "✧✧ ⚡ 𝙍𝘼 - 𝙊𝙉𝙀 ⚡  ✧✧"


@Client.on_message(filters.command(["alive", "awake"], cmd) & filters.me)
async def alip(client: Client, message: Message):
    X = await edit_or_reply(message, "❤️")
    await asyncio.sleep(2)
    sad = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"<b>{alive_text}</b>\n\n"
        f"<b>•─╼⃝𖠁 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚄𝚂 </b>\n\n"
        f"{emoji} <b>𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁:</b> [{client.me.mention}](tg://user?id={OWNER_ID}) \n\n"
        f"{emoji} <b>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅𝙴𝚁𝚂𝙸𝙾𝙽:</b> <code>{versipyro}</code>\n"
        f"{emoji} <b>𝙱𝙾𝚃 𝚄𝙿𝚃𝙸𝙼𝙴:</b> <code>{uptime}</code> \n"
        f"{emoji} <b>𝚅𝙴𝚁𝚂𝙸𝙾𝙽:</b> <code>{BOT_VER}</code> \n"
        f"{emoji} <b>𝙼𝙾𝚃𝙴𝚁𝚂:</b> <code>{len(modules)} Modules</code> \n"
        f"{emoji} <b>𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽:</b> <code>{python_version()}</code> \n"
        f"{emoji}✧[𝙶𝚁𝙾𝚄𝙿](https://t.me/+UHHOPOmVTIFhNzA9)** \n" 
        
    )
    try:
      await sad(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            )
      await X.delete()
    except:
      await X.edit(man, disable_web_page_preview=True)


@Client.on_message(filters.command("setalivelogo", cmd) & filters.me)
async def setalivelogo(client: Client, message: Message):
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    X = await edit_or_reply(message, "`Processing...`")
    link = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await X.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        link = f"https://telegra.ph/{media_url[0]}"
        os.remove(m_d)
    sql.addgvar("ALIVE_LOGO", link)
    await X.edit(
        f"**Successfully Customized ALIVE LOGO Become {link}**",
        disable_web_page_preview=True,
    )
    restart()


@Client.on_message(filters.command("setalivetext", cmd) & filters.me)
async def setalivetext(client: Client, message: Message):
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    X = await edit_or_reply(message, "`Processing...`")
    if not text:
        return await edit_or_reply(
            message, "**Give a text or reply to a text**"
        )
    sql.addgvar("ALIVE_TEKS_CUSTOM", text)
    await X.edit(f"**Successfully Customized ALIVE TEXT Become** `{text}`")
    restart()


@Client.on_message(filters.command("setemoji", cmd) & filters.me)
async def setemoji(client: Client, message: Message):
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    emoji = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    X = await edit_or_reply(message, "`Processing...`")
    if not emoji:
        return await edit_or_reply(message, "**Give A Emoji**")
    sql.addgvar("ALIVE_EMOJI", emoji)
    await X.edit(f"**Successfully Customize ALIVE EMOJI Becomes** {emoji}")
    restart()
