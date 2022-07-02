from pyrogram import filters, Client

from helpers.mongo.gmutedb import get_gmuted_users, gmute_user, ungmute_user
from helpers.mongo.gbandb import *
from helpers.pyrohelper import get_arg
from helpers.adminhelpers import CheckAdmin
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

@Client.on_message(filters.command("ungmute", ["."]) & filters.me)
async def gmute(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I ungmute?**")
            return
    get_user = await app.get_users(user)
    await ungmute_user(get_user.id)
    await message.edit(f"**Unmuted {get_user.first_name}, enjoy!**")

@Client.on_message(filters.command("gban", ["."]) & filters.me)
async def gban(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I gban?**")
            return
    get_user = await app.get_users(user)
    await gban_user(get_user.id)
    await message.edit(f"**Successfully Gbanned {get_user.first_name}!**")


@Client.on_message(filters.command("ungban", ["."]) & filters.me)
async def gbam(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I ungban?**")
            return
    get_user = await app.get_users(user)
    await ungban_user(get_user.id)
    await message.edit(f"**Ungbanned {get_user.first_name}, enjoy!**")


@Client.on_message(filters.group & filters.incoming)
async def check_and_del(app: Client, message):
    if not message:
        return
    try:
        if not message.from_user.id in (await get_gmuted_users()):
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await app.delete_messages(message.chat.id, message_id)
    except:
        pass

@Client.on_message(filters.group & filters.incoming)
async def check_and_del(app: Client, message):
    if not message:
        return
    try:
        if not message.from_user.id in (await get_gban_users()):
            return
    except AttributeError:
        return
    try:
        await app.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    except:
        pass
