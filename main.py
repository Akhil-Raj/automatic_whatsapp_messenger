import pywhatkit as kit
import os
import pandas as pd
from time import sleep
import sys

def get_pure_numbers_string(number_string):
    numbers = number_string.split("/") if "/" in number_string else number_string.split(",")
    for ind in range(len(numbers)):
        result = ""
        for char in numbers[ind]:
            if char in '+0123456789':
                result += char
        if '+91' not in result and '+1' not in result and '+95' not in result:
            result = '+1' + result
            print(f'Appended US country code to the number. New number : {result}')
        numbers[ind] = result
    return numbers

# Read the inputs 
i = 1
DATABASE_PATH_INCLUDE = sys.argv[i]
i += 1
if len(sys.argv) >= 5:
    DATABASE_PATH_EXCLUDE = sys.argv[i]
    i += 1
    df_exclude = pd.read_csv(DATABASE_PATH_EXCLUDE)
    numbers_to_exclude = []
    for index, row in df_exclude.iterrows():
        phone_numbers_string = str(row['Contact'])
        status = row["August MYF.1"]
        if status == "Registered":
            phone_numbers_string_list = get_pure_numbers_string(phone_numbers_string)
            numbers_to_exclude.extend(phone_numbers_string_list)

START_ROW_NUMBER = int(sys.argv[i])
i += 1
END_ROW_NUMBER = int(sys.argv[i])
# row number in sheet = index + 2
START_INDEX = START_ROW_NUMBER - 2
END_INDEX = END_ROW_NUMBER - 2
IMAGE_PATH = "image.jpeg"

# Ensure the image exists
if not os.path.isfile(IMAGE_PATH):
    raise FileNotFoundError(f"The image file '{IMAGE_PATH}' does not exist.")


df_include = pd.read_csv(DATABASE_PATH_INCLUDE)

# Iterate through each row in the DataFrame
for index, row in df_include.iterrows():
    if index < START_INDEX or index > END_INDEX: # Taking only relevant rows
        continue
    first_name = row['Name'].split(" ")[0]
    if first_name in ["Y", "N"]:
        first_name = row['Name'].split(" ")[1]
    if first_name == "Late":
        first_name = ""
    if first_name == "RAK":
        first_name = "Rakshit"
    phone_numbers_string = str(row['Contact No.'])
    phone_numbers_string_list = get_pure_numbers_string(phone_numbers_string)
    for phone_number in phone_numbers_string_list:
        status = "Registered"#row["August MYF.1"] # Verify row name from the csv file, it may not be same as that shown on the google sheet because there might be another row with the same google-sheet name, in which case the internal name is different.
        print(f"Index : {index}\nFirst name : {first_name}\nPhone number : {phone_number}\nStatus : {status}")
        registered_message = f"🎉 Hare Krishna {first_name}!🎉\nJoin us for a Spectacular Evening! \n\n📅 Today's the day! Don't miss out on our Monthly Youth Festival at ISKCON NYC. A night filled with divine joy, delicious prasadam, and spiritual enlightenment awaits you. 🌟\n\n📍 Venue: ISKCON NYC, 305 Schermerhorn St, Brooklyn\n\n⏰ Arrival Time: Be there by 5:30 PM sharp to immerse in the full experience.\n\n🎟 Welcome Bands: Secure yours latest by 6:30 PM at the reception. It's your key to the delightful feast prasadam. \n\nFor any queries or assistance, feel free to reach out. Can't wait to see you there! 🙏"
        reminder_message = registered_message.replace(f"🎉 Hare Krishna {first_name}!🎉", "REMINDER!!!") + "\n\nRegistration Link : https://forms.gle/BF4VDK9BGf1LGC7z8"
        first_message = f"Hare Krishna {first_name}! 🙏🏻\n\nGita Life NYC is delighted to invite you to our 16th Monthly Youth festival 🥳\n\nWhat’s in it for you?\n\nDARSHAN AND AARTI 🪔\nSPIRITUAL TALK 🎤\nDANCING KIRTAN 🪘\nPRASADAM FEAST 🥗\nSPECIAL EVENT 🪩\n\n& we will be honoring all the INSPIRE Donors!\n\nDate: August 17, 2024 (Saturday)\nTime: 5:30 PM onwards\n\nRegistration Link: https://forms.gle/BezjbytdG7F3beTV8\n\nDon't hesitate! 🤔🤔 Register now ☝🏻☝🏻☝🏻 and embrace the opportunity to interact, learn, and grow!\n\nSee you soon! 🙂"

        if status == "To be reached out":
            continue
            message = first_message
        elif status == "No" or status == "Numer Invalid / Moved out of NYC":
            continue
        elif status in ["Yes, Registration link sent", "didn't pick message sent", "Didn't pick up", "Registration sent w/o calling", "Call back/Not sure"]:
            continue
            message = reminder_message
        elif status == "Registered":
            if phone_number in numbers_to_exclude:
                continue
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
        # kit.sendwhats_image(phone_number, IMAGE_PATH, message, wait_time=7, tab_close=True)

        row['Name'] = row['Name'] + '(Done)'
        df_include.to_csv(DATABASE_PATH_INCLUDE)


print("Messages sent successfully!")
