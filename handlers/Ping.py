import time

from pyrogram import filters, Client
from pyrogram.types import Message
from config import SUDO_USERS 

@Client.on_message(filters.command("ping", ".") & filters.me)
async def ping(client: Client, msg: Message):
    st = time.time()
    et = time.time()
    delta_ping = time.time() - start    
    mention = msg.from_user.mention
    uptime = f"\n`{round((et - st), 3)} ms`"
    textt = """
★°:･✧*.°☆.*★°●¸★　 
▃▃▃▃▃▃▃▃▃▃▃
┊ ┊ ┊ ┊ ┊ ┊┊
┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩
┊ ┊ ┊ ┊⍣∙°⚝○｡°✯
┊ ┊ ┊ ┊
┊ ┊ ┊ ⛦『P‌๏‌и‌ɠ‌』 
┊ ┊ ┊︎✫ ˚♡ ⋆˚ ⋆｡ ❀
┊ ┊ ┊
┊ ┊ ┊𓆩𝙈𝙎--≻{delta_ping * 1000:.3f} ﮩ٨ـﮩﮩ٨ـ𓆪
┊ ┊ ✯
┊ ✬ ˚•˚✩
┊⍣ •°
┊亗•ʍʏ ๏ωиэя•亗
★• {} •
⚘ Zαιԃ UʂҽɾႦσƚ ⚘
""".format(uptime, mention)
    await msg.edit(textt)
