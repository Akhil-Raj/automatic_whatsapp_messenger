import pywhatkit as kit
import pandas as pd
from time import sleep
import sys

# Read the CSV file
DATABASE_PATH = sys.argv[1]
START_ROW_NUMBER = int(sys.argv[2])
END_ROW_NUMBER = int(sys.argv[3])
# row number in sheet = index + 2
START_INDEX = START_ROW_NUMBER - 2
END_INDEX = END_ROW_NUMBER - 2
IMAGE_PATH = "/Volumes/Akhil/GitHubRepos/automatic_whatsapp_messager/image.jpeg"

df = pd.read_csv(DATABASE_PATH)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    if index < START_INDEX or index > END_INDEX: # Taking only relevant rows
        continue
    first_name = row['Name'].split(" ")[0]
    phone_number = row['Contact']
    print(f"Index : {index}\nFirst name : {first_name}\nPhone number : {phone_number}\n\n")
    if '+91' not in phone_number and '+1' not in phone_number:
        phone_number = '+1' + phone_number
        print(f'Appended US country code to the number. New number : {phone_number}')
    message = f"Hare Krishna {first_name}! 🙏\n\nGita Life NYC is delighted to invite you to our 15th Monthly Youth festival 🥳\n\nWhat’s in it for you?\n\nDARSHAN AND AARTI 🪔\nSPIRITUAL TALK 🎤\nDANCING KIRTAN 🪘\nPRASADAM FEAST 🥗\nSPECIAL EVENT 🪩\n\nDate: July 13, 2024 (Saturday)\nTime: 5:30 PM onwards\n\nRegistration Link: https://forms.gle/BF4VDK9BGf1LGC7z8\n\nDon't hesitate! 🤔🤔 Register now ☝🏻☝🏻☝🏻 and embrace the opportunity to interact, learn, and grow!\n\nSee you soon! 🙂"

    # Send the message (using the 24-hour format for the time)
    kit.sendwhats_image(phone_number, IMAGE_PATH, message, wait_time=7, tab_close=True)

    row['Name'] = row['Name'] + '(Done)'
    df.to_csv(DATABASE_PATH)

print("Messages sent successfully!")

