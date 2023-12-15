import os
import time
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Updater,
    filters,
)

# Load the .env file.
load_dotenv()

# Get env variables.
bot_token = os.getenv("BOT_TOKEN")

# Enter the target chat ID.
chat_id_gbtf = ["-4080996432"]

# Enter the message content to send.
final_date = datetime.strptime("2023-12-28", "%Y-%m-%d")
d_string = "D-" + str((final_date - datetime.now()).days)
message_notice = f"""(글특알리미) 마나도 소성에 함께할 수 있는날이 💥{d_string}💥밖에 안남았다는 소식!
인도네시아 해외소성에 함께할 수 있는 날이 얼마남지 않았어요 😭
이 기회 놓치면 너무 아쉬우니까 
지금 당장 DM 보내러 고고🔥
"""

# Telegram bot API URL.
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# Send a request to send the message.
# data1 = {'chat_id': chat_id, 'text': message_notice}
# response1 = requests.post(url, data=data1)

# Global Special Forces Operation Room.
for chat_id in chat_id_gbtf:
    data2 = {"chat_id": chat_id, "text": message_notice}
    response = requests.post(url, data=data2)
