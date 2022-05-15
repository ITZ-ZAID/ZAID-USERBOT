from pyrogram import Client, filters
import asyncio
import time
from pyrogram.errors import (
    UsernameInvalid,
    ChatAdminRequired,
    PeerIdInvalid,
    UserIdInvalid,
    UserAdminInvalid,
    FloodWait,
)
from pyrogram.types import ChatPermissions, Message


@Client.on_message(filters.group & filters.command("demote", ["."]) & filters.me)  
async def demote(client: Client, message: Message):
  if message.chat.type in ["group", "supergroup"]:
    cmd = message.command
    me_m= message.from_user
    me_ = await message.chat.get_member(int(me_m.id))
    if not me_.can_promote_members:
        await message.edit("`Boss, You Don't Have Promote Permission!`")
        return
    can_promo = True
    if can_promo:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[1:]))
                else:
                    usr = await client.get_users(cmd[1])
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[2:]))
                    user_id = usr.id
            except IndexError:
                await message.delete()
                return

            if user_id:
                try:
                    await client.promote_chat_member(
             message.chat.id,
             user_id,
            is_anonymous=False,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,)
                    await message.edit_text("demoted due to corruption")
                    await asyncio.sleep(5)
                    await message.delete()
                except UsernameInvalid:
                    await message.edit_text("user_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except PeerIdInvalid:
                    await message.edit_text("peer_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except UserIdInvalid:
                    await message.edit_text("id_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except ChatAdminRequired:
                    await message.edit_text("denied_permission")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit_text(f"**Log:** `{e}`")
                    return

    else:
            await message.edit_text("denied_permission")
            await asyncio.sleep(5)
            await message.delete()
  else:
        await message.delete()
