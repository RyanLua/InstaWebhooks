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
import requests
import instaloader

TARGET_INSTAGRAM_PROFILE = input("Enter the Instagram account you want monitor: ")
DISCORD_WEBHOOK_URL = input("Enter the Discord webhook URL: ")
POST_REFRESH_INTERVAL = 600  # How often to check for new posts (in seconds)

L = instaloader.Instaloader()

def send_to_discord(post_url, image_url, author_name, author_icon_url, post_description):
    """Send a new Instagram post to Discord using a webhook."""
    data = {
        "content": f"{post_url}",
        "embeds": [
            {
                "description": post_description,
                "color": 13500529,
                "author": {
                    "name": author_name,
                    "url": f"https://www.instagram.com/{author_name}/",
                    "icon_url": author_icon_url
                },
                "footer": {
                    "text": "Instagram",
                    "icon_url": "https://images-ext-1.discordapp.net/external/C6jCIKlXguRhfmSp6USkbWsS11fnsbBgMXiclR2R4ps/https/www.instagram.com/static/images/ico/favicon-192.png/68d99ba29cc8.png"
                },
                "image": {
                    "url": image_url
                }
            }
        ],
        "attachments": []
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=10)
    print("Notification sent to Discord:", response.status_code)

def check_for_new_posts():
    """Check for new Instagram posts and send them to Discord."""
    profile = instaloader.Profile.from_username(L.context, TARGET_INSTAGRAM_PROFILE)
    for post in profile.get_posts():
        instagram_post_url = "https://instagram.com/p/" + post.shortcode
        image_url = post.url
        author_name = profile.username
        author_icon_url = profile.profile_pic_url
        post_description = post.caption

        send_to_discord(
            instagram_post_url,
            image_url,
            author_name,
            author_icon_url,
            post_description
        )
        break

# Every 10 minutes
while __name__ == "__main__":
    check_for_new_posts()
    time.sleep(POST_REFRESH_INTERVAL)  # Sleep for 600 seconds (10 minutes)
