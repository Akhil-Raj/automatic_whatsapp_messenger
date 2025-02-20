import pywhatkit as kit
import os
import pandas as pd
from time import sleep
import sys
import json
import pyautogui
import time
from pywhatkit.core import core
from oneClickRegistrationTest import *

# Take a screenshot and save it
def take_screenshot(save_path):
    # return
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)


def get_pure_numbers_string(number_string):
    numbers = number_string.split("/") if "/" in number_string else number_string.split(",")
    for ind in range(len(numbers)):
        result = ""
        for char in numbers[ind]:
            if char in '+0123456789':
                result += char
        if '+91' not in result and '+1' not in result and '+95' not in result:
            result = '+1' + result
            if True:
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
        phone_numbers_string = str(row['Contact Number'])
        # status = row["Sept MYF"]
        # if status == "Registered":
        if phone_numbers_string != 'nan':
            phone_numbers_string_list = get_pure_numbers_string(phone_numbers_string)
            numbers_to_exclude.extend(phone_numbers_string_list)
        
        ## Second Column
        phone_numbers_string = str(row['WhatsApp Number'])
        if phone_numbers_string != 'nan':
            # status = row["Sept MYF"]
            # if status == "Registered":
            phone_numbers_string_list = get_pure_numbers_string(phone_numbers_string)
            numbers_to_exclude.extend(phone_numbers_string_list)

START_ROW_NUMBER = int(sys.argv[i])
i += 1
END_ROW_NUMBER = int(sys.argv[i])
# row number in sheet = index + 2
START_INDEX = START_ROW_NUMBER - 2
END_INDEX = END_ROW_NUMBER - 2
IMAGE_PATH = "./image.jpeg"
# Convert to absolute path
IMAGE_PATH = os.path.abspath(IMAGE_PATH)
print("IAMGE EXISTS : ", os.path.isfile(IMAGE_PATH))

# Ensure the image exists
if not os.path.isfile(IMAGE_PATH):
    raise FileNotFoundError(f"The image file '{IMAGE_PATH}' does not exist.")


df_include = pd.read_csv(DATABASE_PATH_INCLUDE)

numbers_not_on_whatsapp = json.load(open('numbers_not_on_whatsapp.json'))['numbers']


if not os.path.exists("./screenshots"):
    os.mkdir("./screenshots")
# breakpoint()
# Iterate through each row in the DataFramels
for index, row in df_include.iterrows():
    # if row['Column 1'] != None and str(row['Column 1']).strip() == 'Present':
    #     continue
    # print(row['Column 1'], row['Column 1'] == 'Present')
    if index < START_INDEX or index > END_INDEX: # Taking only relevant rows
        continue
    first_name = row['Name'].split(" ")[0]
    if first_name in ["Y", "N"]:
        first_name = row['Name'].split(" ")[1]
    if first_name == "Late":
        first_name = ""
    if first_name == "RAK":
        first_name = "Rakshit"
    phone_numbers_string = str(row['Contact'])
    if True:
        print("original phone_numbers_string : ", phone_numbers_string)
    phone_numbers_string_list = get_pure_numbers_string(phone_numbers_string)
    # phone_numbers_string = str(row['WhatsApp Number'])
    # if phone_numbers_string != 'nan':
    #     phone_numbers_string_list.extend(get_pure_numbers_string(phone_numbers_string))
    # breakpoint()
    phone_numbers_string_list = list(set(phone_numbers_string_list))
    if True:
        print(phone_numbers_string_list)
    for phone_number in phone_numbers_string_list:
        if False:
            print(f"https://www.gitalifenyc.com/registerbylink?phone={phone_number}", end=" ")
        if False: # For Testing
            test_get_name_from_phone(phone_number)
            test_mark_registered(phone_number)

        for number in numbers_not_on_whatsapp:
            if number in phone_number:
                if True:
                    print("Number not on whatsapp : ", phone_number)
                skip = True
                break
        if False:
            continue
        # breakpoint()
        status = row['Feb MYF']
        # assert status == "To be reached out"
        if True:
            print(f"Row Number in sheet : {index + 2}\nFirst name : {first_name}\nPhone number : {phone_number}\nStatus : {status}")

        registered_message = f"""🎉 Hare Krishna!🎉
Join us for a Spectacular Evening! 

📅 Today is the day! Don't miss out on our Monthly Youth Festival at ISKCON NYC. A night filled with divine joy, delicious prasadam, and spiritual enlightenment awaits you. 🌟

📍 Venue: ISKCON NYC, 305 Schermerhorn St, Brooklyn

⏰ Arrival Time: Be there by 5:30 PM sharp to immerse in the full experience.

🎟 Welcome Bands: Secure yours latest by 6:30 PM at the reception. It's your key to the delightful feast prasadam. 

If you want to volunteer for different services, please feel free to contact (Sachin: 9296310021).

Can't wait to see you there! 🙏"""
        # reminder_message = registered_message.replace(f"🎉 Hare Krishna {first_name}!🎉", "REMINDER!!!") + "\n\nRegistration Link : https://forms.gle/BF4VDK9BGf1LGC7z8"
        reminder_message = f"Hare Krishna {first_name}! 🙏🏻\n\nRegister Now!!! 👉 https://forms.gle/P64hwdFEdzbDYyL18"
        first_message = f"""Hi {first_name}!
        
🌟 Gita Life NYC invites you for our 21st Monthly Youth Festival! 🌟

Get ready for an evening filled with inspiration, joy, and unforgettable memories! 🎉

Join us for a spiritual journey featuring:

✨ Enlightening Spiritual Talk by Tulasi Prabhu (traveling monk, author, known for his ecstatic kirtans)
🎭 Drama Performance – Witness incredible performances that will touch your heart!
🕺🏼 Dancing kirtan – Let loose, groove to the beat, and celebrate with us!
🍽️ Feast prasadam– have delicious prasadam and enjoy great company!
and much more….

🗓️ Date: 22nd February (Saturday)
🕒 Time: 5.45 PM
📍 Location: 305 Schermerhorn St. Brooklyn NY (ISKCON NYC)

Register NOW: https://www.gitalifenyc.com/registerbylink?phone={phone_number}

Share with your friends 🌟🌟🌟"""
        present_message = f"I apologize for missing the feedback form's link! Here it is : https://forms.gle/HHsP7ZHcaGCHU9H68"
        registered_but_did_not_present_message = f"Dear {first_name},\n\nWe noticed you weren’t able to join us for the Fall '24 Welcome Party at Gita Life NYC, and we just wanted to say we missed you! We had an amazing evening with kirtan, spiritual discussions, networking, and delicious prasadam.\n\nWe understand that sometimes plans change, but we hope to see you at our next event! Our community is here to support you in your journey of personal, professional, and spiritual growth.\n\nStay tuned for upcoming events, and feel free to reach out to us anytime.\n\nL ooking forward to meeting you soon,\nGita Life NYC Team"
        extra_message = f"""We have implemented one-click registration this time, so you don’t need to fill in your details manually. We would appreciate any feedback about it!"""

        if status == "To be reached out":
            # continue
            message = first_message
        elif status == "No" or status == "Numer Invalid / Moved out of NYC":
            continue
        elif status in ["Yes, Registration link sent", "didn't pick message sent", "Didn't pick up", "Registration sent w/o calling", "Call back/Not sure", "Switched Off/Out of Range"]:
            continue
            message = reminder_message
        elif status == "Registered":
            continue
            message = registered_message
        elif status == "Present":
            continue
            message = present_message
            # print("ERROR STATUS FOR ", first_name)
            # exit(1)
        elif status == "Maybe/Will try, registration link sent":
            continue
            message = ""
        # elif status == "registered_but_did_not_present":
        #     if True:
        #         print("ERROR STATUS FOR ", first_name)
            # exit(1)
        elif status == "mataji, didn't reach out":
            continue
        else :
            continue
            print("CASE NOT COVERED ERROR. STATUS : ", status)
            exit(1)
        

        if True:
            print("Sending Message :", message)
            # phone_number = "+919045907963"
            # Send the message (using the 24-hour format for the time)
            # kit.sendwhatmsg_instantly(phone_number, message, wait_time=7, tab_close=False)
            kit.sendwhats_image(phone_number, IMAGE_PATH, message, wait_time=7, tab_close=False)
            time.sleep(7)
            take_screenshot(os.path.join("./screenshots", first_name + "___" + phone_number + ".png"))
            core.close_tab(wait_time=0)

            row['Name'] = row['Name'] + '(Done)'
            df_include.to_csv(DATABASE_PATH_INCLUDE)

    print()


print("Messages sent successfully!")
