from Zaid.modules.help import add_command_help
import asyncio
import requests
import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message

import os
import re

from pyrogram.types import Message
from httpx import AsyncClient
from Zaid.helper.utility import get_arg


# Pastebins
class PasteBins:
    def __init__(self) -> None:
        # API Urls
        self.nekobin_api = "https://nekobin.com/api/documents"
        self.spacebin_api = "https://spaceb.in/api/v1/documents"
        self.hastebin_api = "https://www.toptal.com/developers/hastebin/documents"
        # Paste Urls
        self.nekobin = "https://nekobin.com"
        self.spacebin = "https://spaceb.in"
        self.hastebin = "https://www.toptal.com/developers/hastebin"
    
    async def paste_text(self, paste_bin, text):
        if paste_bin == "spacebin":
            return await self.paste_to_spacebin(text)
        elif paste_bin == "hastebin":
            return await self.paste_to_hastebin(text)
        elif paste_bin == "nekobin":
            return await self.paste_to_nekobin(text)
        else:
            return "`Invalid pastebin service selected!`"
    
    async def __check_status(self, resp_status, status_code: int = 201):
        if int(resp_status) != status_code:
            return "real shit"
        else:
            return "ok"

    async def paste_to_nekobin(self, text):
        async with AsyncClient() as nekoc:
            resp = await nekoc.post(self.nekobin_api, json={"content": str(text)})
            chck = await self.__check_status(resp.status_code)
            if not chck == "ok":
                return None
            else:
                jsned = resp.json()
                return f"{self.nekobin}/{jsned['result']['key']}"
    
    async def paste_to_spacebin(self, text):
        async with AsyncClient() as spacbc:
            resp = await spacbc.post(self.spacebin_api, data={"content": str(text), "extension": "md"})
            chck = await self.__check_status(resp.status_code)
            if not chck == "ok":
                return None
            else:
                jsned = resp.json()
                return f"{self.spacebin}/{jsned['payload']['id']}"
    
    async def paste_to_hastebin(self, text):
        async with AsyncClient() as spacbc:
            resp = await spacbc.post(self.hastebin_api, data=str(text))
            chck = await self.__check_status(resp.status_code, 200)
            if not chck == "ok":
                return None
            else:
                jsned = resp.json()
                return f"{self.hastebin}/{jsned['key']}"


async def get_pastebin_service(text: str):
    if re.search(r'\bhastebin\b', text):
        pastebin = "hastebin"
    elif re.search(r'\bspacebin\b', text):
        pastebin = "spacebin"
    elif re.search(r'\bnekobin\b', text):
        pastebin = "nekobin"
    else:
        pastebin = "spacebin"
    return pastebin

@Client.on_message(filters.command(["paste", "nekobin", "hastebin", "spacebin"], ["."]) & filters.me)
async def paste_dis_text(_, message: Message):
    pstbin_serv = await get_pastebin_service(message.text.split(" ")[0])
    paste_msg = await message.edit(f"`Pasting to {pstbin_serv.capitalize()}...`")
    replied_msg = message.reply_to_message
    tex_t = get_arg(message)
    message_s = tex_t
    if not tex_t:
        if not replied_msg:
            return await paste_msg.edit("`Reply To File or Send This Command With Text!`")
        if not replied_msg.text:
            file = await replied_msg.download()
            m_list = open(file, "r").read()
            message_s = m_list
            os.remove(file)
        elif replied_msg.text:
            message_s = replied_msg.text
    paste_cls = PasteBins()
    pasted = await paste_cls.paste_text(pstbin_serv, message_s)
    if not pasted:
        return await paste_msg.edit("`Oops, Pasting failed! Please try changing the pastebin service!`")
    await paste_msg.edit(f"**Pasted to {pstbin_serv.capitalize()}!** \n\n**Url:** {pasted}", disable_web_page_preview=True)

add_command_help(
    "paste",
    [
        [
            ".paste `or` .nekobin `or` .hastebin `or` .spacebin",
            "To Paste Text to Hastebin / Nekobin or Spacebin \n\nCreate a Nekobin paste using replied to message.",
        ],
    ],
)
