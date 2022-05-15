from helpers.SQL import dbb

gmuteh = dbb["GMUTE"]


async def is_gmuted(sender_id):
    kk = await gmuteh.find_one({"sender_id": sender_id})
    if not kk:
        return False
    else:
        return True


async def gmute(sender_id, reason="#GMuted"):
    await gmuteh.insert_one({"sender_id": sender_id, "reason": reason})


async def ungmute(sender_id):
    await gmuteh.delete_one({"sender_id": sender_id})
