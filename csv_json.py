import pandas as pd
import json

# Read the CSV file
df = pd.read_csv("./data.csv")

chatroom_links = df["채팅방 링크 (Chatroom link)"]

# only keep the # number part of the link with the hashtag
chatroom_links = chatroom_links.str.split("#").str[1]
# remove nan
chatroom_links = chatroom_links.dropna()

# Convert the column to a list
chatrooms = chatroom_links.tolist()

# Save the list as JSON in youth_groups.json
with open("./youth_groups.json", "w") as file:
    file.write(json.dumps(chatrooms))
