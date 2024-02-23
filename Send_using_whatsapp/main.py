# # Importing the Required Library
# import pywhatkit
# import pyautogui
# import time

# # Defining the Phone Number and Message
# phone_number = "+919566127215"
# message = "hai this is python sened message"

# # Sending the WhatsApp Message
# pywhatkit.sendwhatmsg_instantly(phone_number, message)
# pyautogui.click()
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)
# time.sleep(2)
# # pywhatkit.sendwhatmsg("+919566127215","hai this is python sened message",13,30, 15, True, 2)

# # Displaying a Success Message
# print("WhatsApp message sent!")

import pywhatkit as kit

# Replace 'phone_number' with the recipient's phone number (including the country code)
phone_number = "+919566127215"

# Replace 'message' with the text you want to send
message = "Hello from Python! This is a test message."

# Send the WhatsApp message
kit.sendwhatmsg_instantly(phone_number, message)
