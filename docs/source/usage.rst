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

.. argparse::
   :module: src.instawebhooks.parser
   :func: parser
   :prog: instawebhooks
   :noepilog:

   instagram_username : @after
        Usernames must follow the Instagram username format:

        * Starts with a letter or underscore.
        * Does not contain consecutive periods.
        * Is between 2 and 30 characters long.
        * Ends with an alphanumeric character or underscore.

   discord_webhook_url : @after
        URLs must follow the Discord webhook URL format:

        * ``https://discord.com/api/webhooks/{webhook_id}/{webhook_token}``
        * ``https://discordapp.com/api/webhooks/{webhook_id}/{webhook_token}``
