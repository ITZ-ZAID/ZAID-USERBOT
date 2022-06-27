# Own

from pyrogram.types import Message
import asyncio
import time
from pyrogram import filters, Client
from config import SUDO_USERS as SUDO_USER
from main import *


@Client.on_message(filters.user(SUDO_USER) & filters.command(["delspam", "deletespam"], [","]))
async def delspam(client: Client, message: Message):
    zaid = await message.reply_text("⚡ Usage:\n /delspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        await zaid.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)


@Client.on_message(filters.user(SUDO_USER) & filters.command(["spam", "spamming"], [","]))
async def suspam(client: Client, message: Message):
    zaid = await message.reply_text("⚡ Usage:\n /spam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await zaid.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(filters.user(SUDO_USER) & filters.command(["fastspam"], [","]))
async def spspam(client: Client, message: Message):
    zaid = await message.reply_text("⚡ Usage:\n /fastspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.002)
        return
    
    for _ in range(quantity):
        await zaid.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.002)



@Client.on_message(filters.user(SUDO_USER) & filters.command(["slowspam", "delayspam"], [","]))
async def sperm(client: Client, message: Message):
    zaid = await message.reply_text("⚡ Usage:\n /slowspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        await zaid.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)







@Client.on_message(filters.user(SUDO_USER) & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [","]))
async def pussy(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return
    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if umm.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)



@Client.on_message(filters.user(SUDO_USER) & filters.command(["alive", "awake"], [","]))
async def awake(client: Client, e: Message):
    ids = 0
    try:
        if bot:
            ids += 1
        if bot1:
            ids += 1
        if bot2:
            ids += 1
        if bot3:
            ids += 1
        if bot4:
            ids += 1
        if bot5:
            ids += 1
        if bot6:
            ids += 1
        if bot7:
            ids += 1
        if bot8:
            ids += 1
        if bot9:
            ids += 1
        if bot:
            ids += 1
        if bot11:
            ids += 1
        if bot12:
            ids += 1
        if bot13:
            ids += 1
        if bot14:
            ids += 1
        if bot15:
            ids += 1
        if bot16:
            ids += 1
        if bot17:
            ids += 1
        if bot18:
            ids += 1
        if bot19:
            ids += 1
        if bot20:
            ids += 1
        if bot21:
            ids += 1
        if bot22:
            ids += 1
        if bot23:
            ids += 1
        if bot24:
            ids += 1
        if bot25:
            ids += 1
        if bot26:
            ids += 1
        if bot27:
            ids += 1
        if bot28:
            ids += 1
        if bot29:
            ids += 1
        if bot30:
            ids += 1
        if bot31:
            ids += 1
        if bot32:
            ids += 1
        if bot33:
            ids += 1
        if bot34:
            ids += 1
        if bot35:
            ids += 1
        if bot36:
            ids += 1
        if bot37:
            ids += 1
        if bot38:
            ids += 1
        if bot39:
            ids += 1
        if bot40:
            ids += 1
        if bot41:
            ids += 1
        if bot42:
            ids += 1
        if bot43:
            ids += 1
        if bot44:
            ids += 1
        if bot45:
            ids += 1
        if bot46:
            ids += 1
        if bot47:
            ids += 1
        if bot48:
            ids += 1
        if bot49:
            ids += 1
        if bot50:
            ids += 1
        Alive_msg = f"𝐙𝐚𝐢𝐝 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/Superior_Support) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_text(photo=ALIVE_PIC, caption=Alive_msg)
    except Exception as lol:         
        Alive_msg = f"𝐙𝐚𝐢𝐝 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ](https://t.me/Superior_Support) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(photo=ALIVE_PIC, caption=Alive_msg)


@Client.on_message(filters.command("ping", [","]) & filters.user(SUDO_USER))
async def pingme(client: Client, message: Message):
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"🎉 🇵 🇴 🇳 🇬 !\n\n♡︎ `{delta_ping * 1000:.3f}` 𝗺𝘀 ♡︎")




@Client.on_message(filters.command(["broadcast", "br", "chatbroadcast"], [","]) & filters.user(SUDO_USER))
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


ZAID_Help = f"🔥 Zᴀɪᴅ Sᴜᴅᴏ Uꜱᴇʀꜱ Cᴍᴅꜱ 🔥\n\n"
ZAID_Help += f"`.banall - To banall in a chat\n `.dm` To Do Private Message\n\n"
ZAID_Help += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"
ZAID_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version/total ids \n .`restart` - to restart all spam bots \n `.eval` - Tools for Devs \n `.sh` - installer pkg\n .`.broadcast` to broadcast Message\n\n"
ZAID_Help += f" `.inviteall` - To Scrape Active Members Only\n\n"
ZAID_Help += f" `.leave`|`.join` - to leave /Join public/private channel/groups\n\n"
ZAID_Help += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"
ZAID_Help += f" `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.fspam` - this cmd use for fast spamming\n`.delayspam` - this cmd use for delay spam\n\n"
ZAID_Help += f"© @Superior_Bots\n"

@Client.on_message(filters.user(SUDO_USER) & filters.command(["help", "command"], [","]))
async def helpsx(client: Client, e: Message):
    ids = 0
    try:
        if bot:
            ids += 1
        if bot1:
            ids += 1
        if bot2:
            ids += 1
        Alive_msg = f"𝐙𝐚𝐢𝐝 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/Superior_Support) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_text(photo=ALIVE_PIC, caption=ZAID_Help)
    except Exception as lol:         
        Alive_msg = f"𝐙𝐚𝐢𝐝 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ](https://t.me/Superior_Support) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(photo=ALIVE_PIC, caption=ZAID_Help)




@Client.on_message(filters.command('join', [","]) & filters.user(SUDO_USER))
async def fuck(client: Client, message: Message):
    zaid = message.text[6:]
    count = 0
    if not zaid:
        return await message.reply_text("Need a chat username or invite link to join.")
    if zaid.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(zaid)
        await message.reply_text(f"**Joined**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command('leave', [","]) & filters.user(SUDO_USER))
async def leftfuck(client: Client, message: Message):
    zaid = message.text[6:]
    count = 0
    if not zaid:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if zaid.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(zaid)
        await message.reply_text(f"**Lefted**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
