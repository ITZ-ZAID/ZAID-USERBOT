import re

from pyrogram import filters, Client
from pyrogram.errors import FloodWait, ChatAdminRequired
from main import LOG_GROUP as LOG_CHAT
from helpers.pyrohelper import get_arg
from helpers.mongo.filtersdb import (
    add_filters,
    all_filters,
    del_filters,
    filters_del,
    filters_info,
)
from helpers.mongo.gbandb import gban_info
from helpers.mongo.gmutedb import is_gmuted

@Client.on_message(filters.command("stop", ["."]) & filters.me)
async def del_filterz(client: Client, message):
    note_ = await message.edit("**Processing..**")
    note_name = get_arg(message)
    if not note_name:
        await note_.edit("**Give A Filter Name!**")
        return
    note_name = note_name.lower()
    if not await filters_info(note_name, int(message.chat.id)):
        await note_.edit("**Filter Not Found!**")
        return
    await del_filters(note_name, int(message.chat.id))
    await note_.edit(f"**Filter `{note_name}` Deleted Successfully!**")


@Client.on_message(filters.command("filters", ["."]) & filters.me)
async def show_filters(client: Client, message):
    pablo = await message.edit("**Processing..**")
    poppy = await all_filters(int(message.chat.id))
    if poppy is False:
        await pablo.edit("**No Filters Found In This Chat...**")
        return
    kk = ""
    for Escobar in poppy:
        kk += f"\n ◍ `{Escobar.get('keyword')}`"
    X = await client.get_chat(int(message.chat.id))
    grp_nme = X.title
    mag = f"List Of Filters In {grp_nme}: \n{kk}"
    await pablo.edit(mag)


@Client.on_message(filters.command("filter", ["."]) & filters.me)
async def s_filters(app: Client, message):
    note_ = await message.edit("**Processing..**")
    note_name = get_arg(message)
    if not note_name:
        await note_.edit("**Give A Filter Name!**")
        return
    if not message.reply_to_message:
        await note_.edit("Reply To Message To Save As Filter!")
        return
    note_name = note_name.lower()
    msg = message.reply_to_message
    copied_msg = await msg.copy(int(LOG_CHAT))
    await add_filters(note_name, int(message.chat.id), copied_msg.message_id)
    await note_.edit(f"**Done! `{note_name}` Added To Filters List!**")


@Client.on_message(
    filters.incoming & ~filters.edited & filters.group & ~filters.private & ~filters.me,
    group=3,
)
async def filter_s(client: Client, message):
    owo = message.text
    al_fill = []
    is_m = False
    if not owo:
        return
    user = message.from_user.id
    if await is_gmuted(user):
        try:
            await message.delete()
        except:
            return
    if await gban_info(user):
        if message.chat.type == "private":
            return
        try:
            await message.chat.ban_member(user)
            await message.reply_text(f"👮🏼 **Gbanned** user detected.")
        except ChatAdminRequired:
            print(f"can't remove gbanned user from chat: {message.chat.id}")
            return
    al_fil = await all_filters(int(message.chat.id))
    if not al_fil:
        return
    for all_fil in al_fil:
        al_fill.append(all_fil.get("keyword"))
    owoo = owo.lower()
    for filter_s in al_fill:
        pattern = r"( |^|[^\w])" + re.escape(filter_s) + r"( |$|[^\w])"
        if re.search(pattern, owo, flags=re.IGNORECASE):
            f_info = await filters_info(filter_s, int(message.chat.id))
            m_s = await client.get_messages(int(LOG_CHAT), f_info["msg_id"])
            if await is_media(m_s):
                text_ = m_s.caption or ""
                is_m = True
            else:
                text_ = m_s.text or ""
            if text_ != "":
                mention = message.from_user.mention
                user_id = message.from_user.id
                user_name = message.from_user.username or "No Username"
                first_name = message.from_user.first_name
                last_name = message.from_user.last_name or "No Last Name"
                text_ = text_.format(
                    mention=mention,
                    user_id=user_id,
                    user_name=user_name,
                    first_name=first_name,
                    last_name=last_name,
                )
            if not is_m:
                await client.send_message(
                    message.chat.id, text_, reply_to_message_id=message.message_id
                )
            else:
                await m_s.copy(
                    chat_id=int(message.chat.id),
                    caption=text_,
                    reply_to_message_id=message.message_id,
                )


async def is_media(message):
    if not (
        message.photo
        or message.video
        or message.document
        or message.audio
        or message.sticker
        or message.animation
        or message.voice
        or message.video_note
    ):
        return False
    return True


@Client.on_message(filters.command("stopall", ["."]) & filters.me)
async def del_all_filters(client: Client, message):
    pablo = await message.edit("**Processing..**")
    poppy = await all_filters(int(message.chat.id))
    if poppy is False:
        await pablo.edit("**No Filters Found In This Chat...**")
        return
    await filters_del(int(message.chat.id))
    await pablo.edit("**Deleted All The Filters Successfully!!**")


from handlers.help import *


add_command_help(
    "filters",
    [
        [".filters", " -> List all active filters in current chat.."],
        [".filter [keyword]", " -> Saves a filter."],
        [".stop [keyword]", "-> Stops a filter."],
        [".clearall", " -> Deletes all the saved notes."],
        [".stopall", " -> Removes all the filters in the chat."],

    ],
)
