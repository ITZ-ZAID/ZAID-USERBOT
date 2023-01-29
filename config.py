import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "14301685")) #optional
API_HASH = getenv("API_HASH", "fcf41f9e84b2339cde2bc746eb76c0c0") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1426934949").split()))
OWNER_ID = int(getenv("OWNER_ID", "1426934949"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://mirshodbey:12345@cluster0.qtlroai.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5620598489:AAHErTkrUQFOzPAKYdstof9ZCk0CFGOJRc8")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AgBiMZkAaYwWJXaQxYBodJQI4HGvuNdjmojxnr2rrx_YJwrzgYIE4DlFbor_kgHsTtd8emQRFXdi5tJmQJGe9QRgo8jzZVduIYEIIgzyenxFRCn0WanpfIYJtLZkJzR04iUFnXEJyyg14suT40MIpOLUy0Q9EH7TRi-JGgKDkjoszLffiQLTErgrthi67QCVkQV7tadhz6dS8mpL7v2jWiQrgUJjpylVDWr-0Mb2I1lQ6Vwv90pqQVZyq8xoLCXz3eFfsBDxBwtecUMQ_FaAefwv81rKZOXN8bDQ9cs-DJekrqncK5Lse_sRLO4NkmyEtLNW9JBEYYcPcMgJ1zSQaiHWDRn-TQAAAABVDUylAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")

