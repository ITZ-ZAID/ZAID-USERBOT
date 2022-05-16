from pyrogram import Client, filters
from pyrogram.types import Message 
from helpers.basic import edit_or_reply, get_text
import requests
import re


@Client.on_message(filters.command('wink', ["."]) & filters.me)
async def wink(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/animu/wink"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()
    

@Client.on_message(filters.command('hug', ["."]) & filters.me)
async def hug(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/animu/hug"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()
    

@Client.on_message(filters.command('pat', ["."]) & filters.me)
async def pat(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/animu/pat"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    await message.delete()
        

@Client.on_message(filters.command('pikachu', ["."]) & filters.me)
async def pikachu(client: Client, message: Message):
    hmm_s = "https://some-random-api.ml/img/pikachu"
    r = requests.get(url=hmm_s).json()
    image_s = r["link"]
    await client.send_video(message.chat.id, image_s)
    if image_s.endswith(".png"):
       await client.send_photo(message.chat.id, image_s)
       return
    if image_s.endswith(".jpg"):
       await client.send_photo(message.chat.id, image_s)
       return
    await message.delete()
