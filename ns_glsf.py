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

# # Set the desired year.
# desired_year = '40'
# desired_day = '19'

# # Get the current date and time.
# current_date = datetime.now()

# # Change the date to the desired year.
# current_date = current_date.replace(year=int(desired_year))

# # Format the date in the desired format. (e.g., YYYY-MM-DD)
# newdate = current_date.strftime(f'{desired_year}%m%{desired_day}')

# Enter the message content to send.
message_notice = """
Message from Global Friend to Tech Team Room 🌟
"""

# Text message to send to the tech team room.
message_encourage_screenshot = """
[🌟🏔️ 저는 글로벌특전대 알리미 SATU 🏔️🌟]\n\n
✨ 오늘은 예배날 🔖\n
오늘은 영들과 하나되어 말씀으로 나를 씻는 시간이예요! 한 번 마음내서 준비해볼까요?\n
그리고 예배 후 꼭 '인증!' 부탁드릴게요 :)\n
오늘도 짧게나마 활동 후 보고부탁드려요~~!\n\n
예배 인증 🤳
구님과 소통 💕 
나를 씻는 소중한 시간 🐳
저는 글로벌특전대 알리미 SATU 🏔️
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
