from gpytranslate import Translator
from pyrogram import filters, Client
from pyrogram.types import Message
from handlers.help import *

trl = Translator()




@Client.on_message(filters.me & filters.command("tr", ["."]))
async def translate(client: Client, message: Message):
    trl = Translator()
    if message.reply_to_message and (
        message.reply_to_message.text or message.reply_to_message.caption
    ):
        if len(message.text.split()) == 1:
            await message.delete()
            return
        target = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await message.reply_text(f"Error: `{str(err)}`", parse_mode="Markdown")
            return
    else:
        if len(message.text.split()) <= 2:
            await message.delete()
            return
        target = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
        try:
            tekstr = await trl(text, targetlang=target)
        except ValueError as err:
            await message("Error: `{}`".format(str(err)), parse_mode="Markdown" )
            return
    await message.reply_text(f"**Translated:**\n```{tekstr.text}```\n\n**Detected Language:** `{(await trl.detect(text))}`", parse_mode="Markdown" )


add_command_help(
    "translate",
    [
        [".tr", "Translate some text by give a text or reply that text/caption."],
    ],
)
