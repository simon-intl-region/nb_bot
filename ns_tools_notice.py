import os
import time
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

# Load the .env file.
load_dotenv()

# Get env variables.
bot_token = os.getenv("BOT_TOKEN")

# Telegram room id where we reserve the messages
chat_id_ny = ["-4080996432"]

# Set the desired year.
desired_year = "40"

# 현재 날짜와 시간을 가져옵니다.
current_date = datetime.now()

# Get the current date and time.
current_date = current_date.replace(year=int(desired_year))

# Change the date to the desired year.
newdate = current_date.strftime(f"{desired_year}%m%d")

# Enter the message content to send.
message = f"""
☁️{newdate} Scheduled Message from Global Friend to Tech Team Room 🌟
"""

# Messages for compiling attendance
scheduled_times1 = {
    1: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Monday
    2: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Tuesday
    3: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Wednesday
    4: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Thursday
    5: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Friday
    6: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Saturday
}

# Telegram bot API URL
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# Function to send scheduled messages
while True:

    def send_scheduled_message(message, chat_id, scheduled_time):
        current_time = datetime.now()
        if current_time < scheduled_time:
            time_difference = scheduled_time - current_time
            time.sleep(time_difference.total_seconds())

            for chat_id in chat_id_ny:  # 남영
                data = {"chat_id": chat_id, "text": message}
                response = requests.post(url, data=data)
                if response.status_code == 200:
                    print(f"[Namyeong Test] Scheduled message sent successfully.")
                else:
                    print(
                        f"Failed to send scheduled message: [Namyeong] {response.status_code}"
                    )

            # for chat_id in chat_id_hg: #한강테스트
            #     data = {'chat_id': chat_id, 'text': message}
            #     response = requests.post(url, data=data)
            #     if response.status_code == 200:
            #         print(f"[한강 테스트] 예약 메시지가 성공적으로 보내졌습니다.")
            #     else:
            #         print(f"예약 메시지 보내기 실패: [한강] {response.status_code}")
        else:
            print(f"The scheduled time has already passed. The message was not sent.")
            time.sleep(1)

    # Function to get the current weekday
    def get_current_weekday():
        return datetime.now().weekday()

    # Send scheduled messages for the current weekday
    current_weekday = get_current_weekday()
    if current_weekday in scheduled_times1:  # 주일예배
        scheduled_time = scheduled_times1[current_weekday]
        print("[1st round] Group message sending completed.")
        send_scheduled_message(message, chat_id_ny, scheduled_time)  # 남영
        print("Group message sending completed. [1st round]")
    else:
        print("Today is not the day to send scheduled messages. [1st round]")
pass  # This line is necessary to prevent the loop from terminating.
