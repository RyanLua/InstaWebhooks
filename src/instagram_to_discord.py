"""
Get new Instagram posts from any Instagram profile and send them to Discord using webhooks.

Make sure that you have everything in the requirements.txt file installed and that you are logged
into Instaloader.

Use the following to login:
    instaloader -l USERNAME

If the login fails, you may need to use use your session file to login.
For more details, see https://instaloader.github.io/troubleshooting.html#login-error.
"""

from time import sleep
from instaloader import Instaloader, Profile
import requests

L = Instaloader()

REFRESH_INTERVAL_SECONDS = 3600

# Terrible and repetitive code, but it works for now.
TARGET_INSTAGRAM_USER = input(
    "Enter the Instagram username you want to create a webhook for: ")

profile = Profile.from_username(
    L.context, TARGET_INSTAGRAM_USER)

print(f"""Creating webhook for {profile.full_name} (@{profile.username})

Posts: {profile.mediacount}
Followers: {profile.followers}
Following: {profile.followees}
""")

DISCORD_WEBHOOK_URL = input("Enter your Discord webhook URL: ")


def send_to_discord(post):
    """Send a new Instagram post to Discord using a webhook."""

    post_url = "https://instagram.com/p/" + post.shortcode + "/"
    image_url = post.url
    author_name = profile.username
    author_icon_url = profile.profile_pic_url
    post_description = post.caption
    post_timestamp = post.date
    author_fullname = profile.full_name

    icon_url = "https://www.instagram.com/static/images/ico/favicon-192.png/68d99ba29cc8.png"
    data = {
        "content": f"{post_url}",
        "embeds": [
            {
                "title": author_fullname,
                "description": post_description,
                "url": post_url,
                "color": 13500529,
                "timestamp": post_timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
                "author": {
                    "name": author_name,
                    "url": f"https://www.instagram.com/{author_name}/",
                    "icon_url": author_icon_url
                },
                "footer": {
                    "text": "Instagram",
                    "icon_url": icon_url
                },
                "image": {
                    "url": image_url
                }
            }
        ],
        "attachments": []
    }

    response = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
    print("Post sent to Discord:", response.status_code)


def check_for_new_posts():
    """Check for new Instagram posts and send them to Discord."""

    print("Checking for new posts...")

    posts = profile.get_posts()

    for post in posts:
        print(f"New post found: https://instagram.com/p/{post.shortcode}/")
        send_to_discord(post)
        break


while __name__ == "__main__":
    check_for_new_posts()
    sleep(REFRESH_INTERVAL_SECONDS)
