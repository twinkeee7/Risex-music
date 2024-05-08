## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6446073646:AAEwlps0IXbsjE0oDmeoXnFUoO4AZIWD2bE")
BOT_NAME = getenv("BOT_NAME", "˹Rɪsᴇ ꭙ Assɪsᴛᴀɴᴛ˼ ♪✨ !")

API_ID = int(getenv("API_ID", "27013344"))
API_HASH = getenv("API_HASH", "be5f160b65f07128459b4289c6e286ad")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Rise")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@Rise_Ownerr")
ALIVE_NAME = getenv("ALIVE_NAME", "Rise")
BOT_USERNAME = getenv("BOT_USERNAME", "@RisexAdvancedManagementMusic_bot")
OWNER_ID = getenv("OWNER_ID", "7062539103")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "⏤͟͞Rɪsᴇ ꭙ Assɪsᴛᴀɴᴛ | ™")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/Riseeuniverse")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/RiseUniverseNetwork")
HEROKU_APP_NAME = getenv("Risebanahii")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7062539103").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c2ff050b35f2a1aeecc09.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/463dd0acf84d4b1ae10b0.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
