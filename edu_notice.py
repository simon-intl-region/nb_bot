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
                    hour=8, minute=0, second=0, microsecond=0
                ),
                "type": "EDU_1",
            },
            {
                "schedule": datetime.now().replace(
                    hour=23, minute=0, second=0, microsecond=0
                ),
                "type": "EDU_2",
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
    edu_1 = "Please schedule tomorrow daily bread"

    edu_2 = "Please send daily bread before 9am"

    return edu_1, edu_2


# Load the .env file.
load_dotenv()

# Get env variables.
bot_token = os.getenv("EDU_BOT_TOKEN")

# Telegram room id where we send the messages
# import from json file named youth_groups.json

with open("sir_edu_groups.json", "r") as f:
    edu_groups = json.load(f)

# Telegram bot API URL
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

# Function to send scheduled messages
while True:
    scheduled_times = get_schedueled_times()
    edu_1, edu_2 = get_reminder_message()

    # Send scheduled messages for the current weekday
    current_weekday = get_current_weekday()
    if -1 in scheduled_times:  # everyday messages
        for scheduled_time in scheduled_times[-1]:
            if scheduled_time["type"] == "EDU_1":
                send_scheduled_message(
                    scheduled_time["type"],
                    edu_1,
                    edu_groups,
                    scheduled_time["schedule"],
                )
            elif scheduled_time["type"] == "EDU_2":
                send_scheduled_message(
                    scheduled_time["type"],
                    edu_2,
                    edu_groups,
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
        if scheduled_time["type"] == "EDU_1":
            send_scheduled_message(
                scheduled_time["type"],
                edu_1,
                edu_groups,
                scheduled_time["schedule"],
            )
        elif scheduled_time["type"] == "EDU_2":
            send_scheduled_message(
                scheduled_time["type"],
                edu_groups,
                edu_groups,
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
