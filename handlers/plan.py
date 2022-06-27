from pyrogram import filters, Client
from pyrogram.types import *
import asyncio





@Client.on_message(filters.command("plane", ["."]) & filters.me)
async def plane(client: Client, message: Message):
    await message.edit("✈-------------")
    await message.edit("-✈------------")
    await message.edit("--✈-----------")
    await message.edit("---✈----------")
    await message.edit("----✈---------")
    await message.edit("-----✈--------")
    await message.edit("------✈-------")
    await message.edit("-------✈------")
    await message.edit("--------✈-----") 
    await message.edit("---------✈----")
    await message.edit("----------✈---")
    await message.edit("-----------✈--")
    await message.edit("------------✈-")
    await message.edit("-------------✈")
    await asyncio.sleep(3)
    await message.delete()
