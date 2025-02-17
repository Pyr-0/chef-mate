import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Securely access credentials
ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Masterschool API Base URL
BASE_URL = "http://hackathons.masterschool.com:3030"

def get_messages():
    """Fetch incoming WhatsApp messages for the given Twilio account."""
    url = f"{BASE_URL}/whatsapp/getMessages/{ACCOUNT_SID}"
    print(f"Fetching messages from: {url}")

    response = requests.get(url)

    print(f"Response Status: {response.status_code}")
    print(f"Response Data: {response.text}")

    return response.json() if response.status_code == 200 else {"error": "Failed to retrieve messages"}

def get_message_status():
    """Retrieve the status of WhatsApp messages for the given Twilio account."""
    url = f"{BASE_URL}/whatsapp/getMessageStatus/{ACCOUNT_SID}"
    print(f"Fetching message status from: {url}")

    response = requests.get(url)

    print(f"Response Status: {response.status_code}")
    print(f"Response Data: {response.text}")

    return response.json() if response.status_code == 200 else {"error": "Failed to retrieve message status"}

def send_message(phone_number, message):
    """Send a WhatsApp message via the Masterschool API."""
    url = f"{BASE_URL}/whatsapp/sendMessage"
    
    payload = {
        "phoneNumber": phone_number,
        "message": message,
        "accountSid": ACCOUNT_SID,
        "authToken": AUTH_TOKEN
    }
    
    headers = {"Content-Type": "application/json"}
    
    print("\n--- Sending Message ---")
    print(f"Sending request to: {url}")
    # print(f"Payload: {payload}")

    response = requests.post(url, json=payload, headers=headers)

    print(f"Response Status: {response.status_code}")
    #print(f"Response Content: {response.text}")

    return response.json() if response.status_code == 200 else {"error": "Failed to send message", "status_code": response.status_code}

def process_messages():
    """Continuously fetch new messages and process them."""
    seen_messages = set()  # To avoid processing the same message multiple times
    
    while True:
        print("\nChecking for new messages...")
        messages = get_messages()
        
        for msg in messages:
            message_sid = msg.get("messageSid")
            message_content = msg.get("data", {}).get("text", "No content")

            if message_sid not in seen_messages:
                print(f"New Message Received: {message_content}")
                
                # Example: Auto-reply
                sender = msg.get("data", {}).get("from", "Unknown")
                send_message(sender, f"Auto-reply: Received your message - {message_content}")

                seen_messages.add(message_sid)  # Mark message as processed

        time.sleep(40)  # Wait 5 seconds before fetching again
process_messages()

# Example usage
if __name__ == "__main__":
    phone = "whatsapp:+4917647313187"  # Replace with actual WhatsApp number
    message_text = "Hello from Python!"

    # print("\nFetching messages...")
    # print(get_messages())

    # print("\nFetching message status...")
    # print(get_message_status())

    # print("\nSending message...")
    # print(send_message(phone, message_text))