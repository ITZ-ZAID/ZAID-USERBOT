import os
import time
import asyncio
import shlex
import sys
from pyrogram import filters, Client
from pyrogram.types import Message
from pymediainfo import MediaInfo
from typing import Tuple
from handlers.help import add_command_help

async def convert_vid_to_vidnote(input_vid: str, final_path: str):
    """ Convert Video To Video Note (Round) """
    media_info = MediaInfo.parse(input_vid)
    for track in media_info.tracks:
        if track.track_type == "Video":
            aspect_ratio = track.display_aspect_ratio
            height = track.height
            width = track.width
    if aspect_ratio != 1:
        crop_by = width if (height > width) else height
        await run_cmd(
            f'ffmpeg -i {input_vid} -vf "crop={crop_by}:{crop_by}" {final_path}'
        )
        os.remove(input_vid)
    else:
        os.rename(input_vid, final_path)

async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

@Client.on_message(filters.command("subtitle", ["."]) & filters.me)
async def pijtkiau(client: Client, message: Message):
    msg_ = await message.edit_text("`wait bruh`")
    if not message.reply_to_message:
        await msg_.edit("`Please Reply To Video To Get Its Subtitle!`")
        return
    if not message.reply_to_message.video:
        await msg_.edit("`Please Reply To Video To Get Its Subtitle!`")
        return
    c_time = time.time()
    file_ = await message.reply_to_message.download()
    file_name = (message.reply_to_message.video.file_name).split(".")[0]
    srt_file_name = str(file_name) + ".srt"
    cmd_to_un = f"ffmpeg -i {file_} {srt_file_name}"
    await run_cmd(cmd_to_un)
    if not os.path.exists(srt_file_name):
        await msg_.edit("`Seems Like This Media Don't Have Subtitle`")
        os.remove(file_)
        return
    await msg_.edit("`Almost Done! Now Uploading Srt File!`")
    if message.reply_to_message:
        await client.send_document(
            message.chat.id,
            srt_file_name,
            caption=f">> {file_name} <<",
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_document(
            message.chat.id, srt_file_name, caption=f">> {file_name} <<"
        )
    await msg_.delete()
    for files in (file_, srt_file_name):
        if files and os.path.exists(files):
            os.remove(files)


@Client.on_message(filters.command(["ffwd", "fastforward"], ["."]) & filters.me)
async def prtaiyau(client: Client, message: Message):
    msg_ = await message.edit_text("`Brewing`")
    if not message.reply_to_message:
        await msg_.edit("`Please Reply To Video To Fast Forward It!`")
        return
    if not (message.reply_to_message.video or message.reply_to_message.animation):
        await msg_.edit("`Please Reply To Video To Fast Forward It!`")
        return
    c_time = time.time()
    file_ = await message.reply_to_message.download()
    file_name = "FastForwarded.mp4"
    cmd_to_un = f'ffmpeg -i {file_} -vf "setpts=0.25*PTS" {file_name}'
    await run_cmd(cmd_to_un)
    if not os.path.exists(file_name):
        await msg_.edit("`The magic potion failed`")
        return
    if message.reply_to_message:
        await client.send_video(
            message.chat.id,
            file_name,
            reply_to_message_id=message.reply_to_message.message_id,
            )
    else:
        await client.send_video(
            message.chat.id,
            file_name
             )
    await msg_.delete()
    for files in (file_, file_name):
        if files and os.path.exists(files):
            os.remove(files)


@Client.on_message(filters.command(["slwdwn", "slowdown"], ["."]) & filters.me)
async def piljhsiau(client: Client, message: Message):
    msg_ = await message.edit_text("`Prepping`")
    if not message.reply_to_message:
        await msg_.edit("`Please Reply To Video To Slow Down!`")
        return
    if not (message.reply_to_message.video or message.reply_to_message.animation):
        await msg_.edit("`Please Reply To Video To Slow Down!`")
        return
    c_time = time.time()
    file_ = await message.reply_to_message.download()
    file_name = "SlowDown.mp4"
    cmd_to_un = f'ffmpeg -i {file_} -vf "setpts=4*PTS" {file_name}'
    await run_cmd(cmd_to_un)
    if not os.path.exists(file_name):
        await msg_.edit("`Prep failed`")
        return
    if message.reply_to_message:
        await client.send_video(
            message.chat.id,
            file_name,
            reply_to_message_id=message.reply_to_message.message_id
            )
    else:
        await client.send_video(
            message.chat.id,
            file_name
            )
    await msg_.delete()
    for files in (file_, file_name):
        if files and os.path.exists(files):
            os.remove(files)

@Client.on_message(filters.command(["vidnot", "vnote", "videonote"], ["."]) & filters.me)
async def pijtkiau(client: Client, message: Message):
    msg_ = await message.edit_text("`Making your wish come true`")
    if not message.reply_to_message:
        await msg_.edit("`Please Reply To A Video To Convert To Video Note!`")
        return
    if not (message.reply_to_message.video or message.reply_to_message.animation):
        await msg_.edit("`Please Reply To A Video To Convert To Video Note!`")
        return
    c_time = time.time()
    file_ = await message.reply_to_message.download()
    file_name = "vid_note.mp4"
    await convert_vid_to_vidnote(file_, file_name)
    if not os.path.exists(file_name):
        await msg_.edit("`Sed magic may be a dream`")
        return
    if message.reply_to_message:
        await client.send_video_note(
            message.chat.id,
            file_name,
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_video_note(
            message.chat.id,
            file_name
            )
    await msg_.delete()
    for files in (file_, file_name):
        if files and os.path.exists(files):
            os.remove(files)


add_command_help(
    "convert",
    [
        ["", "This command helps you to convert"],
        [".subtitle", ""],
        [
            ".ffwd `or` .slwdwn",
            "Make Vc Note Faster Else Slower ",
        ],
        [
            ".vidnot",
            "",
        ],
    ],
)
