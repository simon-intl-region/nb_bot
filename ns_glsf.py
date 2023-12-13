import time
from datetime import datetime, timedelta

import requests
from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Updater,
    filters,
)

# 봇 토큰을 입력하세요.
bot_token = "5742885964:AAH2Wi0XvA_kRxoFSb1oz5mLTavqmXczN2g"

# 대상 채팅 ID를 입력하세요.
chat_id_gbtf = ["-4080996432"]

# # 원하는 년도를 설정합니다.
# desired_year = '40'
# desired_day = '19'

# # 현재 날짜와 시간을 가져옵니다.
# current_date = datetime.now()

# # 원하는 년도로 날짜를 변경합니다.
# current_date = current_date.replace(year=int(desired_year))

# # 날짜를 원하는 형식으로 포맷팅합니다. (예: YYYY-MM-DD)
# newdate = current_date.strftime(f'{desired_year}%m%{desired_day}')

# 보낼 메세지 내용을 입력하세요.
message_notice = """
Testing 2
"""

# text message to send to tech team room
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

# 텔레그램 봇 API URL
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# 메세지를 보내는 요청 보내기
# data1 = {'chat_id': chat_id, 'text': message_notice}
# response1 = requests.post(url, data=data1)

# 글로벌특전대 운영방
for chat_id in chat_id_gbtf:
    data2 = {"chat_id": chat_id, "text": message_notice}
    response = requests.post(url, data=data2)
