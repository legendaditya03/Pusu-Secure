import json
import os


def get_user_list(config, key):
    with open("{}/IRO/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it
     
    API_ID = 123456  # integer value, dont use "" this sign get it form my.telegram.org
    API_HASH = "" # get it form my.telegram.org
    TOKEN = ""  # get it form @botfather.
    OWNER_ID = 6513089685  # got to @PusuXSecure_Bot and type /id
    OWNER_USERNAME = "legend_pusu" # your telegram username
    ALLOW_CHATS = True # leave it as it is
    BOT_USERNAME = "PusuXSecure_Bot" # your bot username get it form @botfather
    SUPPORT_CHAT = "pusu_world"  # Your own group for support, do not add the @ if you dont have leave it as it is
    UPDATES_CHANNEL = "pusu_world01"  # Your own chsnnel for support, do not add the @ if you dont have leave it as it is
    JOIN_LOGGER =  (
        -1002090333689
    )  # add @PusuXSecure_Bot in your group and type /id
    EVENT_LOGS = (
        -1002090333689
    )  # add @PusuXSecure_Bot in your group and type /id
    ERROR_LOG = (
        -1002090333689
    )  # add @PusuXSecure_Bot in your group and type /id
    STRICT_GMUTE = True #to allow gmutes
    START_STICKER = "" #sticker id for start animation
    TEMP_DOWNLOAD_DIRECTORY = ". /" # dont change
    OPENWEATHERMAP_ID = None



    # RECOMMENDED
    STRING_SESSION ="" #telethon string session of user or bot get it from @Iro_string_bot
    MONGO_DB_URI = "" #get it from mongodb.com get
    ARQ_API_KEY = "" #git it form @ARQRobot
    ARQ_API_URL = "https://arq.hamker.in" # dont change
    SQLALCHEMY_DATABASE_URL = ""  # needed for any database modules get it from https://www.elephantsql.com/
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@pusu_world"


    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = [6513089685]
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = [6513089685]
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = [6513089685]
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = [6513089685]
    WOLVES = [6513089685]
    START_IMG = "https://graph.org/file/ac65ca5d3c0217acefcf9.jpg" #yor fav img link
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    REM_BG_API_KEY = "BpFP7okACX7S4rFVywGqiRHH"
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = None  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
