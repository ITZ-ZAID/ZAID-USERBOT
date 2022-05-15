import asyncio
import os

from gtts import gTTS
from pyrogram import filters, Client
from pyrogram.types import Message
from handlers.help import add_command_help


__MODULE__ = "Voice"
__HELP__ = """
Convert text to voice chat.

──「 **Voice** 」──
-> `voice (text)`
Convert text to voice by google 

──「 **Voice Language** 」──
-> `voicelang (lang_id)`
Set language of your voice,Some Available Voice lang:
`ID| Language  | ID| Language`
`af: Afrikaans | ar: Arabic
cs: Czech     | de: German  
el: Greek     | en: English
es: Spanish   | fr: French  
hi: Hindi     | id: Indonesian
is: Icelandic | it: Italian
ja: Japanese  | jw: Javanese
ko: Korean    | la: Latin   
my: Myanmar   | ne: Nepali  
nl: Dutch     | pt: Portuguese
ru: Russian   | su: Sundanese 
sv: Swedish   | th: Thai 
tl: Filipino  | tr: Turkish
vi: Vietname  |
zh-cn: Chinese (Mandarin/China)
zh-tw: Chinese (Mandarin/Taiwan)`
"""
lang = "en"  # Default Language for voice


@Client.on_message(filters.me & filters.command(["voice"], ["."]))
async def voice(client: Client, message):
    global lang
    cmd = message.command
    if len(cmd) > 1:
        v_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        v_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("Usage: `reply to a message or send text arg to convert to voice`")
        await asyncio.sleep(2)
        await message.delete()
        return
    await client.send_chat_action(message.chat.id, "record_audio")
    # noinspection PyUnboundLocalVariable
    tts = gTTS(v_text, lang=lang)
    tts.save('handlers/cache/voice.mp3')
    await message.delete()
    if message.reply_to_message:
        await client.send_voice(message.chat.id, voice="nana/cache/voice.mp3",
                                reply_to_message_id=message.reply_to_message.message_id)
    else:
        await client.send_voice(message.chat.id, voice="nana/cache/voice.mp3")
    await client.send_chat_action(message.chat.id, action="cancel")
    os.remove("handlers/cache/voice.mp3")


@Client.on_message(filters.me & filters.command(["voicelang"], ["."]))
async def voicelang(client: Client, message: Message):
    global lang
    temp = lang
    lang = message.text.split(None, 1)[1]
    try:
        gTTS("tes", lang=lang)
    except Exception as e:
        await message.edit("Wrong Language id !")
        lang = temp
        return
    await message.edit("Language Set to {}".format(lang))


add_command_help(
    "Voice",
    [
        [".voice (text)", "Convert text to voice by google."],
        [
            ".voicelang (lang_id) ",
            "Set language of your voice,Some Available Voice lang:"
            "ID| Language  | ID| Language"
            "af: Afrikaans | ar: Arabic"
            "cs: Czech     | de: German"
            "el: Greek     | en: English"
            "es: Spanish   | fr: French"  
            "hi: Hindi     | id: Indonesian"
            "is: Icelandic | it: Italian"
            "ja: Japanese  | jw: Javanese"
            "ko: Korean    | la: Latin"   
            "my: Myanmar   | ne: Nepali"  
            "nl: Dutch     | pt: Portuguese"
            "ru: Russian   | su: Sundanese"
            "sv: Swedish   | th: Thai"
            "tl: Filipino  | tr: Turkish"
            "vi: Vietname  |"
            "zh-cn: Chinese (Mandarin/China)"
            "zh-tw: Chinese (Mandarin/Taiwan)",
        ],
    ],
)
