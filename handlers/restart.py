import platform
import re
import socket
import sys
import time
import uuid
from datetime import datetime
from os import environ, execle, path, remove

import psutil
from pyrogram import __version__
from pyrogram import filters, Client
from pyrogram.types import Message


@Client.on_message(filters.command("restart", ["."]) & filters.me)
async def reboot(client: Client, message: Message):
    await message.edit_text("` Restarting... 🤯🤯`")
    args = [sys.executable, "main.py"]
    execle(sys.executable, *args, environ)
    exit()
    return
