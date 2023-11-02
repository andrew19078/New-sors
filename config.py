from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
app_id = 19861046
app_hash = "c675f88f7e0ae3d1950ffc0eb40f2674"
session = os.environ.get("teleson")
StrPython = TelegramClient(StringSession(session), app_id, app_hash)
StrPython.start()