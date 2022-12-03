from aiohttp.client_exceptions import ClientError
from pyrogram import filters, Client 
from pyrogram.types import Message


from Zaid.helper.aiohttp_helper import AioHttp
from Zaid.modules.help import add_command_help

cf_api_data = {
    "anime": {
        "url": "https://api.computerfreaker.cf/v1/anime",
        "help": "It works on my machine!",
    },
    "hentai": {
        "url": "https://api.computerfreaker.cf/v1/hentai",
        "help": "Sends a nice compliment.",
    },
    "yuri": {
        "url": "https://api.computerfreaker.cf/v1/yuri",
        "help": "Affirmative messages",
    },
    "dva": {
        "url": "https://api.computerfreaker.cf/v1/dva",
        "help": "Affirmative messages",
    },
    "trap": {
        "url": "https://api.computerfreaker.cf/v1/trap",
        "help": "Affirmative messages",
    },
    "hug": {
        "url": "https://api.computerfreaker.cf/v1/hug",
        "help": "Give it a guess dumbass!",
    },
    "neko": {
        "url": "https://api.computerfreaker.cf/v1/neko",
        "format": "Kanye once said:\n`{}`",
        "help": "Kanye used to say",
    },
    "nsfwneko": {
        "url": "https://api.computerfreaker.cf/v1/nsfwneko",
        "help": "Programmers be like.",
    },
    "baguette": {
        "url": "https://api.computerfreaker.cf/v1/baguette",
        "help": "Affirmative messages",
    },
}

text_api_commands = []
for x in cf_api_data:
    text_api_commands.append(x)
    if "alts" in cf_api_data[x]:
        for y in cf_api_data[x]["alts"]:
            text_api_commands.append(y)


@Client.on_message(
    filters.command(text_api_commands, ".") & filters.me
)
async def hentai_api(bot: Client, message: Message):
    cmd = message.command
    api_key = cmd[0]
    api = cf_api_data[api_key]

    try:
        data = await AioHttp().get_json(api["url"])
        content_url: str = data['url']
        await bot.send_photo(message.chat.id, content_url)
    except ClientError as e:
        print(e)

    await message.delete()



for x in cf_api_data:
    add_command_help(
        "anime_cf",
        [
            [f".{x}", cf_api_data[x]["help"]],
        ],
    )
