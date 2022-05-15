import sys
from os import environ, execle, path, remove
import shlex
import asyncio
import heroku3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
import os
from pyrogram import Client, filters
from pyrogram.types import Message

HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API = os.environ.get("HEROKU_API", None)

async def runcmd(cmd: str):
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

def fetch_heroku_git_url(api_key, app_name):
    heroku = heroku3.from_key(api_key)
    try:
        heroku_applications = heroku.apps()
    except:
        return None
    heroku_app = None
    for app in heroku_applications:
        if app.name == app_name:
            heroku_app = app
            break
    if not heroku_app:
        return None
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")

@Client.on_message(filters.command("update", ["."]) & filters.me)  
async def update(client: Client, message: Message):
    HEROKU_APP_NAME = HEROKU_APP_NAME
    HEROKU_API = HEROKU_API

    REPO_ = environ.get(
    "UPSTREAM_REPO", "https://github.com/ITZ-ZAID/ZAID-USERBOT"
    )

    U_BRANCH = "main"
    HEROKU_URL=None
    if HEROKU_API and HEROKU_APP_NAME:
        HEROKU_URL = fetch_heroku_git_url(HEROKU_API, HEROKU_APP_NAME)
    msg_ = await message.reply(message, "`Updating Please Wait!`")      
    try:
        repo = Repo()
    except GitCommandError:
        return await msg_.edit(
            "`Invalid Git Command. Please Report This Bug To @Superior_Support`"
        )
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "upstream" in repo.remotes:
            origin = repo.remote("upstream")
        else:
            origin = repo.create_remote("upstream", REPO_)
        origin.fetch()
        repo.create_head(U_BRANCH, origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    try:
        repo.create_remote("upstream", REPO_)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(U_BRANCH)
    if not HEROKU_URL:
        try:
            ups_rem.pull(U_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await runcmd("pip3 install --no-cache-dir -r requirements.txt")
        await msg_.edit("`Updated Sucessfully! Give Me A min To Restart!`")
        args = [sys.executable, "main.py"]
        execle(sys.executable, *args, environ)
        exit()
        return
    else:
        await msg_.edit("`Heroku Detected! Pushing, Please Halt!`")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(HEROKU_URL)
        else:
            remote = repo.create_remote("heroku",HEROKU_URL)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except BaseException as error:
            return await msg_.edit(f"**Updater Error** \nTraceBack : `{error}`")
        await msg_.edit("`Build Started! Please Wait For 10-15 Minutes!`")

