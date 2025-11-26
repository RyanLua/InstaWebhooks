Usage
=====

To see the available options and arguments, run the following command:

.. code:: console

    $ instawebhooks --help

Examples
--------

* Send new posts:

.. code:: console

    $ instawebhooks <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

* Send new posts with verbose logging:

.. code:: console

    $ instawebhooks -v <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

* Send new posts every 30 minutes:

.. code:: console

    $ instawebhooks -i 1800 <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

* Send new posts with a custom message:

.. code:: console

    $ instawebhooks -c "New post from {owner_name}: {post_url}" <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

* Send new posts with no embed and a custom message:

.. code:: console

    $ instawebhooks -e -c "New post from {owner_name}: {post_url}" <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

* Send new posts for multiple Instagram usernames and Discord webhook URLs:

.. code:: console

    $ instawebhooks <INSTAGRAM_USERNAME_1> <INSTAGRAM_USERNAME_2> ... <DISCORD_WEBHOOK_URL_1> <DISCORD_WEBHOOK_URL_2> ...

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

   -c --message-content : @after
        Accepts placeholders for the post information:

        * ``{post_url}`` - The URL to the post on Instagram: ``https://www.instagram.com/C8wRGmyR-6N``
        * ``{owner_url}`` - The URL to the owner's profile on Instagram: ``https://www.instagram.com/raenlua``
        * ``{owner_name}`` - The owner's full name: ``Ryan Luu``
        * ``{owner_username}`` - The owner's username: ``raenlua``
        * ``{post_caption}`` - The post's caption: ``This is a post caption.``
        * ``{post_shortcode}`` - The post's shortcode: ``C8wRGmyR-6N``
        * ``{post_image_url}`` - The post's image URL: ``https://www.instagram.com/p/C8wRGmyR-6N/media``
