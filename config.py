# <C> MoTechYT


import os

class Config(object):
    MT_BOT_TOKEN = os.environ.get("MT_BOT_TOKEN", "5275883428:AAHhHdfzclsFJZzQklwHVA9RK2Sp1HOukSw")
    API_ID = int(os.environ.get("APP_ID", 7186421))
    API_HASH = os.environ.get("API_HASH", "170ea0505f96effeab358a6115b8d4e8")
    CAPTION = os.environ.get("CAPTION", "@Mo_Tech_YT @Mo_Tech_Group")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/DKBOTZ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Ajsjjsjssnnsnsbot")
