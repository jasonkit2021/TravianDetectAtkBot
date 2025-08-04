# Reminder:
# Please review the functions "f5()" and "changeTab()" because different OSs or browsers may have different shortcut
# Please input the information of your smtp server or discord

# Wait Time
INTERVAL_MONITOR_BASE = 2 # in second
INTERVAL_MONITOR_Q = 6 # deviation => add some "random" to pretend "human"
TIME_TAB_LOAD = 2
TIME_F5_LOAD = 10
DONT_SEND_AGAIN_TIME = 3600 # after an email is sent, wait an hour to send again

# Msg
SUBJECT = "Travian - attack coming"
BODY = "Detail: not available"

# Email
PORT = 587
SMTP_SERVER = "" # e.g. "smtp.gmail.com"
SMTP_PW = "" # smtp password
SENDER = "" # email address for sender
RECEIVER = "" # email address for receiver
EMAIL_ENABLE = True

# Discord
DISCORD_WEBHOOK_URL = "" # your webhook URL
DISCORD_ENABLE = True

import pyautogui
import time
import random
import smtplib
from email.mime.text import MIMEText
import easyocr
import numpy as np
import warnings
import requests
import json

print("init")

# Init
warnings.filterwarnings("ignore")
reader = easyocr.Reader(['en'], gpu = True)
print("started")

# Create MIMEText object
msg = MIMEText(BODY)
msg["Subject"] = SUBJECT
msg["From"] = SENDER
msg["To"] = RECEIVER

# Msg object
payload = { "content": SUBJECT }
headers = { "Content-Type": "application/json" }

def sendEmail():
    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.starttls()
        server.login(SENDER, SMTP_PW)
        server.send_message(msg)
        server.quit()

def sendDiscord():
    response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

def f5():
    pyautogui.hotkey('command','r') # for Mac
    #pyautogui.hotkey('f5') # for Windows or Linux

def changeTab():
    pyautogui.hotkey('ctrl','shift','tab')

lastSentTime = time.time() - DONT_SEND_AGAIN_TIME
while True:
    time.sleep(INTERVAL_MONITOR_BASE + random.random() * INTERVAL_MONITOR_Q)
    changeTab() # switch to other villages
    time.sleep(TIME_TAB_LOAD)
    f5()
    time.sleep(TIME_F5_LOAD) # wait browser to load

    # monitor if there is any incoming war
    screenshot = pyautogui.screenshot()
    imgOriginal = np.array(screenshot)

    recognizedThings = reader.readtext(imgOriginal)
    hasAttack = False
    hasIncoming = False
    for bbox, text, confidence in recognizedThings:
        if 'Incoming' in text and hasIncoming == False:
            hasIncoming = True
        if 'Attack' in text and hasIncoming == True:
            hasAttack = True
        if 'Outgoing' in text:
            break
    
    if hasAttack:
        print("danger")
        if time.time() > lastSentTime + DONT_SEND_AGAIN_TIME:
            if EMAIL_ENABLE:
                sendEmail()
            if DISCORD_ENABLE:
                sendDiscord()
            print("sent")
            lastSentTime = time.time()
    if not hasAttack:
        print("peaceful")
