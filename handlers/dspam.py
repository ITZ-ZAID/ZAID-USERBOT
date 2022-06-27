import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
 
 
@Client.on_message(filters.command("dspam") & filters.me)
async def delayspam_handler(app: Client, m: Message):
    try:
        reply = m.reply_to_message
        m.command
 
        if app.long(m) < 3:
            await app.send_edit(
                m,
                f"use as: .delayspam [conut] [ time in sec ] [text]",
            )
 
        elif app.long(m) > 2 and not reply:
            await m.delete()
            msg = m.text.split(None, 3)
            times = int(msg[1]) if msg[1].isdigit() else None
            sec = int(msg[2]) if msg[2].isdigit() else None
            text = msg[3]
            for x in range(times):
                await app.send_message(m.chat.id, text)
                await asyncio.sleep(sec)
        else:
            await app.send_edit(m, "something wrong")
    except Exception as e:
        await app.error(m, e)
