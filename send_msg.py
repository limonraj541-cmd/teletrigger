import json
import os
from datetime import datetime
import urllib.request
import urllib.parse

# GitHub Secrets বা সরাসরি টোকেন ও চ্যাট আইডি সেট করা
BOT_TOKEN = os.getenv("BOT_TOKEN") or "9272565574:AAF0jxXhDCjN3iMNMBr4CX3mN2c0JVKc3s8"
CHAT_ID = os.getenv("CHAT_ID") or "7828803269"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": text}).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req) as response:
            print("Message sent successfully:", response.read().decode())
    except Exception as e:
        print("Failed to send message:", e)

def main():
    if not os.path.exists("messages.json"):
        print("messages.json not found!")
        return

    with open("messages.json", "r", encoding="utf-8") as f:
        schedules = json.load(f)

    # বর্তমান সময় (বাংলাদেশ সময় অনুযায়ী বা UTC টাইম) চেক করা
    now = datetime.now().strftime("%H:%M")
    print(f"Current time: {now}")

    for item in schedules:
        if item.get("time") == now:
            msg = item.get("message")
            print(f"Sending message: {msg}")
            send_telegram_message(msg)

if __name__ == "__main__":
    main()
