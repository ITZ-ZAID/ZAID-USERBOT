```python3
from pyrogram import Client, filters
from pyrogram.types import Message
from handlers.help import *




@Client.on_message(filters.command("hi", [.]) & filters.me)
async def example(client: Client, message: Message):
    await message.edit("<code>Hello</code>")


@Client.on_message(filters.command("hii", prefix) & filters.me)
async def example_send(client: Client, message: Message):
    await client.send_message(message.chat.id, "<b>Hello 👋</b>")



# add_handler_help(
#    "module"
#       "Command"= "defined",
#)

```
