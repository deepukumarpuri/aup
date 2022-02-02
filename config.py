# <C> MoTechYT


import os

class Config(object):
    MT_BOT_TOKEN = os.environ.get("MT_BOT_TOKEN", "5275883428:AAHhHdfzclsFJZzQklwHVA9RK2Sp1HOukSw")
    API_ID = int(os.environ.get("APP_ID", 12345)
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "@Mo_Tech_YT @Mo_Tech_Group")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/DKBOTZ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Ajsjjsjssnnsnsbot")
