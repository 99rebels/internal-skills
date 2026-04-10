#!/usr/bin/env python3
import os
import sys
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Read the pulse message
with open('/home/rianoleary/.openclaw/workspace/skills/ecosystem-radar/pulse_message.txt', 'r') as f:
    message = f.read()

# Use the bot token from the configuration
bot_token = "xoxb-8992089259041-10846009639297-rI9UVDQQ7lZsOCpCGcNtFdb7"

try:
    client = WebClient(token=bot_token)
    response = client.chat_postMessage(
        channel="C0AQF46E50E",  # Direct channel ID
        text=message
    )
    print(f"Message sent successfully: {response['ts']}")
    sys.exit(0)
except SlackApiError as e:
    print(f"Slack API error: {e.response['error']}")
    sys.exit(1)