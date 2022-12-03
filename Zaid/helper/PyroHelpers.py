from pyrogram.types import Message, User
from pyrogram import Client, enums

async def get_ub_chats(
    client: Client,
    chat_types: list = [
        enums.ChatType.GROUP,
        enums.ChatType.SUPERGROUP,
        enums.ChatType.CHANNEL,
    ],
    is_id_only=True,
):
    ub_chats = []
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types:
            if is_id_only:
                ub_chats.append(dialog.chat.id)
            else:
                ub_chats.append(dialog.chat)
        else:
            continue
    return ub_chats

def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id


def SpeedConvert(size):
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kbit/s", 2: "Mbit/s", 3: "Gbit/s", 4: "Tbit/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


def GetFromUserID(message: Message):
    return message.from_user.id


def GetChatID(message: Message):
    return message.chat.id


def GetUserMentionable(user: User):
    if user.username:
        username = "@{}".format(user.username)
    else:
        if user.last_name:
            name_string = "{} {}".format(user.first_name, user.last_name)
        else:
            name_string = "{}".format(user.first_name)

        username = "<a href='tg://user?id={}'>{}</a>".format(user.id, name_string)

    return username
