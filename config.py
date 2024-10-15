import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = 27018175
API_HASH = "9726271ce98f126cebea0d4758edc88d"

EVAL = list(map(int, getenv("EVAL", "7427691214 7045191057").split()))
# ------------------------------------------------------
BOT_TOKEN = "6823089678:AAGTnvi30JPowUi-fduy3Jn8xSpAgDbpZWg"
# -------------------------------------------------------
OWNER_USERNAME = "@ken_kaneki_off"
# --------------------------------------------------------
BOT_USERNAME = "@marin_music_bot"
# --------------------------------------------------------
BOT_NAME = "marin akuma music"
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "MissYumikoo")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = "Mango db url - mongodb+srv://chomuchot:marin@akuma.6zp9apt.mongodb.net/?retryWrites=true&w=majority&appName=Akuma"
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = -1001985818611
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = 5161733380
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Chomuchot/Marin-akuma.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = "https://t.me/akuma_network"
SUPPORT_CHAT = "https://t.me/akuma_bot_support"
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = "BQGcQ78AG5nq1UUdL5LimDhXCAJUfQ4TQuOEqRGXfM5RQlv9CVTuEP4y2yDOOmJw3E8ITUHlz8W6P8DJULhl5b21e6H-8EV_SbhyPMTkbcO_DrB6jxgcgRWpbcBGH5LYerU_BeHODWQE5D-P3b36kzf7i92C-4LXObAdTIOGr3AI6n1BlJ-TKa8gvMO1JH8zYcq4GHOSaW1HtgaA6ZGBjtM6Gp8O1KAwSU8unSX6ZzsUfzHrl6Zvo4mrYX-UZz53vdspPPGsErYZDxK5KPGN1bdvRcsl7d5bbcKu1FOwby8xc9iMv1MxabcRFuMEbzbCBOa8TU8Kucd7eYhDIwyb6yHpcC3MrwAAAAGiwXINAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/5cb22767b7c88b0961d4f.png"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/3a3d2f651a312adc0b203.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/8bc4fc60d6de1047f5fa3.jpg"
STATS_IMG_URL = "https://graph.org/file/3fe5b9ae21d09d99eea61.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/86b7bc5ee5685d6aaa7d1.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/a9235bdd223b866dca9fe.jpg"
STREAM_IMG_URL = "https://graph.org/file/a207dfa1dc1a4710d6348.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/a3441f991e0a5350c338e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
