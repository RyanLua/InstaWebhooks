"""
Get new Instagram posts from any Instagram profile and send them to Discord using webhooks.
"""

import re
import logging
from argparse import ArgumentTypeError, ArgumentParser
from time import sleep
from instaloader import Instaloader, Profile
import requests
from requests.exceptions import HTTPError


def instagram_username(arg_value):
    """Instagram username type"""
    pattern = re.compile(r'^[a-zA-Z_](?!.*?\.{2})[\w.]{1,28}[\w]$')
    if not pattern.match(arg_value):
        raise ArgumentTypeError(
            f"invalid username value: '{arg_value}': must meet Instagram username requirements")
    return arg_value


def discord_webhook_url(arg_value):
    """Discord webhook URL type"""
    pattern = re.compile(
        r'^.*(discord|discordapp)\.com\/api\/webhooks\/([\d]+)\/([a-zA-Z0-9_.-]*)$')
    if not pattern.match(arg_value):
        raise ArgumentTypeError(
            f"invalid url value: '{arg_value}': must be a valid Discord webhook URL")
    return arg_value


# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)

# Parse command line arguments
parser = ArgumentParser(
    prog='InstaWebhooks',
    description='Monitor Instagram accounts for new posts and send them to a Discord webhook',
    epilog='Documentation: https://github.com/RaenLua/InstaWebhooks')
parser.add_argument("instagram_username",
                    help="the Instagram username to monitor for new posts",
                    type=instagram_username)
parser.add_argument(
    "discord_webhook_url", help="the Discord webhook URL to send new posts to",
    type=discord_webhook_url)
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-i", "--refresh-interval",
                    help="time in seconds to wait before checking for new posts again",
                    type=int, default=3600)
parser.add_argument("--version", action="version", version="%(prog)s 0.0.1")
args = parser.parse_args()

# Set the logger to debug if verbose is enabled
if args.verbose:
    logger.setLevel(logging.DEBUG)
    logger.debug("Verbose output enabled.")

logger.info("Starting InstaWebhooks for https://www.instagram.com/%s on %s",
            args.instagram_username, args.discord_webhook_url)

# Instaloader instance
L = Instaloader()
profile = Profile.from_username(L.context, args.instagram_username)


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

    payload = {
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

    try:
        logger.debug("Sending post sent to Discord")
        r = requests.post(args.discord_webhook_url, json=payload, timeout=10)
        r.raise_for_status()
    except HTTPError as http_error:
        logger.error("HTTP error occurred: %s", http_error)
    else:
        logger.info("Post sent successfully: %s", post_url)


def check_for_new_posts():
    """Check for new Instagram posts and send them to Discord."""

    logger.debug('Checking for new posts: https://www.instagram.com/%s',
                 args.instagram_username)

    posts = profile.get_posts()

    for post in posts:
        logger.info('New post found: https://instagram.com/p/%s',
                    post.shortcode)
        send_to_discord(post)
        break


if __name__ == "__main__":
    check_for_new_posts()
    sleep(args.refresh_interval)
