import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ✅ my.telegram.org/apps se lo
API_ID = int(getenv("API_ID", "22091901"))
API_HASH = getenv("API_HASH", "54b0cd5fb47a40265b197f1a110b20b8")

# ✅ @BotFather se bot token
BOT_TOKEN = getenv("BOT_TOKEN", "8032338023:AAHvF1meONrnbAgMkkMTXQuxqVCu7PomcVU")

# ✅ MongoDB URI (cloud.mongodb.com)
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "✨𝓜𝓮𝓵𝓸𝓭𝔂𝓧✨")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

LOGGER_ID = int(getenv("LOGGER_ID", "-1003189576237"))
OWNER_ID = int(getenv("OWNER_ID", "5811783004"))
LOG = bool(getenv("LOG", "True"))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

API_URL = getenv("API_URL", "https://api.thequickearn.xyz")
VIDEO_API_URL = getenv("VIDEO_API_URL", "https://api.video.thequickearn.xyz")
API_KEY = getenv("API_KEY", "30DxNexGenBotsfcfad8")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/L2LUCKY/BrandedMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shadowmonarchjii")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+md2s35B2X1wxN2M9")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", "False"))
AUTO_GCAST = getenv("AUTO_GCAST", "False")
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

STRING1 = getenv("STRING_SESSION", "BQHtwy4AGGA4MHPmIjqksdceV3VZ9geDXnFRldvgPR1rbzrtiO2vuI7BYPV4GFSpIzeXmP86w9UVvJUQ7PtbSZofHnFzh_Jnc9YQtr7IDqkjNEXTSN6XkVn7aUAjpdFbIlZrHXwoVrVevopapdle_e134Ug-AhtzfwvmKkFb6cZ9tGuudsmLf2c6uBG-e1PkGKebj7biojgj5JTZ2bSGbKw9R1Td0lTFXGbJqomsmAtCKS_-iM900Q6r1RaNyY8IKv_lr8I7KUSSlmK-sLqXZHyGbyja6ezSUxGvLPzAdp6zg17Lsyft4a4R2f1FycaxjNUt5-_db8g5qcN3HXXpTm6efusOtwAAAAHwB2FsAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

AMBOT = [
    "💞", "🦋", "🔍", "🧪", "💖", "⚡️", "🔥", "❤️‍🔥", "🎩", "🌈", "🍷", "🥂", "👀", "🥃", "🥤", "🕊️",
    "💔", "💘", "🎉", "🥀", "🌹", "❣️", "❤️", "🦋", "🪄", "💌", "💗", "💝", "🧨"
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/62c76ac2095332a0ede75.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/4f59fb748e1990acfa297.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/14eb59ea7d31229d8d751.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/4310ea5f523520b2b765b.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/923c1faac33d8c70335dc.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6c66f8b192532fe758e82.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/ebc4dc6357be06e08a3ed.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/d339f390ec168c19879c6.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/ee0cd53ab73f08f4a3627.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5f9fb5bba66021c782d96.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/affe0afec5c7ad63676a4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/3c446e8dee78ed0ca62ff.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL URL galat hai (https:// se start hona chahiye)")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT URL galat hai (https:// se start hona chahiye)")
