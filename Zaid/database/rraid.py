from Zaid.database import cli

collection = cli["Zaid"]["rraid"]


async def rraid_user(chat):
    doc = {"_id": "Rraid", "users": [chat]}
    r = await collection.find_one({"_id": "Rraid"})
    if r:
        await collection.update_one({"_id": "Rraid"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_rraid_users():
    results = await collection.find_one({"_id": "Rraid"})
    if results:
        return results["users"]
    else:
        return []


async def unrraid_user(chat):
    await collection.update_one({"_id": "Rraid"}, {"$pull": {"users": chat}})
