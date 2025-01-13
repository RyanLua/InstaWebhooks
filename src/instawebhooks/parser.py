"""Command line argument parser for InstaWebhooks"""

import importlib.metadata
import re
from argparse import ArgumentParser


def regex(pattern: str):
    """Argument type for matching a regex pattern"""

    def closure_check_regex(arg_value: str):
        if not re.match(pattern, arg_value):
            raise ValueError(f"invalid value: '{arg_value}'")
        return arg_value

    return closure_check_regex


try:
    VERSION = importlib.metadata.version("instawebhooks")
except importlib.metadata.PackageNotFoundError:
    VERSION = "unknown"

# Parse command line arguments
parser = ArgumentParser(
    prog="instawebhooks",
    description=(
        "Monitor Instagram accounts for new posts and send them to a Discord webhook"
    ),
    epilog="https://github.com/RaenLua/InstaWebhooks",
)
logging_group = parser.add_mutually_exclusive_group()
login_group = parser.add_mutually_exclusive_group()
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
logging_group.add_argument(
    "-q", "--quiet", help="hide all logging", action="store_true"
)
logging_group.add_argument(
    "-v", "--verbose", help="show debug logging", action="store_true"
)
login_group.add_argument(
    "-l",
    "--login",
    metavar=("USERNAME", "PASSWORD"),
    type=str,
    help="login to instagram with username and password",
    nargs=2,
)
login_group.add_argument(
    "-t",
    "--interactive-login",
    metavar="USERNAME",
    type=str,
    help="login to instagram with username and ask for password on terminal",
)
parser.add_argument(
    "-p",
    "--catchup",
    help="send the last latest posts on startup regardless of time",
    metavar="POSTS",
    type=int,
    default=0,
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
parser.add_argument("--version", action="version", version="%(prog)s " + VERSION)
