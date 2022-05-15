from pyrogram import filters, Client
from pyrogram.errors import YouBlockedUser
from typing import Union
from pyrogram.types import *
from pyrogram.raw.functions.account import ReportPeer
from pyrogram.raw.types import (
    InputPeerUserFromMessage,
    InputReportReasonPornography,
    InputReportReasonSpam,
)


def full_name(user: dict):
    try:
        f_name = " ".join([user.first_name, user.last_name or ""])
    except:
        raise
    return f_name


async def get_response_(msg, filter_user: Union[int, str] = 0, timeout: int = 5, mark_read: bool = False):
    if filter_user:
        try:
            user_ = await client.get_users(filter_user)
        except:
            raise "Invalid user."
    for msg_ in range(1, 6):
        msg_id = msg.message_id + msg_
        try:
            response = await client.get_messages(msg.chat.id, msg_id)
        except:
            raise "No response found."
        if response.reply_to_message.message_id == msg.message_id:
            if filter_user:
                if response.from_user.id == user_.id:
                    if mark_read:
                        await client.send_read_acknowledge(msg.chat.id, response)
                    return response
            else:
                if mark_read:
                    await client.send_read_acknowledge(msg.chat.id, response)
                return response
        
    raise "No response found in time limit."

@Client.on_message(filters.command(["fstats", "fstat"], ["."]) & filters.me)
async def f_stat(client: Client, message: Message):
    """Fstat of user"""
    reply = message.reply_to_message
    user_ = message.input_str if not reply else reply.from_user.id
    if not user_:
        user_ = message.from_user.id
    try:
        get_u = await client.get_users(user_)
        user_name = full_name(get_u)
        user_id = get_u.id
        await message.edit(
            f"Fetching fstat of user <a href='tg://user?id={user_id}'><b>{user_name}</b></a>..."
        )
    except BaseException:
        await message.edit(
            f"Fetching fstat of user <b>{user_}</b>...\nWARNING: User not found in your database, checking Rose's database."
        )
        user_name = user_
        user_id = user_
    bot_ = "MissRose_bot"
    try:
        async with client.conversation(bot_) as conv:
            await client.send_message(f"!fstat {user_id}")
            response = await client.get_response(mark_read=True, filters=filters.edited)
    except YouBlockedUser:
        await message.err("Unblock @missrose_bot first...", del_in=5)
        return
    except Exception as e:
        return await message.edit(f"<b>ERROR:</b> `{e}`")
    fail = "Could not find a user"
    resp = response.text.html
    resp = resp.replace("/fbanstat", f"`{Config.CMD_TRIGGER}fbanstat`")
    if fail in resp:
        await message.edit(
            f"User <b>{user_name}</b> (<code>{user_id}</code>) could not be found in @MissRose_bot's database."
        )
    else:
        await message.edit(resp, parse_mode="html")


@Client.on_message(filters.command(["fbanstat", "fbannedstat"], ["."]) & filters.me)
async def fban_stat(client: Client, message: Message):
    """check fban details"""
    input_ = message.input_str
    reply_ = message.reply_to_message
    if input_:
        split = input_.split()
    else:
        await message.edit("`ERROR: Provide user and FedID...`", del_in=5)
        return
    if len(split) >= 2:
        user = split[0]
        fed_id = split[1]
    elif len(split) == 1:
        if reply_:
            user = reply_.from_user.id
        else:
            user = message.from_user.id
        fed_id = split[0]
    try:
        user_ = await client.get_users(user)
    except BaseException:
        await message.edit(
            f"<b>ERROR:</b> The given user `{user}` is not valid...", del_in=5
        )
        return
    await message.edit("`Fetching fban stats...`")
    user_id = user_.id
    bot_ = "@missrose_bot"
    try:
        query_ = await client.send_message(bot_, f"!fbanstat {user_id} {fed_id}")
    except YouBlockedUser:
        await message.err("Unblock @MissRose_bot first...")
        return
    try:
        response = await gr(query_, timeout=4, mark_read=True)
    except Exception as e:
        await message.err(e)
        return
    fail = "No fed exists"
    resp = response.text
    if fail in resp:
        await message.edit(f"<b>ERROR:</b> Fed `{fed_id}` doesn't exist.")
    else:
        await message.edit(resp.html, parse_mode="html")
