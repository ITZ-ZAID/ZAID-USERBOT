from pyrogram import filters, Client
from pyrogram.types import *





@Client.on_message(filters.commad("plane", ["."]) & filters.me)
async def plane(client: Client, message: Message)
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
