from subprocess import Popen, PIPE, TimeoutExpired
import os
from time import perf_counter

from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
import asyncio
from handlers.help import *

@Client.on_message(filters.command(["shell", "sh"], ["."]) & filters.user(SUDO_USERS))
async def shell(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("<b>Specify the command in message text</b>")
    cmd_text = message.text.split(maxsplit=1)[1]
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "#" if os.getuid() == 0 else "$"
    text = f"<b>{char}</b> <code>{cmd_text}</code>\n\n"

    umm = await message.reply_text(text + "<b>Running...</b>")
    try:
        start_time = perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "<b>Timeout expired (60 seconds)</b>"
    else:
        stop_time = perf_counter()
        if stdout:
            text += "<b>Output:</b>\n" f"<code>{stdout}</code>\n\n"
        if stderr:
            text += "<b>Error:</b>\n" f"<code>{stderr}</code>\n\n"
        text += f"<b>Completed in {round(stop_time - start_time, 5)} seconds with code {cmd_obj.returncode}</b>"
    await umm.edit(text)
    cmd_obj.kill()



import asyncio
import io
import os
import sys
import traceback

from pyrogram import filters, Client
from pyrogram.types import Message


from helpers.mongo import cli as database
from helpers.PyroHelpers import ReplyCheck


@Client.on_message(
    filters.command(["eval", "ev"], [".", "!"])
    & filters.user(SUDO_USERS)
    & ~filters.forwarded
    & ~filters.edited
    & ~filters.via_bot
)
async def evaluation_func(bot: Client, message: Message):
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        reply = message.reply_to_message or None
        await aexec(cmd, bot, message, reply, database)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>Expression</b>:\n<code>{}</code>\n\n<b>Result</b>:\n<code>{}</code> \n".format(
        cmd, evaluation.strip()
    )

    if len(final_output) > 4096:
        with open("eval.txt", "w", encoding="utf8") as out_file:
            out_file.write(str(final_output))

        await message.reply_document(
            "eval.txt",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
        os.remove("eval.txt")
        await status_message.delete()
    else:
        await status_message.edit(final_output)


async def aexec(code, b, m, r, d):
    sys.tracebacklimit = 0
    exec(
        "async def __aexec(b, m, r, d): "
        + "".join(f"\n {line}" for line in code.split("\n"))
    )
    return await locals()["__aexec"](b, m, r, d)


@Client.on_message(
    filters.command("exec", ".")
    & filters.user(SUDO_USERS)
    & ~filters.forwarded
    & ~filters.edited
    & ~filters.via_bot
)
async def execution(client: Client, message: Message):
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id

    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No errors"
    o = stdout.decode()
    if not o:
        o = "No output"

    OUTPUT = ""
    OUTPUT += f"<b>Command:</b>\n<code>{cmd}</code>\n\n"
    OUTPUT += f"<b>Output</b>: \n<code>{o}</code>\n"
    OUTPUT += f"<b>Errors</b>: \n<code>{e}</code>"

    if len(OUTPUT) > 4096:
        with open("exec.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(OUTPUT))
        await message.reply_document(
            document="exec.text",
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=ReplyCheck(message),
        )
        os.remove("exec.text")
    else:
        await message.reply_text(OUTPUT)



add_command_help(
    "devloper",
    [
        [".eval", "To Run something."],
        [".sh", "To Run commands."],
    ],
)
