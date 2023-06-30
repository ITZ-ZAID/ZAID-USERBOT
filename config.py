import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "10941030")) #optional
API_HASH = getenv("API_HASH", "741bffed5672da71c5c805488882068d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6084589297").split()))
OWNER_ID = int(getenv("6084589297"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "6307108235:AAEkOPB8y8oDQqAciXSz5mdhGQXwnzjD4vM")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBFWphL9sQ3EIILTitK_qC9YgNclDUkgx2TW5JQZG9Grn8htenfhPDlFU5a4qjCO5vilX6bAcnsW8Ii0mzd_WCVFzdYRviEiKNXpSezQRVEp1jnHUf-Q6oGI8MwP2qg-xstdl3wXyMzlkh4pNhMnxh6-JhxE_Qg3T389JLDNMBsl1fmrbkhPgxIjNb9Q43DO0gq8VeBRjwarpUN5gNVbRgYG3h8p6JB-TNfLNkJjbGflVoV0hRl3VsfvqV9O-GxaCC_kQ-mXl4o91AYh0Q6TjyY_UJ8qsADt_7HzImkI0bFCQ41ps3deNJps5kwbSAuG9QwvP0Bn7Z1qOYxUM8X8MpDAAAAAWqrdvEA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
