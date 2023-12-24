import json
import os
import time
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv


def print_log(message):
    print(f"[{datetime.now().strftime('%D %H:%M')}]: {message}")
    with open("log.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%D %H:%M')}]: {message}\n")


# Function to get the current weekday
def get_current_weekday():
    return datetime.now().weekday()


def send_scheduled_message(type, message, chat_ids, scheduled_time):
    current_time = datetime.now()

    if current_time.replace(second=0, microsecond=0) == scheduled_time:
        for chat_id in chat_ids:
            data = {"chat_id": chat_id, "text": message}
            response = requests.post(url, data=data)
            if response.status_code == 200:
                print_log(
                    f"Scheduled message sent successfully. TYPE: {type}, CHAT_ID: {chat_id}"
                )

                # send message to test chatroom with log
                data = {
                    "chat_id": "-4026674973",
                    "text": f"Scheduled message sent successfully. TYPE: {type}, CHAT_ID: {chat_id}",
                }
                response = requests.post(url, data=data)

            else:
                print_log(
                    f"Failed to send scheduled message: TYPE: {type}, CHAT_ID: {chat_id} {response.status_code}"
                )

                # send message to test chatroom with log
                data = {
                    "chat_id": "-4026674973",
                    "text": f"Failed to send scheduled message: TYPE: {type}, CHAT_ID: {chat_id} {response.status_code}",
                }
    else:
        print_log(f"The scheduled time has already passed. The message was not sent.")


def get_schedueled_times():
    # Messages for compiling attendance
    return {
        -1: [
            {
                "schedule": datetime.now().replace(
                    hour=9, minute=0, second=0, microsecond=0
                ),
                "type": "YOUTH",
            },
            {
                "schedule": datetime.now().replace(
                    hour=12, minute=0, second=0, microsecond=0
                ),
                "type": "YOUTH",
            },
            {
                "schedule": datetime.now().replace(
                    hour=18, minute=0, second=0, microsecond=0
                ),
                "type": "YOUTH",
            },
            {
                "schedule": datetime.now().replace(
                    hour=21, minute=0, second=0, microsecond=0
                ),
                "type": "YOUTH",
            },
            {
                "schedule": datetime.now().replace(
                    hour=22, minute=0, second=0, microsecond=0
                ),
                "type": "YOUTH",
            },
            {
                "schedule": datetime.now().replace(
                    hour=9, minute=0, second=0, microsecond=0
                ),
                "type": "SIR",
            },
            {
                "schedule": datetime.now().replace(
                    hour=18, minute=0, second=0, microsecond=0
                ),
                "type": "SIR",
            },
            # TEST TIMES
            {
                "schedule": datetime.now().replace(
                    hour=11, minute=6, second=0, microsecond=0
                ),
                "type": "TEST",
            },
            {
                "schedule": datetime.now().replace(
                    hour=11, minute=6, second=0, microsecond=0
                ),
                "type": "TEST",
            },
        ],  # Everyday
    }


def get_reminder_message():
    # Enter the message content to send.
    # final date is Dec 26, 2023
    final_date = datetime.strptime("2024-01-10", "%Y-%m-%d")
    d_string = "D-" + str((final_date - datetime.now()).days)
    youth_message = f"""(글특알리미) 마나도 소성에 함께할 수 있는날이 💥{d_string}💥밖에 안남았다는 소식!
    인도네시아 해외소성에 함께할 수 있는 날이 얼마남지 않았어요 😭
    이 기회 놓치면 너무 아쉬우니까 
    지금 당장 DM 보내러 고고🔥
    """

    sir_message = f"""[💥{d_string} left till Dec CT]
    GYJNs, secure your ✨blessings✨today by checking if your members have NBed!! Deadline to send the report is till 11pm. Go check now!! 👉
    """

    return youth_message, sir_message


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

# Telegram bot API URL
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# Function to send scheduled messages
while True:
    scheduled_times = get_schedueled_times()
    youth_message, sir_message = get_reminder_message()

    # Send scheduled messages for the current weekday
    current_weekday = get_current_weekday()
    if -1 in scheduled_times:  # everyday messages
        for scheduled_time in scheduled_times[-1]:
            if scheduled_time["type"] == "YOUTH":
                send_scheduled_message(
                    scheduled_time["type"],
                    youth_message,
                    youth_groups,
                    scheduled_time["schedule"],
                )
            elif scheduled_time["type"] == "SIR":
                send_scheduled_message(
                    scheduled_time["type"],
                    sir_message,
                    sir_groups,
                    scheduled_time["schedule"],
                )
            elif scheduled_time["type"] == "TEST":
                send_scheduled_message(
                    scheduled_time["type"],
                    "This is a test message",
                    ["-4026674973"],
                    scheduled_time["schedule"],
                )

    if current_weekday in scheduled_times:  # weekday messages
        scheduled_time = scheduled_times[current_weekday]
        # check type
        if scheduled_time["type"] == "YOUTH":
            send_scheduled_message(
                scheduled_time["type"],
                youth_message,
                youth_groups,
                scheduled_time["schedule"],
            )
        elif scheduled_time["type"] == "SIR":
            send_scheduled_message(
                scheduled_time["type"],
                sir_message,
                sir_groups,
                scheduled_time["schedule"],
            )
        elif scheduled_time["type"] == "TEST":
            send_scheduled_message(
                scheduled_time["type"],
                "This is a test message",
                ["-4026674973"],
                scheduled_time["schedule"],
            )
    else:
        pass

    # sleep for the rest of the minute
    time.sleep(60 - datetime.now().second)
pass  # This line is necessary to prevent the loop from terminating.
