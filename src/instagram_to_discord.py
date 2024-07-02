"""
Get new Instagram posts from any Instagram profile and send them to Discord using webhooks.

Make sure that you have everything in the requirements.txt file installed and that you are logged into Instaloader.

Use the following to login:
    instaloader -l USERNAME

If the login fails, you may need to use import_firefox_session.py to get your session file and login using that.
"""

import time
import requests
import instaloader

TARGET_INSTAGRAM_PROFILE = input("Enter the Instagram account you want monitor: ")
DISCORD_WEBHOOK_URL = input("Enter the Discord webhook URL: ")
POST_REFRESH_INTERVAL = 600  # How often to check for new posts (in seconds)

# Get instance
L = instaloader.Instaloader()

def send_to_discord(post_url):
    """Send the Instagram post URL to Discord."""
    data = {"content": f"New post from {TARGET_INSTAGRAM_PROFILE}: {post_url}"}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
    print("Notification sent to Discord:", response.status_code)

def check_for_new_posts():
    """Check for new posts and notify on Discord."""
    profile = instaloader.Profile.from_username(L.context, TARGET_INSTAGRAM_PROFILE)
    for post in profile.get_posts():
        # Assuming you're running this script regularly, check the latest post
        send_to_discord("https://instagram.com/p/" + post.shortcode)
        break  # Only check the most recent post

# Every 10 minutes
while __name__ == "__main__":
    check_for_new_posts()
    time.sleep(POST_REFRESH_INTERVAL)  # Sleep for 600 seconds (10 minutes)
