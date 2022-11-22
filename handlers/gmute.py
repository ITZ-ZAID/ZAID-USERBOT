from pyrogram import filters, Client
from pyrogram.types import Message

from helpers.mongo.gbandb import gban_info, gban_list, gban_user, ungban_user
from helpers.mongo.gmutedb import gmute, is_gmuted, ungmute
from helpers.basic_helpers import (
    edit_or_reply,
    edit_or_send_as_file,
    get_text,
    get_user,
    iter_chats,
)

from handlers import devs_id
from config import SUDO_USERS as AFS


@Client.on_message(filters.command("gmute", ["."]) & filters.me)
async def gmute_him(client, message):
    g = await message.reply_text("PROCESSING")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    if not user:
        await g.edit("REPLY_TO_USER")
        return
    try:
        userz = await client.get_users(user)
    except:
        await g.edit("User Doesn't Exists In This Chat !")
        return
    if not reason:
        reason = "Just_Gmutted!"
    if userz.id == (await client.get_me()).id:
        await g.edit("TF_DO_IT")
        return
    if userz.id in devs_id:
        await g.edit("`Sadly, I Can't Do That!`")
        return
    if userz.id in AFS:
        await g.edit("`Sudo Users Can't Be Gmutted! Remove Him And Try Again!`")
        return
    if await is_gmuted(userz.id):
        await g.edit("`Re-Gmute? Seriously? :/`")
        return
    await gmute(userz.id, reason)
    gmu = f"**#Gmutted** \n**User :** `{userz.id}` \n**Reason :** `{reason}`"
    await g.edit(gmu)
