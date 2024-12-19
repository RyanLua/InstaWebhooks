Usage
=====

To see the available options and arguments, run the following command:

.. code:: console

    $ instawebhooks --help
    usage: instawebhooks [-h] [-q | -v] [-i REFRESH_INTERVAL] [-c MESSAGE_CONTENT] [-e] [--version]
                         instagram_username discord_webhook_url

    Monitor Instagram accounts for new posts and send them to a Discord webhook

    positional arguments:
      instagram_username    the Instagram username to monitor for new posts
      discord_webhook_url   the Discord webhook URL to send new posts to

    options:
      -h, --help            show this help message and exit
      -q, --quiet           hide all logging
      -v, --verbose         show debug logging
      -i REFRESH_INTERVAL, --refresh-interval REFRESH_INTERVAL
                            time in seconds to wait before checking for new posts again
      -c MESSAGE_CONTENT, --message-content MESSAGE_CONTENT
                            the message content to send with the webhook
      -e, --no-embed        don't show the post embed and only send message content
      --version             show program's version number and exit

    https://github.com/RaenLua/InstaWebhooks

Below, learn how to use InstaWebhooks and what you can do with it.

Examples
--------

In the below templates, replace ``<INSTAGRAM_USERNAME>`` with the Instagram username you want to monitor and ``<DISCORD_WEBHOOK_URL>`` with the Discord webhook URL you want to send new posts to.

Your command should look similar to this:

.. code:: console

    $ instawebhooks raenlua https://discord.com/api/webhooks/0123456789/abcdefghijklmnopqrstuvwxyz

Templates
---------

Example templates for using InstaWebhooks are provided below. Note to change the Instagram username and Discord webhook URL to your own.

.. note::

    The default refresh interval is 1 hour (3600 seconds), and the default message content is an empty string.

Send new posts every hour:

.. code:: console

    $ instawebhooks <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

Send new posts every hour with verbose logging:

.. code:: console

    $ instawebhooks -v <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

Send new posts every 30 minutes:

.. code:: console

    $ instawebhooks -i 1800 <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

Send new posts every hour with a custom message:

.. code:: console

    $ instawebhooks -c "New post from {owner_name}: {post_url}" <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

Send new posts every hour with no embed and a custom message:

.. code:: console

    $ instawebhooks -e -c "New post from {owner_name}: {post_url}" <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

Reference
---------

Positional Arguments
~~~~~~~~~~~~~~~~~~~~

``INSTAGRAM_USERNAME``

    The Instagram username to monitor for new posts.

    Usernames must follow the Instagram username format:

    * Starts with a letter or underscore.
    * Does not contain consecutive periods.
    * Is between 2 and 30 characters long.
    * Ends with an alphanumeric character or underscore.

``DISCORD_WEBHOOK_URL``

    The Discord webhook URL to send new posts to.

    URLs must follow the Discord webhook URL format:

    * ``https://discord.com/api/webhooks/{webhook_id}/{webhook_token}``
    * ``https://discordapp.com/api/webhooks/{webhook_id}/{webhook_token}``

Optional Arguments
~~~~~~~~~~~~~~~~~~

``-h, --help``

    Show this help message and exit.

``-v, --verbose``

    Enable verbose logging.

    Changes the logging level to debug, showing the following logs in addition to the default info logs:

    * When a check for new posts is started.
    * If a new post is found or not.
    * When a post is sent to Discord.

``-i REFRESH_INTERVAL, --refresh-interval REFRESH_INTERVAL``

    .. caution::

        Do not set the refresh interval too low or you may be `rate limited by Instagram <https://instaloader.github.io/troubleshooting.html#too-many-requests>`_.

    The refresh interval to check for new posts in seconds (default: 3600).

``-c MESSAGE_CONTENT, --message-content MESSAGE_CONTENT``

    The message content to send to Discord (default: "").

    Accepts placeholders for the post information:

    * ``{post_url}`` - The URL to the post on Instagram
        * ``https://www.instagram.com/C8wRGmyR-6N``
    * ``{owner_url}`` - The URL to the owner's profile on Instagram
        * ``https://www.instagram.com/raenlua``
    * ``{owner_name}`` - The owner's full name
        * ``Ryan Luu``
    * ``{owner_username}`` - The owner's username
        * ``raenlua``
    * ``{post_caption}`` - The post's caption
        * ``This is a post caption.``
    * ``{post_shortcode}`` - The post's shortcode
        * ``C8wRGmyR-6N``
    * ``{post_image_url}`` - The post's image URL
        * ``https://www.instagram.com/p/C8wRGmyR-6N/media``

``-e, --no-embed``

    Don't show the post embed and only send message content

    A message content must be provided when using this option. Empty messages cannot be sent.