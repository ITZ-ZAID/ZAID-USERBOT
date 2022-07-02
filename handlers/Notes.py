from pyrogram import filters, Client

from helpers.pyrohelper import get_arg
import helpers.mongo.notesdb as Zaid
from main import LOG_GROUP
from handlers.help import *

LOG_CHAT = LOG_GROUP


@Client.on_message(filters.command("save", ["."]) & filters.me)
async def save(client: Client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**You must give a name for a note.**")
        return
    note_name = arg
    note = await Zaid.get_note(note_name)
    if note:
        await message.edit(f"**Note `{note_name}` already exists**")
        return
    reply = message.reply_to_message
    if not reply:
        await message.edit("Reply to a message to save a note")
        return
    copy = await client.copy_message(LOG_CHAT, message.chat.id, reply.message_id)
    await Zaid.save_note(note_name, copy.message_id)
    await message.edit("**Note saved**")


@Client.on_message(filters.command("get", ["."]) & filters.me)
async def get(app: Client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("Get what?")
        return
    note_name = arg
    note = await Zaid.get_note(note_name)
    if not note:
        await message.edit(f"**Note {note_name} dosen't exists**")
        return
    if message.reply_to_message:
        await app.copy_message(
            message.chat.id,
            LOG_CHAT,
            note,
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await app.copy_message(message.chat.id, LOG_CHAT, note)
    await message.delete()


@Client.on_message(filters.command("clear", ["."]) & filters.me)
async def clear(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("What do you want to delete?")
        return
    note_name = arg
    note = await Zaid.get_note(note_name)
    if not note:
        await message.edit(f"**Failed to delete note `{note_name}`**")
        return
    await Zaid.rm_note(note_name)
    await message.edit(f"**Succesfully deleted note `{note_name}`**")


@Client.on_message(filters.command("notes", ["."]) & filters.me)
async def notes(client, message):
    msg = "**Saved Notes**\n\n"
    all_notes = await Zaid.all_notes()
    if not all_notes:
        await message.edit("**No notes has been saved**")
        return
    for notes in all_notes:
        msg += f"◍ `{notes}`\n"
    await message.edit(msg)


@Client.on_message(filters.command("clearall", ["."]) & filters.me)
async def clearall(client, message):
    await Zaid.rm_all()
    await message.edit("**Removed all saved notes**")

add_command_help(
    "notes",
    [
        [".save", " -> Save a new note. Must be used in reply with one parameter (note name)."],
        [".get", " -> Gets the note specified."],
        [".clear", "-> Deletes a note, specified by note name."],
        [".clearall", " -> Deletes all the saved notes."],
        [".notes", " -> List the saved notes."],

    ],
)
