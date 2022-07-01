import motor.motor_asyncio
from main import MONGO_DB


cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DB)
