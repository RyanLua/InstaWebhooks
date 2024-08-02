"""Module for sending new Instagram posts to Discord."""

import asyncio
import io
import logging
import re
import sys
from argparse import ArgumentParser
from datetime import datetime, timedelta
from itertools import dropwhile, takewhile
from time import sleep

try:
    from aiohttp import ClientSession
except ModuleNotFoundError as exc:
    raise SystemExit("Aiohttp not found.\n  pip install [--user] aiohttp") from exc

try:
    from discord import Embed, File, SyncWebhook
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Discord.py not found.\n  pip install [--user] discord.py"
    ) from exc

try:
    from instaloader import Instaloader, LoginRequiredException, Post, Profile
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
parser.add_argument(
    "-c",
    "--message-content",
    help="the message content to send with the webhook",
    type=str,
    default="",
)
parser.add_argument(
    "-e",
    "--no-embed",
    help="don't show the post embed and only send message content",
    action="store_true",
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
except KeyboardInterrupt:
    print("\nInterrupted by user.")
    sys.exit(0)
except LoginRequiredException as exc:
    logger.critical("instaloader: error: %s", exc)
    raise SystemExit(
        "Not logged into Instaloader.\n  instaloader --login YOUR-USERNAME"
    ) from exc

# Ensure that a message content is provided if no embed is enabled
if args.no_embed and args.message_content == "":
    logger.critical("error: Cannot send an empty message. No message content provided.")
    raise SystemExit(
        "Please provide a message content with the --message-content flag."
    )


async def create_embed(post: Post):
    """Create a Discord embed object from an Instagram post"""

    logger.debug("Creating post embed...")

    footer_icon_url = (
        "https://www.instagram.com/static/images/ico/favicon-192.png/68d99ba29cc8.png"
    )

    # Download the post image and profile picture
    async with ClientSession() as cs:
        async with cs.get(post.url) as res:
            post_image_bytes = await res.read()

        async with cs.get(post.owner_profile.profile_pic_url) as res:
            profile_pic_bytes = await res.read()

    post_image_file = File(io.BytesIO(post_image_bytes), "post_image.webp")
    profile_pic_file = File(io.BytesIO(profile_pic_bytes), "profile_pic.webp")

    # Replace hashtags with clickable links
    if post.caption is None:
        post_caption = ""
    else:
        post_caption = re.sub(
            r"#([a-zA-Z0-9]+\b)",
            r"[#\1](https://www.instagram.com/explore/tags/\1)",
            post.caption,
        )

    embed = Embed(
        color=13500529,
        title=post.owner_profile.full_name,
        description=post_caption,
        url=f"https://www.instagram.com/p/{post.shortcode}/",
        timestamp=post.date,
    )
    embed.set_author(
        name=post.owner_username,
        url=f"https://www.instagram.com/{post.owner_username}/",
        icon_url="attachment://profile_pic.webp",
    )
    embed.set_footer(text="Instagram", icon_url=footer_icon_url)
    embed.set_image(url="attachment://post_image.webp")

    return embed, post_image_file, profile_pic_file


def format_message(post: Post):
    """Format the message content with placeholders"""

    logger.debug("Formatting message for placeholders...")

    placeholders = {
        "{post_url}": f"https://www.instagram.com/p/{post.shortcode}/",
        "{owner_url}": f"https://www.instagram.com/{post.owner_username}/",
        "{owner_name}": post.owner_profile.full_name,
        "{owner_username}": post.owner_username,
        "{post_caption}": post.caption,
        "{post_shortcode}": post.shortcode,
        "{post_image_url}": post.url,
    }

    # Replace placeholders in the message content
    for placeholder, value in placeholders.items():
        args.message_content = args.message_content.replace(placeholder, value)


async def send_to_discord(post: Post):
    """Send a new Instagram post to Discord using a webhook"""

    webhook = SyncWebhook.from_url(args.discord_webhook_url)

    if args.message_content:
        format_message(post)

    logger.debug("Sending post sent to Discord")

    if not args.no_embed:
        embed, post_image_file, profile_pic_file = await create_embed(post)
        webhook.send(
            content=args.message_content,
            embed=embed,
            files=[post_image_file, profile_pic_file],
        )
    else:
        webhook.send(content=args.message_content)

    logger.info("New post sent to Discord successfully.")


async def check_for_new_posts():
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
        logger.debug("New post found: https://www.instagram.com/p/%s", post.shortcode)
        await send_to_discord(post)
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

    try:
        while True:
            asyncio.run(check_for_new_posts())
            sleep(args.refresh_interval)
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(0)
