Installation
============

InstaWebhooks expects that you have `Python 3.10 or higher <https://www.python.org/downloads/>`_ (and `pip <https://pypi.org/project/pip/>`_ if you are using it to install) to be installed.

Using pip (recommended)
-----------------------

The recommended way to install is using `pip <https://pypi.org/project/pip/>`_. This allows for easy installation and upgrading.

To install:

.. code:: console

    $ pip install instawebhooks

To upgrade to its latest release:

.. code:: console

    $ pip install --upgrade instawebhooks

From development container
--------------------------

`Development containers <https://containers.dev/>`_ can be used setup your machine for contributing InstaWebhooks.

GitHub Codespaces
~~~~~~~~~~~~~~~~~

.. image:: https://github.com/codespaces/badge.svg
   :target: https://codespaces.new/ryanlua/instawebhooks?quickstart=1
   :alt: Open in GitHub Codespaces

1. To get started, click the "Open in GitHub Codespaces" badge or the Code button, then click the Codespaces tab, and "Create codespace on main"

.. figure:: https://github.com/user-attachments/assets/229f37b8-9650-4809-b79a-37a565f6c855
   :alt: Create codespace on main

   Button to create codespace on main

2. You may be prompted to configure your codespace, you can leave it alone since the default configuration is adequate enough
3. Wait for the codespace to be created and fully loaded. InstaWebhooks will be installed automatically.

For more information about creating a codespace, see `Creating a codespace for a repository <https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository>`_.

Visual Studio Code
~~~~~~~~~~~~~~~~~~

.. image:: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
   :target: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/ryanlua/instawebhooks
   :alt: Open in Dev Containers

1. Follow the `installation steps for Visual Studio Code Dev Containers <https://code.visualstudio.com/docs/devcontainers/containers#_installation>`_.
2. Click the "Open in Dev Containers" badge or locally clone this repository and click "Reopen in Container" from the `Dev Containers extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers>`_.

.. figure:: https://github.com/user-attachments/assets/c1fb1ba6-a423-4e03-9d69-d7df6635583d
   :alt: Reopen in Container

   Notification to reopen in container

3. Wait for the codespace to be created and fully loaded. InstaWebhooks will be installed automatically.

For more information about dev containers in Visual Studio Code, see `Developing inside a Container <https://code.visualstudio.com/docs/devcontainers/containers#_installation>`_.

From source code
----------------

Installing from source code is another option to contribute or use the latest development version.

1. `Clone the repository <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`_ onto your machine

.. code:: console

    $ git clone https://github.com/ryanlua/instawebhooks.git

2. Navigate to the repository's directory

.. code:: console

    $ cd instawebhooks

3. Install the required packages that InstaWebhooks uses:

.. code:: console

    $ pip install -r requirements.txt

4. Enter `Development Mode <https://setuptools.pypa.io/en/latest/userguide/development_mode.html>`_:

.. code:: console

    $ pip install --editable .
