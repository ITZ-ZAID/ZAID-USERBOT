import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config import *

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = API_ID
API_HASH = API_HASH 
LOG_GROUP = LOG_GROUP
SUDO_USERS = SUDO_USERS
DB_URL = DB_URL


if not STRING_SESSION1:
    logging.error("No String Session Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)

if ALIVE_IMG:
    ALIVE_PIC = ALIVE_IMG
else: 
    ALIVE_PIC = 'https://telegra.ph/file/077f0e0eb681938c6d85f.jpg'

if MONGO_DB:
    MONGO_DB = MONGO_DB
else: 
    MONGO_DB = "mongodb+srv://Zaid:Zaid@cluster0.4bszo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

if LOG_GROUP:
    Owner = LOG_GROUP
else:
    Owner = 777000


if STRING_SESSION1:
    bot1 = Client(session_name= STRING_SESSION1, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot1 = None

if STRING_SESSION2:
    bot2 = Client(session_name= STRING_SESSION2, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot2 = None

if STRING_SESSION3:
    bot3 = Client(session_name= STRING_SESSION3, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot3 = None

if STRING_SESSION4:
    bot4 = Client(session_name= STRING_SESSION4, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot4 = None

if STRING_SESSION5:
    bot5 = Client(session_name= STRING_SESSION5, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot5 = None

if STRING_SESSION6:
    bot6 = Client(session_name= STRING_SESSION6, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot6 = None

if STRING_SESSION7:
    bot7 = Client(session_name= STRING_SESSION7, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot7 = None

if STRING_SESSION8:
    bot8 = Client(session_name= STRING_SESSION8, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot8 = None

if STRING_SESSION9:
    bot9 = Client(session_name= STRING_SESSION9, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot9 = None

if STRING_SESSION10:
    bot = Client(session_name= STRING_SESSION10, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot = None

if STRING_SESSION11:
    bot11 = Client(session_name= STRING_SESSION11, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot11 = None

if STRING_SESSION12:
    bot12 = Client(session_name= STRING_SESSION12, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot12 = None

if STRING_SESSION13:
    bot13 = Client(session_name= STRING_SESSION13, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot13 = None

if STRING_SESSION14:
    bot14 = Client(session_name= STRING_SESSION14, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot14 = None

if STRING_SESSION15:
    bot15 = Client(session_name= STRING_SESSION15, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot15 = None

if STRING_SESSION16:
    bot16 = Client(session_name= STRING_SESSION16, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot16 = None

if STRING_SESSION17:
    bot17 = Client(session_name= STRING_SESSION17, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot17 = None

if STRING_SESSION18:
    bot18 = Client(session_name= STRING_SESSION18, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot18 = None

if STRING_SESSION19:
    bot19 = Client(session_name= STRING_SESSION19, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot19 = None

if STRING_SESSION20:
    bot20 = Client(session_name= STRING_SESSION20, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot20 = None

if STRING_SESSION21:
    bot21 = Client(session_name= STRING_SESSION21, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot21 = None

if STRING_SESSION22:
    bot22 = Client(session_name= STRING_SESSION22, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot22 = None

if STRING_SESSION23:
    bot23 = Client(session_name= STRING_SESSION23, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot23 = None

if STRING_SESSION24:
    bot24 = Client(session_name= STRING_SESSION24, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot24 = None

if STRING_SESSION25:
    bot25 = Client(session_name= STRING_SESSION25, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot25 = None

if STRING_SESSION26:
    bot26 = Client(session_name= STRING_SESSION26, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot26 = None

if STRING_SESSION27:
    bot27 = Client(session_name= STRING_SESSION27, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot27 = None

if STRING_SESSION28:
    bot28 = Client(session_name= STRING_SESSION28, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot28 = None

if STRING_SESSION29:
    bot29 = Client(session_name= STRING_SESSION29, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot29 = None

if STRING_SESSION30:
    bot30 = Client(session_name= STRING_SESSION30, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot30 = None

if STRING_SESSION31:
    bot31 = Client(session_name= STRING_SESSION31, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot31 = None

if STRING_SESSION32:
    bot32 = Client(session_name= STRING_SESSION32, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot32 = None

if STRING_SESSION33:
    bot33 = Client(session_name= STRING_SESSION33, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot33 = None

if STRING_SESSION34:
    bot34 = Client(session_name= STRING_SESSION34, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot34 = None

if STRING_SESSION35:
    bot35 = Client(session_name= STRING_SESSION35, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot35 = None

if STRING_SESSION36:
    bot36 = Client(session_name= STRING_SESSION36, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot36 = None

if STRING_SESSION37:
    bot37 = Client(session_name= STRING_SESSION37, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot37 = None

if STRING_SESSION38:
    bot38 = Client(session_name= STRING_SESSION38, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot38 = None

if STRING_SESSION39:
    bot39 = Client(session_name= STRING_SESSION39, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot39 = None

if STRING_SESSION40:
    bot40 = Client(session_name= STRING_SESSION40, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot40 = None

if STRING_SESSION41:
    bot41 = Client(session_name= STRING_SESSION41, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot41 = None

if STRING_SESSION42:
    bot42 = Client(session_name= STRING_SESSION42, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot42 = None

if STRING_SESSION43:
    bot43 = Client(session_name= STRING_SESSION43, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot43 = None

if STRING_SESSION44:
    bot44 = Client(session_name= STRING_SESSION44, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot44 = None

if STRING_SESSION45:
    bot45 = Client(session_name= STRING_SESSION45, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot45 = None

if STRING_SESSION46:
    bot46 = Client(session_name= STRING_SESSION46, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot46 = None

if STRING_SESSION47:
    bot47 = Client(session_name= STRING_SESSION47, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot47 = None

if STRING_SESSION48:
    bot48 = Client(session_name= STRING_SESSION48, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot48 = None

if STRING_SESSION49:
    bot49 = Client(session_name= STRING_SESSION49, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot49 = None

if STRING_SESSION50:
    bot50 = Client(session_name= STRING_SESSION50, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="handlers"))
else:
    bot50 = None



scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

if bot1:
    bot1.start()
    bot1.join_chat("TheUpdatesChannel")
if bot2:
    bot2.start()
    bot2.join_chat("TheUpdatesChannel")
if bot3:
    bot3.start()
    bot3.join_chat("TheUpdatesChannel")
if bot4:
    bot4.start()
    bot4.join_chat("TheUpdatesChannel")
if bot5:
    bot5.start()
    bot5.join_chat("TheUpdatesChannel")
if bot6:
    bot6.start()
    bot6.join_chat("TheUpdatesChannel")
if bot7:
    bot7.start()
    bot7.join_chat("TheUpdatesChannel")
if bot8:
    bot8.start()
    bot8.join_chat("TheUpdatesChannel")
if bot9:
    bot9.start()
    bot9.join_chat("TheUpdatesChannel")
if bot:
    bot.start()
    bot.join_chat("TheUpdatesChannel")
if bot11:
    bot11.start()
    bot11.join_chat("TheUpdatesChannel")
if bot12:
    bot12.start()
    bot12.join_chat("TheUpdatesChannel")
if bot13:
    bot13.start()
    bot12.join_chat("TheUpdatesChannel")
if bot14:
    bot14.start()
    bot14.join_chat("TheUpdatesChannel")
if bot15:
    bot15.start()
    bot15.join_chat("TheUpdatesChannel")
if bot16:
    bot16.start()
    bot16.join_chat("TheUpdatesChannel")
if bot17:
    bot17.start()
    bot17.join_chat("TheUpdatesChannel")
if bot18:
    bot18.start()
    bot18.join_chat("TheUpdatesChannel")
if bot19:
    bot19.start()
    bot19.join_chat("TheUpdatesChannel")
if bot20:
    bot20.start()
    bot20.join_chat("TheUpdatesChannel")
if bot21:
    bot21.start()
    bot21.join_chat("TheUpdatesChannel")
if bot22:
    bot22.start()
    bot22.join_chat("TheUpdatesChannel")
if bot23:
    bot23.start()
    bot23.join_chat("TheUpdatesChannel")
if bot24:
    bot24.start()
    bot24.join_chat("TheUpdatesChannel")
if bot25:
    bot25.start()
    bot25.join_chat("TheUpdatesChannel")
if bot26:
    bot26.start()
    bot26.join_chat("TheUpdatesChannel")
if bot27:
    bot27.start()
    bot27.join_chat("TheUpdatesChannel")
if bot28:
    bot28.start()
    bot28.join_chat("TheUpdatesChannel")
if bot29:
    bot29.start()
    bot29.join_chat("TheUpdatesChannel")
if bot30:
    bot30.start()
    bot30.join_chat("TheUpdatesChannel")
if bot31:
    bot31.start()
    bot31.join_chat("TheUpdatesChannel")
if bot32:
    bot32.start()
    bot32.join_chat("TheUpdatesChannel")
if bot33:
    bot33.start()
    bot33.join_chat("TheUpdatesChannel")
if bot34:
    bot34.start()
    bot34.join_chat("TheUpdatesChannel")
if bot35:
    bot35.start()
    bot35.join_chat("TheUpdatesChannel")
if bot36:
    bot36.start()
    bot36.join_chat("TheUpdatesChannel")
if bot37:
    bot37.start()
    bot37.join_chat("TheUpdatesChannel")
if bot38:
    bot38.start()
    bot38.join_chat("TheUpdatesChannel")
if bot39:
    bot39.start()
    bot39.join_chat("TheUpdatesChannel")
if bot40:
    bot40.start()
    bot40.join_chat("TheUpdatesChannel")
if bot41:
    bot41.start()
    bot41.join_chat("TheUpdatesChannel")
if bot42:
    bot42.start()
    bot42.join_chat("TheUpdatesChannel")
if bot43:
    bot43.start()
    bot43.join_chat("TheUpdatesChannel")
if bot44:
    bot44.start()
    bot44.join_chat("TheUpdatesChannel")
if bot45:
    bot45.start()
    bot45.join_chat("TheUpdatesChannel")
if bot46:
    bot46.start()
    bot46.join_chat("TheUpdatesChannel")
if bot47:
    bot47.start()
    bot47.join_chat("TheUpdatesChannel")
if bot48:
    bot48.start()
    bot48.join_chat("TheUpdatesChannel")
if bot49:
    bot49.start()
    bot49.join_chat("TheUpdatesChannel")
if bot50:
    bot50.start()
    bot50.join_chat("TheUpdatesChannel")

idle()

print("🎉 Successfully Deployed 🎉 @Timesisnotwaiting")
print("Enjoy! Do visit @Superiro_Bots")

