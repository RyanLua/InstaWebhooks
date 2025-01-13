"""Module for sending new Instagram posts to Discord."""

import asyncio
import io
import logging
import re
import sys
from datetime import datetime, timedelta
from itertools import dropwhile, takewhile
from time import sleep
from typing import Dict, List

from .parser import parser

try:
    from aiohttp import ClientSession
    from discord import Embed, File, SyncWebhook
    from instaloader.exceptions import LoginException, LoginRequiredException
    from instaloader.instaloader import Instaloader
    from instaloader.structures import Post, Profile
except ModuleNotFoundError as exc:
    raise SystemExit(
        f"{exc.name} not found.\n  pip install [--user] {exc.name}"
    ) from exc


# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)


args = parser.parse_args()

# Set the logger to debug if verbose is enabled
if args.quiet:
    logger.setLevel(logging.CRITICAL)
    logger.debug("Quiet output enabled.")
elif args.verbose:
    logger.setLevel(logging.DEBUG)
    logger.debug("Verbose output enabled.")
else:
    logger.setLevel(logging.INFO)

if args.login or args.interactive_login:
    logger.info("Logging into Instagram...")
    try:
        if args.login:
            Instaloader().login(*args.login)
        if args.interactive_login:
            Instaloader().interactive_login(args.interactive_login)
    except LoginException as login_exc:
        logger.critical("instaloader: error: %s", login_exc)
        raise SystemExit(
            "An error happened during login. Check if the provided username exists."
        ) from login_exc
    except KeyboardInterrupt:
        print("\nLogin interrupted by user.")
        sys.exit(0)

# Log the start of the program
logger.info("Starting InstaWebhooks...")

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

    # Format the post caption with clickable links for mentions and hashtags
    post_caption = post.caption or ""
    post_caption = re.sub(
        r"#([a-zA-Z0-9]+\b)",
        r"[#\1](https://www.instagram.com/explore/tags/\1)",
        post_caption,
    )
    post_caption = re.sub(
        r"@([a-zA-Z0-9_]+\b)",
        r"[@\1](https://www.instagram.com/\1)",
        post_caption,
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
    placeholders: Dict[str, str] = {
        "{post_url}": f"https://www.instagram.com/p/{post.shortcode}/",
        "{owner_url}": f"https://www.instagram.com/{post.owner_username}/",
        "{owner_name}": post.owner_profile.full_name,
        "{owner_username}": post.owner_username,
        "{post_caption}": post.caption or "",
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

    logger.debug("Sending post sent to Discord...")

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


async def check_for_new_posts(catchup: int = args.catchup):
    """Check for new Instagram posts and send them to Discord"""

    logger.info("Checking for new posts")

    posts = Profile.from_username(
        Instaloader().context, args.instagram_username
    ).get_posts()

    since = datetime.now()
    until = datetime.now() - timedelta(seconds=args.refresh_interval)

    new_posts_found = False

    async def send_post(post: Post):
        logger.info("New post found: https://www.instagram.com/p/%s", post.shortcode)
        await send_to_discord(post)

    if catchup > 0:
        logger.info("Sending last %s posts on startup...", catchup)
        posts_to_send: List[Post] = []
        for post in takewhile(lambda _: catchup > 0, posts):
            posts_to_send.append(post)
            catchup -= 1

        # Reverse the posts to send oldest first
        for post in reversed(posts_to_send):
            await send_post(post)
            sleep(2)  # Avoid 30 requests per minute rate limit

    for post in takewhile(
        lambda p: p.date > until, dropwhile(lambda p: p.date > since, posts)
    ):
        new_posts_found = True
        await send_post(post)
        sleep(2)  # Avoid 30 requests per minute rate limit

    if not new_posts_found:
        logger.info("No new posts found.")


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
    except LoginRequiredException as login_exc:
        logger.critical("instaloader: error: %s", login_exc)
        raise SystemExit(
            "Not logged in. Please login with the --login flag."
        ) from login_exc
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(0)
