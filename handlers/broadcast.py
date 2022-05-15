from pyrogram import Client , filters
import asyncio
from pyrogram.types import Message
from io import BytesIO, StringIO
from handlers.help import add_command_help


@Client.on_message(filters.command(["chatbroadcast", "broadcast", "br"], ".") & filters.me)
async def chat_broadcast(c: Client, m: Message):
    if m.reply_to_message:
        msg = m.reply_to_message.text.markdown
    else:
        await m.reply_text("Reply to a message to broadcast it")
        return

    exmsg = await m.reply_text("Started broadcasting!")
    err_str, done_broadcast = "", 0

    async for dialog in c.iter_dialogs():
          try:
                await c.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done_broadcast += 1
                await asyncio.sleep(0.1)
          except Exception as e:
            await m.reply_text(f"[Broadcast] {dialog.chat.id} {e}")


add_command_help(
    "broadcast",
    [
        [".broadcast", "Give a Message to Broadcast It."],
        ["/broadcast", "Give a message to Broadcast (Sudo-Users)."],
    ],
)
