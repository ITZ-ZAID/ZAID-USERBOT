import asyncio
import random

from pyrogram import filters, Client
from pyrogram.types import Message

from Zaid.helper.PyroHelpers import ReplyCheck
from Zaid.modules.help import add_command_help

sticker_data = {
    "mock": {
        "value": 7,
        "empty_message": "GiVE ME sOMEThINg TO MOCK",
        "action": "Mocking...",
    },
    "ggl": {
        "value": 12,
        "empty_message": "Senpai, I need something to Google...",
        "action": "Googling...",
    },
    "waifu": {
        "alts": ["ag", "animegirl"],
        "value": [15, 20, 32, 33, 34, 40, 41, 42, 58],
        "empty_message": "The waifu ran away...",
        "action": "Asking my wiafus to say it...",
    },
    "animeboy": {
        "alts": ["ab"],
        "value": [37, 38, 48, 55],
        "empty_message": "Senpai, I need something to say...",
        "action": "The boys are on it...",
    },
}

sticker_commands = []
for x in sticker_data:
    sticker_commands.append(x)
    if "alts" in sticker_data[x]:
        for y in sticker_data[x]["alts"]:
            sticker_commands.append(y)


@Client.on_message(filters.command(sticker_commands, ".") & filters.me)
async def sticker_super_func(bot: Client, message: Message):
    try:
        sticker = {}
        command = message.command[0]
        if command not in sticker_data:
            for sticker in sticker_data:
                if (
                        "alts" in sticker_data[sticker]
                        and command in sticker_data[sticker]["alts"]
                ):
                    sticker = sticker_data[sticker]
                    break
        else:
            sticker = sticker_data[message.command[0]]

        cmd = message.command

        sticker_text = ""
        if len(cmd) > 1:
            sticker_text = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            sticker_text = message.reply_to_message.text
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit(sticker["empty_message"])
            await asyncio.sleep(2)
            await message.delete()
            return

        await message.edit(f"`{sticker['action']}`")

        values = sticker["value"]
        choice = None
        if isinstance(values, list):
            choice = int(random.choice(values))
        elif isinstance(values, int):
            choice = values

        if choice:
            sticker_results = await bot.get_inline_bot_results(
                "stickerizerbot", f"#{choice}" + sticker_text
            )
        else:
            sticker_results = await bot.get_inline_bot_results(
                "stickerizerbot", sticker_text
            )

        try:
            await bot.send_inline_bot_result(
                chat_id=message.chat.id,
                query_id=sticker_results.query_id,
                result_id=sticker_results.results[0].id,
                reply_to_message_id=ReplyCheck(message),
                hide_via=True,
            )
        except TimeoutError:
            await message.edit("`@StickerizerBot didn't respond in time...`")
            await asyncio.sleep(2)
    except Exception:
        await message.edit("`Failed to reach @Stickerizerbot...`")
        await asyncio.sleep(2)
    await message.delete()


add_command_help(
    "stickers",
    [
        [
            ".mock",
            "Sends a Spongebob mocking meme of what you sent with command or text of what you replied to.\n"
            '**Usage**:\n```.mock you smell like shit``` will give you the meme that says "You smell like shit"\n'
            "Reply to a text message with .mock and it will grab the text of that message and generate the meme.",
        ],
        [
            ".animegirl `or` .ag",
            "Sends a random anime girl sticker. Rules apply as above.",
        ],
        [".animeboy `or` .ab", "Sends a random boy sticker. Rules apply as above."],
        [
            ".ggl",
            "Sends google search buttons with the query you give it. Rules apply as above.",
        ],
    ],
)
