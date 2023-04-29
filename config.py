from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "20279969"))
API_HASH = getenv("API_HASH", "cceaafe470deee009bbe859fd59482fb")
BOT_TOKEN = getenv("BOT_TOKEN", "6271497235:AAFiHWF-9gMcz0B7oWE_OIMrSqfD_ZRPnPU")
SESSION_NAME = getenv("SESSION_NAME", "BABDUMFqcpvNk17ZxGOV45vWMgvnxkUc6XH2rSjrrwGyqeqWsnW0j4IeDC9iwfct_P0VSjf0lS4JiCyV6gsGG4YMUuG8R-LYxHkg5BjVT3e_PgnGdvrFLemEG6nrZYRz-UZPoaRV5pN9aol6oibUSYxEwWKOPD8jdGmQjikg9yBNMHf7BB2HYoD79kOH-CBw9FE5qTnj_6cp3ERJyFgzYvqT7Um7Y-3FvZItLUAkhAnbzKBS1KocNjCT250cLZ2HP2EOxb3JYP91vSpH3ocmoOkhIlyrQL-KfItoV6Ik3XX_fR7X8XLB53TuX9-fdvoxvaZwf1XfGQMwOMwGodznPE-EAAAAAXdbcuoA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "@C1_CU")
ALIVE_NAME = getenv("ALIVE_NAME"#ᕼEᒪᑭEᖇ⚝|ᑎᗩITᖇO𝅘𝅥𝅯<")
BOT_USERNAME = getenv("BOT_USERNAME", "DD_UC_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "mezooy")
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
