import time
import random
import os
import sys
import threading
import requests

# Motivational Quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "You miss 100% of the shots you don’t take.",
    "The journey of a thousand miles begins with one step."
]

# Fortune Cookies
fortunes = [
    "You will have a great day today!",
    "Something wonderful is about to happen.",
    "You will meet someone special soon.",
    "A new opportunity will come your way.",
    "Expect the unexpected."
]

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
        response = requests.get('https://emoji-api.com/emojis?access_key=your_access_key')
        if response.status_code == 200:
            emojis = response.json()
            return random.choice(emojis)['character']
        else:
            return random.choice(['😀', '😂', '😅', '😎', '😍', '😡', '😢', '😱', '👍', '👎'])  # Fallback emojis
    except Exception as e:
        print(f"Error fetching emoji: {e}")
        return random.choice(['😀', '😂', '😅', '😎', '😍', '😡', '😢', '😱', '👍', '👎'])  # Fallback emojis

def print_random_message():
    while True:
        if random.choice([True, False]):
            print(f"\n{random.choice(quotes)}\n")
        else:
            print(f"\n{random.choice(fortunes)}\n")
        time.sleep(3600)  # Every hour

def change_screen_color():
    while True:
        color = random.choice(['0A', '0B', '0C', '0D', '0E', '0F'])
        os.system(f'color {color}')
        time.sleep(5)  # Every 5 seconds

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