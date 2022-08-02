from pyrogram import filters, Client

from helpers.mongo.gmutedb import get_gmuted_users, gmute_user, ungmute_user
from helpers.mongo.gbandb import *
from helpers.pyrohelper import get_arg
from helpers.adminhelpers import CheckAdmin

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
    except Exception as e:
        print(str(e))
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
    except Exception as e:
        print(str(e))
        pass
