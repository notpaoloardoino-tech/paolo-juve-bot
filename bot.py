import tweepy
from datetime import datetime
import os

# Chiavi API (usa secrets GitHub)
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

start_date = datetime(2025, 10, 20)

current_date = datetime.now()
day_count = (current_date - start_date).days + 1
message = f"Day {day_count} asking @paolo_ardoino buying @Juventusfc"

try:
    api.update_status(message)
    print(f"Postato: {message} alle {current_date}")
except tweepy.TweepyException as e:
    print(f"Errore: {e}")
