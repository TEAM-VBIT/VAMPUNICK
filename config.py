#ALONE CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "34708578"))
        self.API_HASH = getenv("API_HASH", "d532e5b947d462f858077d614f31f22b")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8949527149:AAFmjNfGT_SIgvWAREcCLhOFxLPCB_2dXcY")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Jani_Sanatani_Power:RamRP@jani.elxnxrd.mongodb.net/?appName=Jani")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1002654645615"))
        self.OWNER_ID = int(getenv("OWNER_ID", "8740084288"))
        
        self.SESSION1 = getenv("SESSION", "BQC86fAAaX03BgMmTcYaLAkc0Aa6dYiF3CNc29j8QIjtJK-Wt2e-xmG0ZpKCo8Ipzy6wqta0PePYuSmi28_X0hDAD5NDCFC6qwutmV6u3MaKq8pfxT7vbY1qEbr_mNjPq5KdUPUjuMFTjoQLTusUwQvwf5lwuhE0P2lhZfyPlCXocc-CuRrl-jgWUJn0uDizNeyTedls9VxrgRsm3LtwOrSRDJhD3uYaEqncD1LhnO4UyfZgHO5ZrOqd5JUiGUrYbH_tqK0PLCdmInFyFwyM_lSlEX7a8htGtxb_BwojEkIo9VrtIBCVtkUynYsTEN2xsmHvbrKIiYUvQ4ETNDAOgstVUE_1jQAAAAIOLarHAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/anjalixupdate")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+xnUCDYVIAONlMzNl")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "99999999999"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY", "INFLEX68575028D")
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
