from os import getenv

API_ID = int(getenv("API_ID", "12230070")) #optional
API_HASH = getenv("API_HASH", "61dd2ae1bf10edcb7dc53f17109c50b6") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID", "5562325175"))
MONGO_URL = getenv("MONGO_URL","Yatoo99@cluster0.3gj7zms.mongodb.net")
BOT_TOKEN = getenv("BOT_TOKEN", "5651649947:AAHSklarrf21EahrUe0ZGjpmDZO8oxEOzPY")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBeGSM7eHA02L-9cmsB1ZJn8wuRJTMYjetY4wftl3wK3dhtxys49t6bL5pBLapQf2poQHlYpnFZISSbFeeExmNiTGBDf_Z68z_LkOEUgspETQLWVj4Lwf21TKjv4M0LkCVUhQl5CEpHvVq_56oxEhu8PgtkbKHkNZcTPBV9tU0PjsTACedcaySnDtUaaKrosWT9ova9U6iLxW3N9DABvZU1AMHAGkKIHmYADmDCYUbYdu_6Q0iMKgGvPbhWa1G9qbC-nD7OcZ7iSP364_S5Wcdvhrff_byaN6AlNyj2n85i8mPCgdOJGzcpfT6gA-Wb6ag34mJTgrSjS0_H_TW-lZS6AAAAAUuKWLcA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
