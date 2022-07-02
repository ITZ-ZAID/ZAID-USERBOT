import re
from pyrogram import filters, Client

from helpers.pyrohelper import get_arg, welcome_chat
import helpers.mongo.welcomedb as Zaid
from main import LOG_GROUP


LOG_CHAT = LOG_GROUP


@Client.on_message(filters.command("clearwelcome", ["."]) & filters.me)
async def welcome(client, message):
    await Zaid.clear_welcome(str(message.chat.id))
    await message.edit("**I am sulking not to say hello anymore :(**")


@Client.on_message(filters.create(welcome_chat) & filters.new_chat_members, group=-2)
async def new_welcome(app: Client, message):
    msg_id = await Zaid.get_welcome(str(message.chat.id))
    caption = ""
    men = ""
    msg = await app.get_messages(LOG_CHAT, msg_id)
    if msg.media:
        if msg.caption:
            caption = msg.caption
            if "{mention}" in caption:
                men = caption.replace("{mention}", "[{}](tg://user?id={})")
        if msg.photo and caption is not None:
            await app.send_photo(
                message.chat.id,
                msg.photo.file_id,
                caption=men.format(
                    message.new_chat_members[0]["first_name"],
                    message.new_chat_members[0]["id"],
                ),
                reply_to_message_id=message.message_id,
            )
        if msg.animation and caption is not None:
            await app.send_animation(
                message.chat.id,
                msg.animation.file_id,
                caption=men.format(
                    message.new_chat_members[0]["first_name"],
                    message.new_chat_members[0]["id"],
                ),
                reply_to_message_id=message.message_id,
            )
        if msg.sticker:
            await app.send_sticker(
                message.chat.id,
                msg.sticker.file_id,
                reply_to_message_id=message.message_id,
            )

    else:
        text = msg.text
        if "{mention}" in text:
            men = text.replace("{mention}", "[{}](tg://user?id={})")
            await app.send_message(
                message.chat.id,
                men.format(
                    message.new_chat_members[0]["first_name"],
                    message.new_chat_members[0]["id"],
                ),
                reply_to_message_id=message.message_id,
            )
        else:
            await app.send_message(
                message.chat.id, text, reply_to_message_id=message.message_id
            )


@Client.on_message(filters.command("setwelcome", ["."]) & filters.me)
async def setwelcome(app: Client, message):
    reply = message.reply_to_message
    if not reply:
        await message.edit("**Reply to a message or media to set welcome message.**")
        return
    frwd = await app.copy_message(LOG_CHAT, message.chat.id, reply.message_id)
    msg_id = frwd.message_id
    await Zaid.save_welcome(str(message.chat.id), msg_id)
    await message.edit("**Welcome message has been saved.**")


from handlers.help import *


add_command_help(
    "welcome",
    [
        [".clearwelcome", " -> Disables welcome message in the chat."],
        [".setwelcome [keyword]", " -> Sets a custom welcome message."],
    ],
)
