import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
que = {}
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
