from pyrogram import Client, filters
import asyncio
import time
from emoji import get_emoji_regexp
from pyrogram.types import ChatPermissions, Message
from pyrogram.errors import (
    UsernameInvalid,
    ChatAdminRequired,
    PeerIdInvalid,
    UserIdInvalid,
    UserAdminInvalid,
    FloodWait,
)


@Client.on_message(filters.group & filters.command("promote", ["."]) & filters.me)  
async def promotte(client: Client, message: Message):
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
                        can_change_info=True,
                        can_delete_messages=True,
                        can_restrict_members=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                    )

                    await asyncio.sleep(2)
                    await client.set_administrator_title(
                        message.chat.id, user_id, custom_rank
                  )
                    await message.edit_text("promoted due to bribe")
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
