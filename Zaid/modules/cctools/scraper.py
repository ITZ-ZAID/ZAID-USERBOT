from os import remove
from re import findall

from pyrogram import Client, filters

from Zaid import SUDO_USER


_SCRTXT = """
**✅ CC Scrapped Successfully!**

**Source ->** {}
**Amount ->** {}
**Skipped ->** {}
**Cc Found ->** {}


🥷 **Scrapped By ->** {}
👨‍🎤 **Developed By ->** @TheUpdatesChannel 🐲
"""


@Client.on_message(
    filters.command(["scrape"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def cc_scraper(c, m):
    txt = ""
    skp = 0
    spl = m.text.split(" ")
    e3 = await m.reply_text("...", quote=True)
    if not spl:
        return await e3.edit("full cmd de vai.. 😔")
    elif len(spl) == 2:
        _chat = spl[1].strip()
        limit = 100
    elif len(spl) > 2:
        _chat = spl[1].strip()
        try:
            limit = int(spl[2].strip())
        except ValueError:
            return await e3.edit("No. of card to Scrape must be Integer!")

    await e3.edit(f"`Scrapping from {_chat}. \nHold your Horses...`")
    _get = lambda m: getattr(m, "text", 0) or getattr(m, "caption", 0)
    _getcc = lambda m: list(filter(bool, findall("\d{16}\|\d{2,4}\|\d{2,4}\|\d{2,4}", m)))

    async for x in c.get_chat_history(_chat, limit=limit):
        if not (text := _get(x)):
            skp += 1
            continue
        if not (cc := _getcc(text)):
            skp += 1
        else:
            txt += "\n".join(cc) + "\n"

    cap = _SCRTXT.format(
        _chat,
        str(limit),
        str(skp),
        str(txt.count("\n")),
        m.from_user.mention,
    )
    file = f"x{limit} CC Scrapped by ZaidUB.txt"
    with open(file, "w+") as f:
        f.write(txt)
    del txt
    y = await c.send_document(
        m.chat.id,
        file,
        caption=cap,
        reply_to_message_id=m.id,
    )
    remove(file)
    await e3.delete()
