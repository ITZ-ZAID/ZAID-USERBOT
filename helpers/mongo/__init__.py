import motor.motor_asyncio
from main import MONGO_DB_URI


cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
