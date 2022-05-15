from helpers.SQL import dbb

gbun = dbb["GBAN"]


async def gban_user(user, reason="#GBanned"):
    await gbun.insert_one({"user": user, "reason": reason})


async def ungban_user(user):
    await gbun.delete_one({"user": user})


async def gban_list():
    return [lo async for lo in gbun.find({})]


async def gban_info(user):
    kk = await gbun.find_one({"user": user})
    if not kk:
        return False
    else:
        return kk["reason"]
