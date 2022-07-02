from pyrogram import filters, Client

from helpers.mongo.gmutedb import get_gmuted_users, gmute_user, ungmute_user
from helpers.mongo.gbandb import *
from helpers.pyrohelper import get_arg
from helpers.adminhelpers import CheckAdmin


@Client.on_message(filters.command("gmute", ["."]) & filters.me)
async def gmute(app: Client, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I gmute?**")
            return
    get_user = await app.get_users(user)
    await gmute_user(get_user.id)
    await message.edit(f"**Successfully Taped {get_user.first_name}, This users mouth!**")
