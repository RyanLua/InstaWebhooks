"""
Placeholder
"""

import re
import logging
import argparse


def instagram_username(arg_value):
    """Instagram username type"""
    pattern = re.compile(r'^[a-zA-Z_](?!.*?\.{2})[\w.]{1,28}[\w]$')
    if not pattern.match(arg_value):
        raise argparse.ArgumentTypeError(
            f"invalid value: '{arg_value}': must meet Instagram username requirements")
    return arg_value


def discord_webhook_url(arg_value):
    """Discord webhook URL type"""
    pattern = re.compile(
        r'^.*(discord|discordapp)\.com\/api\/webhooks\/([\d]+)\/([a-zA-Z0-9_.-]*)$')
    if not pattern.match(arg_value):
        raise argparse.ArgumentTypeError(
            f"invalid value: '{arg_value}': must be a valid Discord webhook URL")
    return arg_value


# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)

# Parse command line arguments
parser = argparse.ArgumentParser(
    prog='instawebhooks',
    description='Monitor Instagram accounts for new posts and send them to a Discord webhook',
    epilog='More documentation can be found at: https://github.com/RaenLua/InstaWebhooks')
parser.add_argument("instagram_username",
                    help="the Instagram username to monitor for new posts",
                    type=instagram_username)
parser.add_argument(
    "discord_webhook_url", help="the Discord webhook URL to send new posts to",
    type=discord_webhook_url)
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

# Set the logger to debug if verbose is enabled
if args.verbose:
    logger.setLevel(logging.DEBUG)
    logger.debug("Verbose output enabled.")

logger.info("Starting InstaWebhooks for %s on %s",
            args.instagram_username, args.discord_webhook_url)
