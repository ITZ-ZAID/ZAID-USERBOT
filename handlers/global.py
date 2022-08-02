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

from handlers.help import *
add_command_help(
    "global",
    [
        [".gmute", "To mute someone Globally."],
        [".ungmute", "To Unmute someone Globally."],
        [".gban", "To Ban someone Globally."],
        [".ungmute", "To Unban someone Globally."],
        [".gcast", "To message Globally."],
    ],
)

from handlers import devs_id
from config import SUDO_USERS as AFS

"""
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
"""

@Client.on_message(filters.command("ungmute", ["."]) & filters.me)
async def gmute_him(client, message):
    ug = await message.reply_text("PROCESSING")
    text_ = get_text(message)
    user_ = get_user(message, text_)[0]
    if not user_:
        await ug.edit("REPLY_TO_USER")
        return
    try:
        userz = await client.get_users(user_)
    except BaseException as e:
        await ug.edit(f"USER_MISSING {e}")
        return
    if userz.id == (await client.get_me()).id:
        await ug.edit("TF_DO_IT")
        return
    if userz.id in AFS:
        await ug.edit("`Sudo Users Can't Be Un-Gmutted! Remove Him And Try Again!`")
        return
    if not await is_gmuted(userz.id):
        await ug.edit("`Un-Gmute A Non Gmutted User? Seriously? :/`")
        return
    await ungmute(userz.id)
    ugmu = f"**#Un-Gmutted** \n**User :** `{userz.id}`"
    await ug.edit(ugmu)


@Client.on_message(filters.command("gban", ["."]) & filters.me)
async def gbun_him(client, message):
    gbun = await message.reply_text("PROCESSING")
    text_ = get_text(message)
    user, reason = get_user(message, text_)
    failed = 0
    if not user:
        await gbun.edit("REPLY_TO_USER")
        return
    try:
        userz = await client.get_users(user)
    except BaseException as e:
        await gbun.edit(f"USER_MISSING {e}")
        return
    if not reason:
        reason = "Private Reason!"
    if userz.id == (await client.get_me()).id:
        await gbun.edit("TF_DO_IT")
        return
    if userz.id in devs_id:
        await g.edit("`Sadly, I Can't Do That!`")
        return
    if userz.id in AFS:
        await gbun.edit("`Sudo Users Can't Be Gbanned! Remove Him And Try Again!`")
        return
    if await gban_info(userz.id):
        await gbun.edit("`Re-Gban? Seriously? :/`")
        return
    await gbun.edit("`Please, Wait Fectching Your Users Details!`")
    await gban_user(userz.id, reason)
    gbanned = f"**#GBanned** \n**User :** [{userz.first_name}](tg://user?id={userz.id}) \n**Reason :** `{reason}`"
    await gbun.edit(gbanned)



@Client.on_message(filters.command("ungban", ["."]) & filters.me)
async def ungbun_him(client, message):
    ungbun = await message.reply_text("PROCESSING")
    text_ = get_text(message)
    user = get_user(message, text_)[0]
    failed = 0
    if not user:
        await ungbun.edit("Reply to a user")
        return
    try:
        userz = await client.get_users(user)
    except BaseException as e:
        await ungbun.edit(f"USER_MISSING {e}")
        return
    if userz.id == (await client.get_me()).id:
        await ungbun.edit("TF_DO_IT")
        return
    if not await gban_info(userz.id):
        await ungbun.edit("`Un-Gban A Ungbanned User? Seriously? :/`")
        return
    await ungbun.edit("`Please, Wait Fectching Your Users Details!`")
    await ungban_user(userz.id)
    ungbanned = f"**#Un_GBanned** \n**User :** [{userz.first_name}](tg://user?id={userz.id})"
    await ungbun.edit(ungbanned)

@Client.on_message(filters.command("gbanlist", ["."]) & filters.me)
async def give_glist(client, message):
    oof = "**#GBanList** \n\n"
    glist = await message.reply_text("PROCESSING")
    list_ = await gban_list()
    if len(list_) == 0:
        await glist.edit("`No User is Gbanned Till Now!`")
        return
    for lit in list_:
        oof += f"**User :** `{lit['user']}` \n**Reason :** `{lit['reason']}` \n\n"
    await edit_or_send_as_file(oof, glist, client, "GbanList", "Gban-List")




