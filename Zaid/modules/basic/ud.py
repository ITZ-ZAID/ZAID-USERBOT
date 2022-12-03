from asyncio import sleep

from pyrogram import filters, Client 


from Zaid.helper.aiohttp_helper import AioHttp
from Zaid.modules.help import add_command_help


def replace_text(text):
    return text.replace('"', "").replace("\\r", "").replace("\\n", "").replace("\\", "")


@Client.on_message(filters.me & filters.command(["ud"], "."))
async def urban_dictionary(bot, message):
    if len(message.text.split()) == 1:
        await message.edit("Usage: `ud example`")
        return
    try:
        text = message.text.split(None, 1)[1]
        response = await AioHttp().get_json(
            f"http://api.urbandictionary.com/v0/define?term={text}"
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        resp = (
            f"**Text: {replace_text(word)}**\n"
            f"**Meaning:**\n`{replace_text(definition)}`\n\n"
            f"**Example:**\n`{replace_text(example)}` "
        )
        await message.edit(resp)
        return
    except Exception as e:
        await message.edit("`The Urban Dictionary API could not be reached`")
        print(e)
        await sleep(3)
        await message.delete()



add_command_help(
    "dictionary",
    [
        [".ubran | .ud", "Define the word you send or reply to."],
    ],
)
