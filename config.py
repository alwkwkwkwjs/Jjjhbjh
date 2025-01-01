from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "20752475")
APP_HASH = os.environ.get("APP_HASH", "f66ef394aeace4306b16cbc1bd62607a")
SESSION = os.environ.get("SESSION")
ha313so = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
ha313so.start()
