import time
import random
import os
import webbrowser
import sys
import threading

# Motivational Quotes
quotes = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "You miss 100% of the shots you don’t take.",
    "The journey of a thousand miles begins with one step."
]

# Emojis
emojis = ['😀', '😂', '😅', '😎', '😍', '😡', '😢', '😱', '👍', '👎']

# Fortune Cookies
fortunes = [
    "You will have a great day today!",
    "Something wonderful is about to happen.",
    "You will meet someone special soon.",
    "A new opportunity will come your way.",
    "Expect the unexpected."
]

def print_motivational_quote():
    while True:
        print(f"\nMotivational Quote: {random.choice(quotes)}\n")
        time.sleep(3600)  # Every hour

def change_screen_color():
    while True:
        color = random.choice(['0A', '0B', '0C', '0D', '0E', '0F'])
        os.system(f'color {color}')
        time.sleep(5)  # Every 5 seconds

def open_random_wikipedia_article():
    while True:
        webbrowser.open('https://en.wikipedia.org/wiki/Special:Random')
        time.sleep(60)  # Every minute

def show_typing_indicator():
    while True:
        for char in '|/-\\':
            sys.stdout.write(f'\r{char} Typing...')
            sys.stdout.flush()
            time.sleep(0.1)

def print_random_emoji():
    while True:
        print(f"\nRandom Emoji: {random.choice(emojis)}")
        time.sleep(3)  # Every 3 seconds

def show_fortune_cookie():
    print(f"\nFortune Cookie: {random.choice(fortunes)}\n")

# Run the functions in separate threads
threads = [
    threading.Thread(target=print_motivational_quote),
    threading.Thread(target=change_screen_color),
    threading.Thread(target=open_random_wikipedia_article),
    threading.Thread(target=show_typing_indicator),
    threading.Thread(target=print_random_emoji),
    threading.Thread(target=show_fortune_cookie)
]

for thread in threads:
    thread.daemon = True
    thread.start()

# Keep the main thread alive
while True:
    time.sleep(1)