.. InstaWebhooks documentation master file, created by
   sphinx-quickstart on Tue Dec  3 22:03:26 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

InstaWebhooks documentation
===========================

InstaWebhooks is a `Python <https://www.python.org/>`_ command-line interface which allows you to monitor any Instagram account for new posts and then send them to a `Discord webhook <https://discord.com/developers/docs/resources/webhook>`_.

Quickstart
----------

With `Python <https://www.python.org/>`_ installed, install InstaWebhooks with `pip <https://pypi.org/project/pip/>`_:

.. code:: console

    $ pip install instawebhooks

After installing, you can run InstaWebhooks with the following command (change the username and webhook URL to your own):

.. code:: console

    $ instawebhooks raenlua https://discord.com/api/webhooks/0123456789/abcdefghijklmnopqrstuvwxyz

Now, whenever the Instagram account `@raenlua` posts a new photo, it will be sent to the Discord webhook.

Contents
--------

.. toctree::

   getting-started
   installation
   usage

.. toctree::
   :caption: Project

   Contributing <https://github.com/RyanLua/InstaWebhooks/blob/docs-site/CONTRIBUTING.md>
   Code of Conduct <https://github.com/RyanLua/InstaWebhooks/tree/docs-site?tab=coc-ov-file#readme>
   GitHub <https://github.com/RyanLua/InstaWebhooks>
   PyPI <https://pypi.org/project/instawebhooks>