import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# tokens
BOT_TOKEN = os.getenv("TOKEN_BOT")

DOMAIN = os.getenv("DOMAIN")
PAGE_SIZE = int(os.getenv("PAGE_SIZE"))

CHAT_ID = os.getenv("CHAT_ID")
