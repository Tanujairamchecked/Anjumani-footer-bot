# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 1234567))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5575527838:AAFTFsaENJdgfSeQaVs4rREL1Hmgu3IQPdM")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Footer-Bot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    START_TEXT = """
Hi, I am a anjumani foter Bot,From @anjumani_zone team!

I can add footer to Channel Media Messages. Just add me to the channel as Admin with all rights and setup /settings !!
"""
