import os

from dotenv.main import load_dotenv

load_dotenv()

# Discord config
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
BOT_PREFIX = "?"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
