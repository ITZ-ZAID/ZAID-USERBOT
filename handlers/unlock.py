from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from handlers.help import add_command_help

add_command_help(
    "locks",
    [
        [".lock", "locks permission in the group."],
        [".unlock", "unlocks permission in the group Supported Locks / Unlocks:`msg` | `media` | `stickers``polls` | `info`  | `invite` |`animations` | `games` |`inlinebots` | `webprev` |`pin` | `all`."],
    ],
)

@Client.on_message(filters.command("unlock", ["."]) & filters.me)
async def unlock(client: Client, message: Message):
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
        umsg = ""
        umedia = ""
        ustickers = ""
        uanimations = ""
        ugames = ""
        uinlinebots = ""
        uwebprev = ""
        upolls = ""
        uinfo = ""
        uinvite = ""
        upin = ""
        uperm = ""  # pylint:disable=E0602

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
                await client.set_chat_permissions(chat_id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_stickers=True,
                        can_send_animations=True,
                        can_send_games=True,
                        can_use_inline_bots=True,
                        can_send_polls=True,
                        can_change_info=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_add_web_page_previews=True,
                    ))
                await message.edit_text("unlocked all")
                await asyncio.sleep(5)
                await message.delete()

            except Exception as e:
                await messagee.edit_text("denied_permission")
            return

        if lock_type == "messages":
            messages = True
            perm = "messages"

        elif lock_type == "media":
            media = True
            perm = "audios, documents, photos, videos, video notes, voice notes"

        elif lock_type == "stickers":
            stickers = True
            perm = "stickers"

        elif lock_type == "animations":
            animations = True
            perm = "animations"

        elif lock_type == "games":
            games = True
            perm = "games"

        elif lock_type == "inlinebots":
            inlinebots = True
            perm = "inline bots"

        elif lock_type == "webprev":
            webprev = True
            perm = "web page previews"

        elif lock_type == "polls":
            polls = True
            perm = "polls"

        elif lock_type == "info":
            info = False
            perm = "info"

        elif lock_type == "invite":
            invite = True
            perm = "invite"

        elif lock_type == "pin":
            pin = True
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
            await message.edit_text(f"unlocked chat {perm}")
            await asyncio.sleep(5)
            await message.delete()
        except Exception as e:
            print(e)
            await message.delete()
            return
    else:
        await message.delete()
