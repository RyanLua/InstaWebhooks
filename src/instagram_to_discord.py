"""
Get new Instagram posts from any Instagram profile and send them to Discord using webhooks.

Make sure that you have everything in the requirements.txt file installed and that you are logged
into Instaloader.

Use the following to login:
    instaloader -l USERNAME

If the login fails, you may need to use use your session file to login.
For more details, see https://instaloader.github.io/troubleshooting.html#login-error.
"""

import time
from itertools import dropwhile, takewhile
from datetime import datetime
import requests
import instaloader

L = instaloader.Instaloader()

POST_REFRESH_INTERVAL = 3600  # Seconds

# Terrible and repetitive code, but it works for now.
TARGET_INSTAGRAM_PROFILE = input(
    "Enter the Instagram account you want to create a webhook for: ")

profile = instaloader.Profile.from_username(
    L.context, TARGET_INSTAGRAM_PROFILE)

print(f"\nProfile information\n\nName: {profile.full_name}\nUsername: {profile.username}\nPosts: {
      profile.mediacount}\nFollowers: {profile.followers}\nFollowing: {profile.followees}\n")

DISCORD_WEBHOOK_URL = input("Enter the Discord webhook URL: ")
REFRESH_INTERVAL = 3600


def send_to_discord(post_details):
    """Send a new Instagram post to Discord using a webhook."""
    icon_url = "https://www.instagram.com/static/images/ico/favicon-192.png/68d99ba29cc8.png"
    data = {
        "content": f"{post_details.post_url}",
        "embeds": [
            {
                "title": post_details.author_fullname,
                "description": post_details.post_description,
                "url": post_details.post_url,
                "color": 13500529,
                "timestamp": post_details.post_timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
                "author": {
                    "name": post_details.author_name,
                    "url": f"https://www.instagram.com/{post_details.author_name}/",
                    "icon_url": post_details.author_icon_url
                },
                "footer": {
                    "text": "Instagram",
                    "icon_url": icon_url
                },
                "image": {
                    "url": post_details.image_url
                }
            }
        ],
        "attachments": []
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
    print("Notification sent to Discord:", response.status_code)


def check_for_new_posts():
    """Check for new Instagram posts and send them to Discord."""
    profile = instaloader.Profile.from_username(
        L.context, TARGET_INSTAGRAM_PROFILE)
    posts = profile.get_posts()

    until = datetime.now()
    since = until.replace(second=until.second-POST_REFRESH_INTERVAL)

    for post in takewhile(lambda p: p.date > until, dropwhile(lambda p: p.date > since, posts)):
        post_details = {
            "post_url": "https://instagram.com/p/" + post.shortcode + "/",
            "image_url": post.url,
            "author_name": profile.username,
            "author_icon_url": profile.profile_pic_url,
            "post_description": post.caption,
            "post_timestamp": post.date,
            "author_fullname": profile.full_name
        }

        send_to_discord(post_details)
        break


while __name__ == "__main__":
    check_for_new_posts()
    time.sleep(POST_REFRESH_INTERVAL)
