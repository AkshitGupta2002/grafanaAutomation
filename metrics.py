#!/usr/bin/env python3
from skpy import Skype
from apicalls import main
from datetime import datetime
import pytz
import os


username = os.getenv('SKYPE_USERNAME')
password = os.getenv('SKYPE_PASSWORD')
print(username)


# Replace with your Skype credentials
ist = pytz.timezone('Asia/Kolkata')
timestamp = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
print(username)
skype = Skype(username, password)  # Log in to Skype
print("Chats in your account:")


# Access the Skype group chat
group_chat = skype.chats["19:8215a495d7b843508c767c65fe4acb93@thread.skype"]
metrics = main()
cpu = metrics.get("cpu_utilization", 0)  # Default to 0 if not found
memory = metrics.get("memory_utilization", 0)  # Default to 0 if not found
latency = metrics.get("latency", 0)  # Default to 0 if not found
request_count = metrics.get("request_count", 0)  # Default to 0 if not found
http_2xx_errors = metrics.get("http_2xx_errors", 0)  # Default to 0 if not found
http_3xx_errors = metrics.get("http_3xx_errors", 0)  # Default to 0 if not found
http_4xx_errors = metrics.get("http_4xx_errors", 0)  # Default to 0 if not found
http_5xx_errors = metrics.get("http_5xx_errors", 0)  # Default to 0 if not found

if(latency>1):
    colour_latency = "Red"
colour_latency = "Green"

# Send "Hello World" to the group
message = (
        
    f"Server Metrics Update ({timestamp}):\n"
    f"API \n"
    f"CPU Utilization: {cpu:.2f}%\n"
    f"Memory Utilization: {memory:.2f}%\n"
    f"Latency: {latency:.2f} ms [{colour_latency}]\n"
    f"Request Count: {request_count}\n"
    f"HTTP 2XX Errors: {http_2xx_errors}\n"
    f"HTTP 3XX Errors: {http_3xx_errors}\n"
    f"HTTP 4XX Errors: {http_4xx_errors}\n"
    f"HTTP 5XX Errors: {http_5xx_errors}"
)
# Send the message to the Skype group
group_chat.sendMsg(message)
print(f"Message sent to group: {message}")