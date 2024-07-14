"""
Get new Instagram posts from any Instagram profile and send them to Discord using webhooks.
"""

import logging
import re
from argparse import ArgumentParser, ArgumentTypeError
from datetime import datetime, timedelta
from itertools import dropwhile, takewhile
from time import sleep

import requests
from instaloader import Instaloader, Post, Profile
from requests.exceptions import HTTPError


def instagram_username(arg_value: str):
    """Instagram username"""
    pattern = re.compile(r'^[a-zA-Z_](?!.*?\.{2})[\w.]{1,28}[\w]$')
    if not pattern.match(arg_value):
        raise ArgumentTypeError(
            f"invalid username value: '{arg_value}': must meet Instagram username requirements")
    return arg_value


def discord_webhook_url(arg_value: str):
    """Discord webhook URL"""
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

# Log the start of the program
logger.info("Starting InstaWebhooks for https://www.instagram.com/%s on %s",
            args.instagram_username, args.discord_webhook_url)


def create_embed_json(post: Post):
    """Create a Discord embed object from an Instagram post"""

    footer_icon_url = "https://www.instagram.com/static/images/ico/favicon-192.png/68d99ba29cc8.png"

    embed = {
        "title": post.owner_username,
        "description": post.caption,
        "url": "https://instagram.com/p/" + post.shortcode + "/",
        "color": 13500529,
        "timestamp": post.date.strftime("%Y-%m-%dT%H:%M:%S"),
        "author": {
            "name": post.owner_profile.full_name,
            "url": "https://www.instagram.com/" + post.owner_username + "/",
            "icon_url": post.owner_profile.profile_pic_url
        },
        "footer": {
            "text": "Instagram",
            "icon_url": footer_icon_url
        },
        "image": {
            "url": post.url
        }
    }

    return embed


def send_to_discord(post: Post):
    """Send a new Instagram post to Discord using a webhook"""

    payload = create_embed_json(post)

    try:
        logger.debug("Sending post sent to Discord")
        r = requests.post(args.discord_webhook_url, json=payload, timeout=10)
        r.raise_for_status()
    except HTTPError as http_error:
        logger.error("HTTP error occurred: %s", http_error)
    else:
        logger.info("Post sent successfully: %s", post_url)


def check_for_new_posts():
    """Check for new Instagram posts and send them to Discord"""

    logger.debug('Checking for new posts: https://www.instagram.com/%s',
                 args.instagram_username)

    posts = Profile.from_username(
        Instaloader().context, args.instagram_username).get_posts()

    since = datetime.now() - timedelta(seconds=args.refresh_interval)
    until = datetime.now()

    for post in takewhile(lambda p: p.date > until, dropwhile(lambda p: p.date > since, posts)):
        logger.info('New post found: https://instagram.com/p/%s',
                    post.shortcode)
        send_to_discord(post)


if __name__ == "__main__":
    check_for_new_posts()
    sleep(args.refresh_interval)
