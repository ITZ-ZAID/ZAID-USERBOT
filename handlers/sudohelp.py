from pyrogram import Client, filters
from pyrogram.types import Message
from main import SUDO_USERS


ZAID_Help = "🔥 Zᴀɪᴅ Sᴜᴅᴏ Uꜱᴇʀꜱ Cᴏᴍᴍᴀɴᴅꜱ 🔥\n\n"
 
ZAID_Help += f"`.banall - To banall in a chat\n `.dm` To Do Private Message\n\n"

ZAID_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

ZAID_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version/total ids \n .`restart` - to restart all spam bots \n `.eval` - Tools for Devs \n `.sh` - installer pkg\n .`.broadcast` to broadcast Message\n\n"
 
ZAID_Help += f" `.inviteall` - To Scrape Active Members Only\n\n"

ZAID_Help += f" `.leave`|`.join` - to leave /Join public/private channel/groups\n\n"
 
ZAID_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"

ZAID_Help += f" `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.fspam` - this cmd use for fast spamming\n`.delayspam` - this cmd use for delay spam\n\n"

ZAID_Help += f"© @Superior_Bots\n"


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help", "commands"], [".", "!", "/"]))
async def help(client: Client, e: Message):
    ids = 0
    try:
        await e.reply_text(photo=ALIVE_PIC, caption=ZAID_Help)
    except Exception as lol:
        await e.reply_photo(photo=ALIVE_PIC, caption=ZAID_Help)
