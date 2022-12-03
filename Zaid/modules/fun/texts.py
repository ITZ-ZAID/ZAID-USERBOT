import asyncio
import re
from random import choice, randint

import uwuify
from pyrogram import filters, Client
from pyrogram.types import Message

from Zaid.helper.PyroHelpers import GetUserMentionable
from Zaid.helper.aiohttp_helper import AioHttp
from Zaid.helper.constants import Fs, MEMES, Weebify
from Zaid.helper.utility import get_mock_text
from Zaid.modules.help import add_command_help


@Client.on_message(filters.command("lorem", ".") & filters.me)
async def lorem(bot: Client, message: Message):
    response = await AioHttp().get_text('https://loripsum.net/api/plaintext')
    await message.edit(response)


@Client.on_message(filters.command("nice", ".") & filters.me)
async def nice(bot: Client, message: Message):
    await message.edit("NICENICENICENICE")


@Client.on_message(filters.command("reverse", ".") & filters.me)
async def reverse(bot: Client, message: Message):
    await message.edit(
        text=MEMES.REVERSE,
    )


@Client.on_message(filters.command("cock", ".") & filters.me)
async def cock(bot: Client, message: Message):
    await message.edit(
        text=MEMES.COCK,
    )


@Client.on_message(filters.command("slap", ".") & filters.me)
async def slap(bot: Client, message: Message):
    if message.reply_to_message is None:
        await message.edit(
            "`WHO SHOULD I SLAP?`"
        )
        await asyncio.sleep(5)
        await message.delete()
        return
    else:
        replied_user = message.reply_to_message.from_user

        if message.from_user.id is replied_user.id:
            return

        slapped = GetUserMentionable(replied_user)

        temp = choice(MEMES.SLAP_TEMPLATES)
        item = choice(MEMES.ITEMS)
        hit = choice(MEMES.HIT)
        throw = choice(MEMES.THROW)
        where = choice(MEMES.WHERE)

        caption = temp.format(
            victim=slapped, item=item, hits=hit, throws=throw, where=where
        )

        try:
            await message.edit(caption)
        except Exception:
            await message.edit(
                "`Can't slap this person, need to fetch some sticks and stones!!`"
            )


@Client.on_message(
    (filters.command("-_-", "") | filters.command("ok", ".")) & filters.me
)
async def ok(bot: Client, message: Message):
    okay = "-_-"
    for _ in range(10):
        okay = okay[:-1] + "_-"
        await message.edit(okay, parse_mode=None)


@Client.on_message(
    (filters.command(";_;", "") | filters.command(["sad", "cri"], ".")) & filters.me
)
async def sad_cri(bot: Client, message: Message):
    cri = ";_;"
    for _ in range(10):
        cri = cri[:-1] + "_;"
        await message.edit(cri, parse_mode=None)


@Client.on_message(filters.regex(r"^\.?oof$") & filters.me)
async def send_oof(bot: Client, message: Message):
    oof = "Oo "
    for _ in range(10):
        oof = oof[:-1] + "of"
        await message.edit(oof, parse_mode=None)


@Client.on_message(filters.command("mockt", ".") & filters.me)
async def mock_text(bot: Client, message: Message):
    cmd = message.command

    mock_t = ""
    if len(cmd) > 1:
        mock_t = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        mock_t = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("I need something to mock")
        await asyncio.sleep(2)
        await message.delete()
        return

    input_str = mock_t
    if not input_str:
        await message.edit("`gIvE sOMEtHInG tO MoCk!`")
        return

    reply_text = get_mock_text(input_str.lower())

    await message.edit(reply_text)


@Client.on_message(filters.command("brain", ".") & filters.me)
async def brain(bot: Client, message: Message):
    for x in MEMES.BRAIN:
        await asyncio.sleep(0.35)
        await message.edit(x)


@Client.on_message(filters.command("f", ".", case_sensitive=True) & filters.me)
async def pay_respects(bot: Client, message: Message):
    await message.edit(Fs().F)


@Client.on_message(filters.command("F", ".", case_sensitive=True) & filters.me)
async def pay_respects_new(bot: Client, message: Message):
    await message.edit(Fs.BIG_F)


@Client.on_message(filters.command("f", "#") & filters.me)
async def calligraphic_f(bot: Client, message: Message):
    await message.edit(Fs.FANCY_F)


def uwu(raw_text):
    flags = uwuify.SMILEY | uwuify.YU
    text = uwuify.uwu(raw_text, flags=flags)
    return text


@Client.on_message(filters.command(["uwu", "uwuify"], ".") & filters.me)
async def weebify(bot: Client, message: Message):
    cmd = message.command

    raw_text = ""
    if len(cmd) > 1:
        raw_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        raw_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit(f"`{weebify_text('Could not uwuify...')}`")
        await asyncio.sleep(2)
        await message.delete()
        return

    await message.edit(uwu(raw_text))


def weebify_text(raw_text):
    for normie_char in raw_text:
        if normie_char in Weebify.NORMIE_FONT:
            weeby_char = Weebify.WEEBY_FONT[Weebify.NORMIE_FONT.index(normie_char)]
            raw_text = raw_text.replace(normie_char, weeby_char)
    return raw_text


@Client.on_message(filters.command(["weeb", "weebify"], ".") & filters.me)
async def weebify(bot: Client, message: Message):
    cmd = message.command

    raw_text = ""
    if len(cmd) > 1:
        raw_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        raw_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit(f"`{weebify_text('Could not weebify...')}`")
        await asyncio.sleep(2)
        await message.delete()
        return

    await message.edit(weebify_text(raw_text))


@Client.on_message(filters.command("vapor", ".") & filters.me)
async def vapor(bot: Client, message: Message):
    cmd = message.command

    vapor_text = ""
    if len(cmd) > 1:
        vapor_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        vapor_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
        await asyncio.sleep(2)
        await message.delete()
        return

    reply_text = []

    for char in vapor_text:
        if 0x21 <= ord(char) <= 0x7F:
            reply_text.append(chr(ord(char) + 0xFEE0))
        elif ord(char) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(char)

    await message.edit("".join(reply_text))


@Client.on_message(filters.command("stretch", ".") & filters.me)
async def stretch(bot: Client, message: Message):
    cmd = message.command

    stretch_text = ""
    if len(cmd) > 1:
        stretch_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        stretch_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("`Giiiiiiiv sooooooomeeeeeee teeeeeeext!`")
        await asyncio.sleep(2)
        await message.delete()
        return

    count = randint(3, 10)
    reply_text = re.sub(
        r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count), stretch_text
    )
    await message.edit(reply_text)


@Client.on_message(filters.command("beemoviescript", ".") & filters.me)
async def bee_movie_script(bot: Client, message: Message):
    await message.edit(
        "Here is the entire Bee Movie script.\nhttps://nekobin.com/yixofunaqa"
    )

@Client.on_message(filters.command(["ht"], ".") & filters.me)
async def heads_tails(bot: Client, message: Message):
    coin_sides = ["Heads", "Tails"]
    ht = f"Heads or Tails? `{choice(coin_sides)}`"
    await message.edit(ht)

@Client.on_message(filters.command(["otherwise", 'other'], ".") & filters.me)
async def youd_think_so_but_this_says_otherwise(bot: Client, message: Message):
    disable_web_page_preview = True
    if len(message.command) > 1:
        disable_web_page_preview = False

    await message.edit(
        f"You\'d think so, but this says <a href='https://i.imgur.com/nzncews.jpg'>otherwise</a>.",
        disable_web_page_preview=disable_web_page_preview
    )


@Client.on_message(filters.command("reverset", ".") & filters.me)
async def text_reverse(bot: Client, message: Message):
    cmd = message.command

    reverse_text = ""
    if len(cmd) > 1:
        reverse_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        reverse_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("`Give me something to reverse`"[::-1])
        await asyncio.sleep(2)
        await message.delete()
        return

    await message.edit(reverse_text[::-1])


@Client.on_message(filters.me & filters.command(["shg", "shrug"], "."))
async def shrug(bot: Client, message):
    await message.edit(choice(MEMES.SHRUGS))


@Client.on_message(filters.me & filters.command(["tableflip", "tflip"], "."))
async def table_flip(bot: Client, message):
    await message.edit(choice(MEMES.TABLE_FLIPS))


@Client.on_message(filters.me & filters.command("flip", "."))
async def flip_text(bot: Client, message):
    cmd = message.command

    text = ""
    if len(cmd) > 1:
        text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await message.edit("`Give me something to reverse`"[::-1])
        await asyncio.sleep(2)
        await message.delete()
        return

    final_str = ""
    for char in text:
        if char in MEMES.REPLACEMENT_MAP.keys():
            new_char = MEMES.REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        await message.edit(final_str)
    else:
        await message.edit(text)


@Client.on_message(filters.me & filters.command('silence', '.'))
async def silence_wench(bot: Client, message):
    await message.edit("Silence wench. Do not speak of the forbidden scripture to me. I was there when it was written.")



add_command_help(
    "text",
    [
        [".nice", "Replaces command with NICENICENICENICE."],
        [".compliment", "Replaces command with a nice compliment."],
        [".devexcuse", "Replaces command with an excuse that a developer would give."],
        [".reverse", "Sends ASCII version of the Uno reverse card."],
        [".slap", "Sends a randomly generated slap text. Can become very random at some times."],
        [".insult", "Sends a randomly generated insult. Can become very random at some times."],
        [".vapor", "Vaporizes the text."],
        [".weeb `or` .weebify", "Weebifies the text."],
        [".ok", "Sends -_____- with a fast animation."],
        ["-_-", "Extends to -________-"],
        [".f", "Pay respects"],
        [".F", "Pay respects but filled"],
        ["#f", "Pay respects but calligraphy."],
        [".mockt", "Mock (text only version)"],
        [".dice", "Send dice animation"],
        [".target", "Send target animation"],
        ["oof", "Oof"],
        [";_; `or` .sad `or` cri", ";_;"],
        [".ht", "Heads or Tails"],
        [".reverset", "Reverses the text"],
        [".shrug", "Random shrug"],
        [".tableflip", "Flip the table"],
        [".silence", "Silence wench"],
    ],
)
