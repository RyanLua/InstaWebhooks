import instaloader
import requests
import time

INSTAGRAM_PROFILE = input("Enter the Instagram account you want monitor: ")
INSTAGRAM_USERNAME = input("Enter your Instagram username to login: ")
WEBHOOK_URL = input("Enter the Discord webhook URL: ")

# Get instance
L = instaloader.Instaloader()
L.load_session_from_file(INSTAGRAM_PROFILE, "./session-*")

def send_to_discord(post_url):
    """Send the Instagram post URL to Discord."""
    data = {"content": f"New post from {INSTAGRAM_PROFILE}: {post_url}"}
    response = requests.post(WEBHOOK_URL, json=data)
    print("Notification sent to Discord:", response.status_code)

def check_for_new_posts():
    """Check for new posts and notify on Discord."""
    profile = instaloader.Profile.from_username(L.context, INSTAGRAM_PROFILE)
    for post in profile.get_posts():
        # Assuming you're running this script regularly, check the latest post
        send_to_discord("https://instagram.com/p/" + post.shortcode)
        break  # Only check the most recent post

# Every 10 minutes
while True:
    check_for_new_posts()
    time.sleep(600)  # Sleep for 600 seconds (10 minutes)