from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "6246896261:AAEoeINps2oQZ0hxFOwxndIuqYIxZW1CYBY")
BOT_TOKEN = getenv("BOT_TOKEN", "5385370603:AAHjSbZFL1OLl_uOm3v8lS0iKSYhRJS_bKs")
SESSION_NAME = getenv("SESSION_NAME", "BAA6lh4JtsRc4fptq8_Lk7GB8GLicJtRxxpgwguP62JOCOsVRhdzkB5eM67nY2x8DLSLg7yvdFFQOy3OiPKLXjJiIwr9UA0N2CvgEDiY_7zDZMEzjVdgzx__R-iV4jdrSaR895-0UhRZEOlFQFt06JBgp0i9bN80uezk5EQm6cj6F3NTNmLs2GiOvsPyNYtFSH04jxc_fryDfxlPzv6MEc0R3LRhmftmXsoseBR3MS7IV4yG5mzSoKcm-RixAlwEnX8_JWy6WVeCy5WpyJ97-CMkE17f9-W6LphiAdXGPR9m7Yl7q-CvR30b1pLsF9q-fR1Sv6Nc5QAVI2ZniTLu-dukAAAAAU94hDUA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "T_K_1T")
ALIVE_NAME = getenv("ALIVE_NAME", "اتشـٰـُ͢ـُٰـيڪڪو")
BOT_USERNAME = getenv("BOT_USERNAME", "UUIUU7_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "T_K_1T")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "UU_OP7")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
