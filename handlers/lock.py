from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message


@Client.on_message(filters.command("lock", ["."]) & filters.me)  
async def lock(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        cmd = message.command
        me_m= message.from_user
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_manage_chat:
           await message.edit("`You Don't Have Enough Permission!`")
           return
        lock_type = " ".join(cmd[1:])
        chat_id = message.chat.id
        if not lock_type:
            await message.delete()
            return

        get_perm = await client.get_chat(chat_id)

        messages = get_perm.permissions.can_send_messages
        media = get_perm.permissions.can_send_media_messages
        stickers = get_perm.permissions.can_send_stickers
        animations = get_perm.permissions.can_send_animations
        games = get_perm.permissions.can_send_games
        inlinebots = get_perm.permissions.can_use_inline_bots
        webprev = get_perm.permissions.can_add_web_page_previews
        polls = get_perm.permissions.can_send_polls
        info = get_perm.permissions.can_change_info
        invite = get_perm.permissions.can_invite_users
        pin = get_perm.permissions.can_pin_messages

        if lock_type == "all":
            try:
                await client.set_chat_permissions(chat_id, ChatPermissions())
                await message.edit_text("locked all")
                await asyncio.sleep(5)
                await message.delete()

            except Exception as e:
                await messagee.edit_text("denied_permission or the chat is already locked bruh")
            return

        if lock_type == "messages":
            messages = False
            perm = "messages"

        elif lock_type == "media":
            media = False
            perm = "audios, documents, photos, videos, video notes, voice notes"

        elif lock_type == "stickers":
            stickers = False
            perm = "stickers"

        elif lock_type == "animations":
            animations = False
            perm = "animations"

        elif lock_type == "games":
            games = False
            perm = "games"

        elif lock_type == "inlinebots":
            inlinebots = False
            perm = "inline bots"

        elif lock_type == "webprev":
            webprev = False
            perm = "web page previews"

        elif lock_type == "polls":
            polls = False
            perm = "polls"

        elif lock_type == "info":
            info = False
            perm = "info"

        elif lock_type == "invite":
            invite = False
            perm = "invite"

        elif lock_type == "pin":
            pin = False
            perm = "pin"

        else:
            print(e)
            await message.delete()
            return

        try:
            await client.set_chat_permissions(
                chat_id,
                ChatPermissions(
                    can_send_messages=messages,
                    can_send_media_messages=media,
                    can_send_stickers=stickers,
                    can_send_animations=animations,
                    can_send_games=games,
                    can_use_inline_bots=inlinebots,
                    can_add_web_page_previews=webprev,
                    can_send_polls=polls,
                    can_change_info=info,
                    can_invite_users=invite,
                    can_pin_messages=pin,
                ),
            )
            await message.edit_text(f"locked chat {perm}")
            await asyncio.sleep(5)
            await message.delete()
        except Exception as e:
            print(e)
            await message.delete()
            return
    else:
        await message.delete()
