"""
Get new Instagram posts from any Instagram profile and send them to Discord using webhooks.
"""

import logging
import re
from argparse import ArgumentParser
from datetime import datetime, timedelta
from itertools import dropwhile, takewhile
from time import sleep

try:
    import requests
    from instaloader import Instaloader, LoginRequiredException, Post, Profile
    from requests.exceptions import HTTPError
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Instaloader not found.\n  pip install [--user] instaloader"
    ) from exc


def regex(pattern: str):
    """Argument type for matching a regex pattern"""

    def closure_check_regex(arg_value):
        if not re.match(pattern, arg_value):
            raise ValueError(f"invalid value: '{arg_value}'")
        return arg_value

    return closure_check_regex


# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)

# Parse command line arguments
parser = ArgumentParser(
    prog="instawebhooks",
    description="Monitor Instagram accounts for new posts and send them to a Discord webhook",
    epilog="https://github.com/RaenLua/InstaWebhooks",
)
parser.add_argument(
    "instagram_username",
    help="the Instagram username to monitor for new posts",
    type=regex(r"^[a-zA-Z_](?!.*?\.{2})[\w.]{1,28}[\w]$"),
)
parser.add_argument(
    "discord_webhook_url",
    help="the Discord webhook URL to send new posts to",
    type=regex(
        r"^.*(discord|discordapp)\.com\/api\/webhooks\/([\d]+)\/([a-zA-Z0-9_.-]*)$"
    ),
)
parser.add_argument(
    "-v", "--verbose", help="increase output verbosity", action="store_true"
)
parser.add_argument(
    "-i",
    "--refresh-interval",
    help="time in seconds to wait before checking for new posts again",
    type=int,
    default=3600,
)
parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
args = parser.parse_args()

# Set the logger to debug if verbose is enabled
if args.verbose:
    logger.setLevel(logging.DEBUG)
    logger.debug("Verbose output enabled.")

# Log the start of the program
logger.info("Starting InstaWebhooks...")

# Check if we need to sign in to access the Instagram profile
try:
    Profile.from_username(Instaloader().context, args.instagram_username).get_posts()
except LoginRequiredException as exc:
    logger.critical("instaloader: error: %s", exc)
    raise SystemExit(
        "Not logged into Instaloader.\n  instaloader --login YOUR-USERNAME"
    ) from exc


def create_webhook_json(post: Post):
    """Create a Discord embed object from an Instagram post"""

    footer_icon_url = (
        "https://www.instagram.com/static/images/ico/favicon-192.png/68d99ba29cc8.png"
    )

    webhook_json = {
        "content": "",
        "embeds": [
            {
                "title": post.owner_profile.full_name,
                "description": post.caption,
                "url": "https://instagram.com/p/" + post.shortcode + "/",
                "color": 13500529,
                "timestamp": post.date.strftime("%Y-%m-%dT%H:%M:%S"),
                "author": {
                    "name": post.owner_username,
                    "url": "https://www.instagram.com/" + post.owner_username + "/",
                    "icon_url": post.owner_profile.profile_pic_url,
                },
                "footer": {"text": "Instagram", "icon_url": footer_icon_url},
                "image": {"url": post.url},
            }
        ],
        "attachments": [],
    }

    return webhook_json


def send_to_discord(post: Post):
    """Send a new Instagram post to Discord using a webhook"""

    payload = create_webhook_json(post)

    try:
        logger.debug("Sending post sent to Discord")
        r = requests.post(args.discord_webhook_url, json=payload, timeout=10)
        r.raise_for_status()
    except HTTPError as http_error:
        logger.error("HTTP error occurred: %s", http_error)
    else:
        logger.info("New post sent to Discord successfully.")


def check_for_new_posts():
    """Check for new Instagram posts and send them to Discord"""

    logger.debug("Checking for new posts")

    posts = Profile.from_username(
        Instaloader().context, args.instagram_username
    ).get_posts()

    since = datetime.now() - timedelta(seconds=args.refresh_interval)
    until = datetime.now()

    new_posts_found = False

    for post in takewhile(
        lambda p: p.date > until, dropwhile(lambda p: p.date > since, posts)
    ):
        new_posts_found = True
        logger.debug("New post found: https://instagram.com/p/%s", post.shortcode)
        send_to_discord(post)
        sleep(2)  # Avoid 30 requests per minute rate limit

    if not new_posts_found:
        logger.debug("No new posts found.")


def main():
    """Check for new Instagram posts and send them to Discord"""
    logger.info("InstaWebhooks started successfully.")
    logger.info(
        "Monitoring '%s' every %s seconds on ̀%s.",
        args.instagram_username,
        args.refresh_interval,
        args.discord_webhook_url,
    )

    while True:
        check_for_new_posts()
        sleep(args.refresh_interval)


if __name__ == "__main__":
    main()
