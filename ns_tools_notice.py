import os
import time
from datetime import datetime, timedelta
import json

import requests
from dotenv import load_dotenv


def send_scheduled_message(message, chat_ids, scheduled_time):
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

with open("sir_groups.json", "r") as f:
    sir_groups = json.load(f)

# Set the desired year.
desired_year = "40"

# 현재 날짜와 시간을 가져옵니다.
current_date = datetime.now()

# Get the current date and time.
current_date = current_date.replace(year=int(desired_year))

# Change the date to the desired year.
newdate = current_date.strftime(f"{desired_year}%m%d")

# Enter the message content to send.
# final date is Dec 26, 2023
final_date = datetime.strptime("2023-12-28", "%Y-%m-%d")
d_string = "D-" + str((final_date - datetime.now()).days)
message = f"""(글특알리미) 마나도 소성에 함께할 수 있는날이 💥{d_string}💥밖에 안남았다는 소식!
인도네시아 해외소성에 함께할 수 있는 날이 얼마남지 않았어요 😭
이 기회 놓치면 너무 아쉬우니까 
지금 당장 DM 보내러 고고🔥
"""

sir_message = f"""[💥{d_string} left till Dec CT]
GYJNs, secure your ✨blessings✨today by checking if your members have NBed!! Deadline to send the report is till 11pm. Go check now!! 👉
"""

# Messages for compiling attendance
youth_scheduled_times = {
    # if -1, then send message at 9, 12, 18, 21 o'clock everyday
    -1: [
        datetime.now().replace(hour=9, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=12, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=18, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=21, minute=0, second=0, microsecond=0),
    ],  # Everyday
}

sir_scheduled_times = {
    # if -1, then send message at 8, 21, 22 o'clock everyday
    -1: [
        datetime.now().replace(hour=8, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=21, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=22, minute=00, second=0, microsecond=0),
    ],  # Everyday
}

# Telegram bot API URL
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

count = 0

# Function to send scheduled messages
while True:
    # Function to get the current weekday
    def get_current_weekday():
        return datetime.now().weekday()

    # Send scheduled messages for the current weekday
    current_weekday = get_current_weekday()
    if -1 in youth_scheduled_times:  # everyday messages
        for scheduled_time in youth_scheduled_times[-1]:
            send_scheduled_message(message, youth_groups, scheduled_time)
            print(f"Group message sending completed. [Round {count}]")

    if -1 in sir_scheduled_times:  # everyday messages
        for scheduled_time in sir_scheduled_times[-1]:
            send_scheduled_message(sir_message, sir_groups, scheduled_time)
            print(f"Group message sending completed. [Round {count}]")

    if current_weekday in youth_scheduled_times:  # weekday messages
        scheduled_time = youth_scheduled_times[current_weekday]
        send_scheduled_message(message, youth_groups, scheduled_time)
        print(f"Group message sending completed. [Round {count}]")
    elif current_weekday in sir_scheduled_times:  # weekday messages
        scheduled_time = sir_scheduled_times[current_weekday]
        send_scheduled_message(sir_message, sir_groups, scheduled_time)
        print(f"Group message sending completed. [Round {count}]")
    else:
        print(f"Today is not the day to send scheduled messages. [Round {count}]")
pass  # This line is necessary to prevent the loop from terminating.
