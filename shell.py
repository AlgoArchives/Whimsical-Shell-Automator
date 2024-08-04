import time
import random
import os
import sys
import threading
import requests
from apikey import EMOJI_API_KEY, QUOTES_API_KEY
from fortunes import FORTUNES

# Typing messages
typing_messages = [
    "Typing...",
    "Thinking...",
    "Processing...",
    "Loading...",
    "Calculating..."
]

# Function to fetch a random emoji from an API
def fetch_random_emoji():
    try:
        response = requests.get(f'https://emoji-api.com/emojis?access_key={EMOJI_API_KEY}')
        if response.status_code == 200:
            emojis = response.json()
            return random.choice(emojis)['character']
        else:
            return random.choice(['😀', '😂', '😅', '😎', '😍', '😡', '😢', '😱', '👍', '👎'])  # Fallback emojis
    except Exception as e:
        return random.choice(['😀', '😂', '😅', '😎', '😍', '😡', '😢', '😱', '👍', '👎'])  # Fallback emojis

# Function to fetch a random quote from the API Ninjas Quotes API
def fetch_random_quote():
    try:
        response = requests.get('https://api.api-ninjas.com/v1/quotes?limit=1', headers={'X-Api-Key': QUOTES_API_KEY})
        if response.status_code == 200:
            quote = response.json()[0]
            return f"{quote['quote']} — {quote['author']}"
        else:
            return "The best way to predict the future is to invent it. — Alan Kay"  # Fallback quote
    except Exception as e:
        return "The best way to predict the future is to invent it. — Alan Kay"  # Fallback quote

# Function to fetch a random fortune from the hardcoded fortunes
def fetch_random_fortune():
    return random.choice(FORTUNES)

# Function to fetch a random light color from an API
def fetch_random_light_color():
    try:
        while True:
            response = requests.get('https://www.thecolorapi.com/random')
            if response.status_code == 200:
                color = response.json()
                hex_value = color['hex']['clean']
                # Convert hex to RGB
                r = int(hex_value[0:2], 16)
                g = int(hex_value[2:4], 16)
                b = int(hex_value[4:6], 16)
                # Check if the color is light
                if (r*0.299 + g*0.587 + b*0.114) > 186:
                    return r, g, b
    except Exception as e:
        return 255, 255, 255  # Fallback light color (white)

def show_typing_indicator(duration=5):
    end_time = time.time() + duration
    while time.time() < end_time:
        message = random.choice(typing_messages)
        for char in '|/-\\':
            sys.stdout.write(f'\r{char} {message}')
            sys.stdout.flush()
            time.sleep(0.1)
    # Clear the line after the typing indicator is done
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

# Show the typing indicator once at the start
show_typing_indicator()
print("\nTyping indicator is done. You can continue with your work.\n")

# Continue with other terminal work
while True:
    try:
        command = input("Enter your command: ")
        if command.lower() == "exit":
            break
        else:
            os.system(command)
    except KeyboardInterrupt:
        break