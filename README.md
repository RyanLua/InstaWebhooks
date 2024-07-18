<div align="center">
	<img alt="InstaWebhooks" src="assets/Logo.svg" width="128px" />
	<h1>InstaWebhooks</h1>
</div>

<div align="center">

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/RyanLua/InstaWebhooks?quickstart=1)

</div>

Monitor Instagram accounts for new posts and send them to a Discord webhook.

* Works with **any Instagram account**, including private accounts if you are a follower
* Customizable **Discord embeds** for new posts and message contents including **mentions/pings**
* **User-definable refresh interval** for checking for new posts the second they are posted

<img alt="Example of a new post notification" src="assets/ScreenshotEmbedExample.png" height="512px" />

## Installation

Before installing, make sure you have [Python 3.8 or newer](https://www.python.org/downloads/) installed.

1. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) onto your machine
```
git clone https://github.com/RyanLua/InstaWebhooks.git
```
2. Install the required Python packages by running the following command in the repository directory (we only have one package to install for now):
```
pip install instaloader
```

Now you are ready to use the script! See the [Usage](#usage) section for more information on usage.

## Usage

Usage is simple once you have everything installed, just run the script with the Instagram username you want to monitor and the Discord webhook URL you want to send new posts to.

An example of monitoring the Instagram account `raenlua` and sending new posts to a Discord webhook URL:
```
python instawebhooks.py raenlua https://discord.com/api/webhooks/1256506980734992447/GnM79-OWCDQ935_hPp6zY0DCHopS8uBWTgjgEI9OTrXZFqayDcfiMYo_CvhYPWvDTB3h
```

You can also use the optional arguments to customize the behavior of the script. For example, to check for new posts every 1800 seconds (30 minutes):
```
python instawebhooks.py raenlua https://discord.com/api/webhooks/1256506980734992447/GnM79-OWCDQ935_hPp6zY0DCHopS8uBWTgjgEI9OTrXZFqayDcfiMYo_CvhYPWvDTB3h -i 1800
```

For more on different arguments you can use, see [Documentation](#documentation).

## Documentation

The different arguments you can use are very simple. Below are all the arguments you can use and what they do.

### Arguments
* `instagram_username`: The Instagram username to monitor for new posts.
* `discord_webhook_url`: The Discord webhook URL to send new posts to.

### Options
* `-v`, `--verbose`: Increase output verbosity.
* `-i`, `--refresh-interval`: Time in seconds to wait before checking for new posts again (default is 3600 seconds).
* `--version`: Show the program's version number and exit.
