import os
import time
from datetime import datetime, timedelta
import json

import requests
from dotenv import load_dotenv


def send_scheduled_message(message, chat_id, scheduled_time):
    current_time = datetime.now()
    if current_time < scheduled_time:
        time_difference = scheduled_time - current_time
        time.sleep(time_difference.total_seconds())

        for chat_id in chat_ids:
            data = {"chat_id": chat_id, "text": message}
            response = requests.post(url, data=data)
            if response.status_code == 200:
                print(f"[Test] Scheduled message sent successfully.")
            else:
                print(
                    f"Failed to send scheduled message: [Namyeong] {response.status_code}"
                )
    else:
        print(f"The scheduled time has already passed. The message was not sent.")
        time.sleep(1)


# Load the .env file.
load_dotenv()

# Get env variables.
bot_token = os.getenv("BOT_TOKEN")

# Telegram room id where we send the messages
# import from json file named youth_groups.json
with open("youth_groups.json", "r") as f:
    youth_groups = json.load(f)

chat_ids = youth_groups

# Set the desired year.
desired_year = "40"

# 현재 날짜와 시간을 가져옵니다.
current_date = datetime.now()

# Get the current date and time.
current_date = current_date.replace(year=int(desired_year))

# Change the date to the desired year.
newdate = current_date.strftime(f"{desired_year}%m%d")

# Enter the message content to send.
final_date = datetime.now() + timedelta(days=13)
d_string = "D-" + str((final_date - datetime.now()).days)
message = f"""(글특알리미) 마나도 소성에 함께할 수 있는날이 💥{d_string}💥밖에 안남았다는 소식!
인도네시아 해외소성에 함께할 수 있는 날이 얼마남지 않았어요 😭
이 기회 놓치면 너무 아쉬우니까 
지금 당장 DM 보내러 고고🔥
"""

# Messages for compiling attendance
scheduled_times = {
    # if -1, then send message at 9, 12, 18, 21 o'clock everyday
    -1: [
        datetime.now().replace(hour=9, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=12, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=18, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=21, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=23, minute=35, second=0, microsecond=0),
    ],  # Everyday
    # 0: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Monday
    # 1: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Tuesday
    # 2: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Wednesday
    # 3: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Thursday
    # 4: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Friday
    # 5: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Saturday
    # 6: datetime.now().replace(hour=10, minute=45, second=0, microsecond=0),  # Sunday
}

# Telegram bot API URL
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# Function to send scheduled messages
while True:
    # Function to get the current weekday
    def get_current_weekday():
        return datetime.now().weekday()

    # Send scheduled messages for the current weekday
    current_weekday = get_current_weekday()
    if -1 in scheduled_times:  # everyday messages
        for scheduled_time in scheduled_times[-1]:
            send_scheduled_message(message, chat_ids, scheduled_time)
            print("Group message sending completed. [0th round]")

    if current_weekday in scheduled_times:  # weekday messages
        scheduled_time = scheduled_times[current_weekday]
        print("[1st round] Group message sending completed.")
        send_scheduled_message(message, chat_ids, scheduled_time)  # 남영
        print("Group message sending completed. [1st round]")
    else:
        print("Today is not the day to send scheduled messages. [1st round]")
pass  # This line is necessary to prevent the loop from terminating.
