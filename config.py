import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "21675257")) #optional
API_HASH = getenv("API_HASH", "c355e903072870b1d79de084958ede97") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5465436159").split()))
OWNER_ID = int(getenv("5715764478"))
MONGO_URL = getenv("mongodb+srv://Shivamelu:shivamelu12@cluster0.gyoy4gq.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5446322651:AAFLDXBuLLpCkroBlc-X7ervirfO8slpq3c)"
ALIVE_PIC = getenv("ALIVE_PI")
ALIVE_TEXT = getenv("tobi")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("-837164004")
GIT_TOKEN = getenv("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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/SHIVAMELU/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkARYYs2KjGJH45wDp27zavIbI1w7CEjEaY9pgQbwFEC2ZBcNwyOBplxIyIGNEKd-EcFRAUVKpxa9x1NbDBDG-ZCyOoS0waS6nMKU_TlMEf4eUV-zx-pHMo9rdgSBVcDQPP1V7W1zgeRE7yfBawtKRjT9IsdSdiD20puO_frB6-vXARxJa0iphSLU3iyushNPPyAC3YbFrWXjc17-95IxtM0tfIbRPOs5jMiRjCRxfa9MlIbDNr2z7CnH5k6j_Sz1_yMtmv-XnZcX7apXfuoLjuA3VugFQ4vKQrnuXGeJHkYP6mFv_JkYgS6HochPUKO5YEfwx1GVVYVxROllIlsBpoQgAAAAFFw-__AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
