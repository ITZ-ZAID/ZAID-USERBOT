from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import *
from pyrogram import Client
ALIVE_PIC = "https://telegra.ph/file/5dd84629f6aeeb91c6e88.jpg"

 
@Client.on_message(filters.command(["alive"]))
async def alive(client: Client, e: Message):
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
        Alive_msg = f"𝐒𝐩𝐚𝐦𝐛𝐨𝐭 𝐢𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠. 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Sᴘᴀᴍʙᴏᴛ ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/Superior_Support) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Superior_Bots")
                ], [
                    InlineKeyboardButton(
                        "• 𝐑𝐞𝐩𝐨 •", url="https://github.com/The-HellBot/ArrayCore")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"𝐒𝐩𝐚𝐦𝐛𝐨𝐭 𝐢𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠. 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Sᴘᴀᴍʙᴏᴛ ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ](https://t.me/Superior_Support) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Superior_Bots"),
                ],
                [
                    InlineKeyboardButton("• 𝐑𝐞𝐩𝐨 •", url="https://github.com/Itz-Zaid/Spam-Userbot"),
                ],
            ],
        ),
    ) 


@Client.on_message(filters.command(["alive", "awake"], ".") & filters.me)
async def alive(client: Client, e: Message):
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
        Alive_msg = f"𝐒𝐩𝐚𝐦𝐛𝐨𝐭 𝐢𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠. 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Sᴘᴀᴍʙᴏᴛ ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/Superior_Support) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Superior_Bots")
                ], [
                    InlineKeyboardButton(
                        "• 𝐑𝐞𝐩𝐨 •", url="https://github.com/The-HellBot/ArrayCore")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"𝐒𝐩𝐚𝐦𝐛𝐨𝐭 𝐢𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠. 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Sᴘᴀᴍʙᴏᴛ ᴠᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.15` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ](https://t.me/Superior_Support) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Superior_Bots"),
                ],
                [
                    InlineKeyboardButton("• 𝐑𝐞𝐩𝐨 •", url="https://github.com/Itz-Zaid/Spam-Userbot"),
                ],
            ],
        ),
    ) 
