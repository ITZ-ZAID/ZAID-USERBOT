import asyncio
import os
import time
import requests
import wget
from yt_dlp import YoutubeDL
from youtubesearchpython import SearchVideos
from pyrogram import filters, Client
from pyrogram.types import User , Message
from handlers.help import add_command_help

@Client.on_message(filters.command(["vid", "video"] , ["."]) & filters.me)
async def yt_vid(client: Client, message: Message):
    input_st = message.text
    input_str= input_st.split(" ", 1)[1]
    pablo = await message.edit_text("`Processing...`")
    if not input_str:
        await message.edit_text(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    await message.edit_text(f"`Searching {input_str} From Youtube. Please Wait.`")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await message.edit_text(f"**Failed To Download** \n**Error :** `{str(e)}`")
        return
    c_time = time.time()
    file_path= f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** `{vid_title}` \n**Requested For ➠** `{input_str}` \n**Channel ➠** `{uploade_r}` \n**Link ➠** `{url}`"
    await client.send_video(
        message.chat.id,
        video=open(file_path, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=downloaded_thumb,
        caption=capy,
        supports_streaming=True,
    )
    await message.delete()
    for files in (downloaded_thumb, file_path):
        if files and os.path.exists(files):
            os.remove(files)


add_command_help(
    "video",
    [
        [
            ".video",
            "Download Video from YouTube ",
        ]
    ],
)
