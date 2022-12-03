import motor.motor_asyncio

from config import MONGO_URL
cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
