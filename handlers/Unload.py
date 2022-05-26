from pyrogram import Client, filters
from pyrogram.types import *
from handlers.restarter import restart
import os
module_list = {}

from handlers.help import *


@Client.on_message(filters.command(['unloadmod', "uninstall"], ["."]) & filters.me)
async def unloadmod(client: Client, message: Message):
    try:
        module_name = message.text.replace(f'{prefix}unloadmod', '')
        params = module_name.split()
        module_name = params[0]
        del module_list[module_name]
        file = file_list[module_name]
        os.remove(f'handlers/{file}')
        await message.edit("**The module has been successfully unloaded.**\nRestart...")
        await restart(message, restart_type="restart")
    except Exception as error:
        await message.edit(f"**An error has occurred.**\nLog: not found {error}")



@Client.on_message(filters.command(['loadmod', "install"], ["."]) & filters.me)
async def loadmod(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("<b>Load module...</b>")
        link = message.command[1]
        wget.download(link, 'handlers/')
        await message.edit(
            f"<b>**The module has been loaded successfully.**\nRestart..."
        )
        await restart(message, restart_type="restart")
    else:
        await client.download_media(message.reply_to_message.document, file_name='plugins/')
        await message.edit(
            f"<b>**The module has been loaded successfully.**\nRestart..."
        )
        await restart(message, restart_type="restart")


add_command_help(
    "modules",
    [
        [".uninstall", "To Uninstall A module\n Usage: .uninstall name"],
        [".install", "To install A modules usage:.install reply to plugin file"],
    ],
)
