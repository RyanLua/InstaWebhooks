.. image:: https://raw.githubusercontent.com/RyanLua/InstaWebhooks/main/assets/Logo.png
   :alt: InstaWebhooks
   :width: 64px

InstaWebhooks - Discord webhooks for Instagram
==============================================

.. |ci-badge| image:: https://github.com/RyanLua/InstaWebhooks/actions/workflows/ci.yml/badge.svg
   :target: https://github.com/RyanLua/InstaWebhooks/actions/workflows/ci.yml
   :alt: Continuous Integration

.. |pypi-version| image:: https://img.shields.io/pypi/v/instawebhooks
   :target: https://pypi.org/project/instawebhooks/
   :alt: PyPI

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/instawebhooks
   :target: https://pypi.org/project/instawebhooks
   :alt: PyPI - Python Version

.. |license-badge| image:: https://img.shields.io/pypi/l/instawebhooks
   :target: https://pypi.org/project/instawebhooks/
   :alt: PyPI - License

.. |code-style-badge| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: black

.. |lint-badge| image:: https://img.shields.io/badge/linting-pylint-yellowgreen
   :target: https://github.com/pylint-dev/pylint
   :alt: Linting: pylint

|ci-badge| |pypi-version| |python-versions| |license-badge| |code-style-badge| |lint-badge|

    `Documentation <https://instawebhooks.readthedocs.io/>`_

Monitor Instagram accounts for new posts and send them to a Discord webhook.

* Works with **any Instagram account**, including private accounts if you are a follower
* Customizable **Discord embeds** for new posts and message contents including **mentions/pings**
* **User-definable refresh interval** for checking for new posts the second they are posted

.. image:: https://raw.githubusercontent.com/RyanLua/InstaWebhooks/main/assets/ScreenshotEmbedExample.png
   :alt: Example of a new post notification
   :width: 512px

What is InstaWebhooks?
-----------------------

InstaWebhooks is a Python package CLI that allows you to monitor Instagram accounts for new posts and send them to a Discord webhook. It is designed to be simple to use and easy to set up, with a focus on customizability and ease of use.

Internally, InstaWebhooks uses `Instaloader <https://instaloader.github.io/>`_ to fetch Instagram posts and `Discord Webhooks <https://discord.com/developers/docs/resources/webhook>`_ to send messages to Discord via `requests <https://requests.readthedocs.io/en/latest/>`_ which happens to be the same dependency Instaloader uses. It uses `argparse <https://docs.python.org/3/library/argparse.html>`_ for the CLI and `logging <https://docs.python.org/3/library/logging.html>`_ for logging.

Example
-------

Below, InstaWebhooks is monitoring the Instagram account `raenlua <https://www.instagram.com/raenlua/>`_ for new posts and sending them to a Discord webhook every 30 minutes and sends a message to Discord with the post URL and the owner's name.

.. code:: console

    # Install InstaWebhooks
    pip install instawebhooks

    # Run InstaWebhooks with custom message contents
    instawebhooks -c "New post from {owner_name}: {post_url}" raenlua https://discord.com/api/webhooks/0123456789/abcdefghijklmnopqrstuvwxyz

What it looks like:

.. image:: https://github.com/user-attachments/assets/15ce14a6-01ba-4675-a62e-d9c24128490b
   :alt: Example of a customized message
   :width: 512px

Installation
------------

InstaWebhooks is available on `PyPI <https://pypi.org/project/instawebhooks/>`_, and can be installed using `pip`:

.. code:: console

    pip install instawebhooks

For more ways to install, see `Installation <https://instawebhooks.readthedocs.io/en/latest/installation.html>`_.

Usage
-----

You can run ``instawebhooks --help`` to see the full list of options and arguments available.

The most basic usage of InstaWebhooks is to provide an Instagram account and a Discord webhook URL (replace ``<INSTAGRAM_USERNAME>`` and ``<DISCORD_WEBHOOK_URL>``):

.. code:: console

    instawebhooks <INSTAGRAM_USERNAME> <DISCORD_WEBHOOK_URL>

For more about each option and argument, including example templates, see `Usage <https://instawebhooks.readthedocs.io/en/latest/usage.html>`_.

Contributing
------------

For contributions, see the `contributing guidelines <CONTRIBUTING.md>`_.

This project supports `development containers <https://containers.dev/>`_, allowing you to instantly setup your development environment. For more, read about `installing from dev container <https://instawebhooks.readthedocs.io/en/latest/installation.html#from-development-container>`_.
