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

```console
$ python instawebhooks.py <instagram_username> <discord_webhook_url>
```

<img alt="Example of a new post notification" src="assets/ScreenshotEmbedExample.png" width="512px" />

## Installation

Before installing, make sure you have [Python 3.8 or newer](https://www.python.org/downloads/) installed.

## Usage

Usage is simple once you have everything installed, just run the script with the Instagram username you want to monitor and the Discord webhook URL you want to send new posts to.

### Example
```console
$ python instawebhooks.py raenlua https://discord.com/api/webhooks/1256506980734992447/GnM79-OWCDQ935_hPp6zY0DCHopS8uBWTgjgEI9OTrXZFqayDcfiMYo_CvhYPWvDTB3h
```

## Documentation

### Arguments
* `instagram_username`: The Instagram username to monitor for new posts.
* `discord_webhook_url`: The Discord webhook URL to send new posts to.

### Options
* `-v`, `--verbose`: Increase output verbosity.
* `-i`, `--refresh-interval`: Time in seconds to wait before checking for new posts again (default is 3600 seconds).
* `--version`: Show the program's version number and exit.
