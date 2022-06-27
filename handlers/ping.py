#
# Copyright (C) 2021-2022 by Rexoma@Github, < https://github.com/Rexoma >.
#
# This file is part of < https://github.com/Rexoma/SpamBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Rexoma/SpamBot/blob/main/LICENSE >
#
# All rights reserved.

import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from time import time
from datetime import datetime
from config import SUDO_USER

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.user(SUDO_USER) & filters.command(["ping", "on"], [".", "/", "!"]))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.reply_text("`...`")
   delta_ping = time() - start
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m.delete() 
   await m_reply.edit(f"╭━━━╮╱╱╭━╮╭━╮\n┃╭━╮┃╱╱╰╮╰╯╭╯\n┃╰━╯┣━━╮╰╮╭╯╭━━╮\n┃╭╮╭┫┃━┫╭╯╰╮┃╭╮┃\n┃┃┃╰┫┃━╋╯╭╮╰┫╰╯┃\n╰╯╰━┻━━┻━╯╰━┻━━╯\n═══════════════════\n   **Rᴇxᴏᴍᴀ SᴘᴀᴍBᴏᴛ**   \n═══════════════════\n\nMy 🇵 🇮 🇳 🇬  Is : `{delta_ping * 1000:.3f}`")
 
