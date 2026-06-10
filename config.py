#ALONE CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "34708578"))
        self.API_HASH = getenv("API_HASH", "d532e5b947d462f858077d614f31f22b")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8986039564:AAHGOtou4rRK3LIqlKMX1o1FcWMBbtE9kqs")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Jani_Sanatani_Power:RamRP@jani.elxnxrd.mongodb.net/?appName=Jani")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1001962121217"))
        self.OWNER_ID = int(getenv("OWNER_ID", "8092368726"))
        
        self.SESSION1 = getenv("SESSION", "BQIRnGIAaiLPqb2nU3ROlOxKedRySKq2FfEZ_ZsYLhFHCcvPahIztT_hXHfP47irz_NnpiS1r4Ryx6qbAawGYdoU0PYReNpdGqe9vtdz0uju6-rKpgrD-y8CgMYKPSENKtEYPDQOZuHtnzC6vRriddVVbNDMGaQ9qj1l9gZdHUPQjMqvbCdGs0lxI59L5MEvToXVFu5va2p3OadQ7z4gU1iif-LsGkiz-LRFh9n0cxpAXfi3olDQAK6L37lXykCFz9KOwAGLafv_Vca9B9S4gMI4goloXchSZ6yWh8HDU0c7X8E6eJUJmJkk9KHY6qqnZPt5eFLYm7uyi-hYTOkhMWiSZ3Lz-wAAAAIEfEdeAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Jani_Ki_Jaanu")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+xnUCDYVIAONlMzNl")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "99999999999"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY", "INFLEX87773028D")
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/wn3ool.jpg")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/wn3ool.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
