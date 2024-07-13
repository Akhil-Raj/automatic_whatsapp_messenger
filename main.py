import pywhatkit as kit
import os
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
IMAGE_PATH = "image.jpeg"

# Ensure the image exists
if not os.path.isfile(IMAGE_PATH):
    raise FileNotFoundError(f"The image file '{IMAGE_PATH}' does not exist.")


df = pd.read_csv(DATABASE_PATH)

def get_pure_number(number):
    result = ""
    for char in number:
        if char in '+0123456789':
            result += char
    return result

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    if index < START_INDEX or index > END_INDEX: # Taking only relevant rows
        continue
    first_name = row['Name'].split(" ")[0]
    if first_name == "Y":
        first_name = "Manikanta"
    phone_number = str(row['Contact'])
    phone_number = get_pure_number(phone_number)
    status = row["July MYF.1"]
    print(f"Index : {index}\nFirst name : {first_name}\nPhone number : {phone_number}\nStatus : {status}")
    if '+91' not in phone_number and '+1' not in phone_number:
        phone_number = '+1' + phone_number
        print(f'Appended US country code to the number. New number : {phone_number}')
    registered_message = f"🎉 Hare Krishna {first_name}!🎉\nJoin us for a Spectacular Evening!\n\n📅 Tomorrow's the day! Don't miss out on our Monthly Youth Festival at ISKCON NYC. A night filled with divine joy, delicious prasadam, and spiritual enlightenment awaits you. 🌟\n\n📍 Venue: ISKCON NYC, 305 Schermerhorn St, Brooklyn\n\n⏰ Arrival Time: Be there by 5:30 PM sharp to immerse in the full experience.\n\n🎟 Welcome Bands: Secure yours latest by 6:30 PM at the reception. It's your key to the delightful feast prasadam. \n\nFor any queries or assistance, feel free to reach out. Can't wait to see you there! 🙏"
    reminder_message = registered_message.replace(f"🎉 Hare Krishna {first_name}!🎉", "REMINDER!!!") + "\n\nRegistration Link : https://forms.gle/BF4VDK9BGf1LGC7z8"
    first_message = f"Hare Krishna {first_name}! 🙏\n\nGita Life NYC is delighted to invite you to our 15th Monthly Youth festival 🥳\n\nWhat’s in it for you?\n\nDARSHAN AND AARTI 🪔\nSPIRITUAL TALK 🎤\nDANCING KIRTAN 🪘\nPRASADAM FEAST 🥗\nSPECIAL EVENT 🪩\n\nDate: July 13, 2024 (Saturday)\nTime: 5:30 PM onwards\n\nRegistration Link: https://forms.gle/BF4VDK9BGf1LGC7z8\n\nDon't hesitate! 🤔🤔 Register now ☝🏻☝🏻☝🏻 and embrace the opportunity to interact, learn, and grow!\n\nSee you soon! 🙂"

    if status == "To be reached out":
        message = first_message
    elif status == "No" or status == "Numer Invalid / Moved out of NYC":
        continue
    elif status in ["Yes, Registration link sent", "didn't pick message sent", "Didn't pick up", "Registration sent w/o calling", "Call back/Not sure"]:
        message = reminder_message
    elif status == "Registered":
        message = registered_message
    elif status == "Present":
        print("ERROR STATUS FOR ", first_name)
        exit(1)
    else :
        print("CASE NOT COVERED ERROR. STATUS : ", status)
        exit(1)

    print("Sending Message :", message)

    # phone_number = "+919045907963"
    # Send the message (using the 24-hour format for the time)
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=7, tab_close=True)

    row['Name'] = row['Name'] + '(Done)'
    df.to_csv(DATABASE_PATH)

print("Messages sent successfully!")
