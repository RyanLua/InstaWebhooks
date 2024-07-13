"""
Placeholder
"""

import logging
import argparse

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO)

parser = argparse.ArgumentParser(
    prog='instawebhooks',
    description='Monitor Instagram accounts for new posts and send them to a Discord webhook',
    epilog='More documentation can be found at: https://github.com/RaenLua/InstaWebhooks')
parser.add_argument("instagram_username",
                    help="the Instagram username to monitor for new posts")
parser.add_argument(
    "discord_webhook_url", help="the Discord webhook URL to send new posts to")
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

if args.verbose:
    logger.setLevel(logging.DEBUG)
    logger.debug("Verbose output enabled.")

print(f"Creating webhook for {args.instagram_username}")

logger.info("Starting InstaWebhooks for %s", args.instagram_username)
