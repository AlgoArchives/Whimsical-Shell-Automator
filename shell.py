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
        # print(f"Error fetching emoji: {e}")
        return random.choice(['😀', '😂', '😅', '😎', '😍', '😡', '😢', '😱', '👍', '👎'])  # Fallback emojis

# Function to fetch a random quote from the API Ninjas Quotes API
def fetch_random_quote():
    try:
        response = requests.get('https://api.api-ninjas.com/v1/quotes?limit=1', headers={'X-Api-Key': QUOTES_API_KEY})
        if response.status_code == 200:
            quote = response.json()[0]
            return f"{quote['quote']} — {quote['author']}"
        else:
            # print(f"Error fetching quote: HTTP {response.status_code}")
            return "The best way to predict the future is to invent it. — Alan Kay"  # Fallback quote
    except Exception as e:
        # print(f"Error fetching quote: {e}")
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
        # print(f"Error fetching color: {e}")
        return 255, 255, 255  # Fallback light color (white)

def change_screen_color():
    while True:
        r, g, b = fetch_random_light_color()
        color_code = f'\033[38;2;{r};{g};{b}m'
        print(color_code, end='')
        time.sleep(5)  # Every 5 seconds

def print_random_message():
    while True:
        if random.choice([True, False]):
            print(f"\n{fetch_random_quote()}\n")
        else:
            print(f"\n{fetch_random_fortune()}\n")
        time.sleep(3600)  # Every hour

def show_typing_indicator():
    while True:
        message = random.choice(typing_messages)
        for char in '|/-\\':
            sys.stdout.write(f'\r{char} {message}')
            sys.stdout.flush()
            time.sleep(0.1)

def print_random_emoji():
    while True:
        emoji = fetch_random_emoji()
        print(f"\n Current Mood: {emoji} ?")
        time.sleep(300)  # Every 300 seconds (5 minutes)

# Run the functions in separate threads
threads = [
    threading.Thread(target=print_random_message),
    threading.Thread(target=change_screen_color),
    threading.Thread(target=show_typing_indicator),
    threading.Thread(target=print_random_emoji)
]

for thread in threads:
    thread.daemon = True
    thread.start()

# Keep the main thread alive
while True:
    time.sleep(1)