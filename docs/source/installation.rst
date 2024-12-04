Usage
=====

Installation
------------

InstaWebhooks expects that you have `Python 3.8 or higher <https://www.python.org/downloads/>`_ (and `pip <https://pypi.org/project/pip/>`_ if you are using it to install) to be installed.

Using pip (recommended)
-----------------------

The recommended way to install is using `pip <https://pypi.org/project/pip/>`_. This allows for easy installation, upgrading, and installation.

To install:

.. code-block:: console

    pip3 install instawebhooks

To upgrade to its latest release:

.. code-block:: console

    pip3 install --upgrade instawebhooks

From development container
--------------------------

We fully support `development containers <https://containers.dev/>`_ for easily getting started, whether you want to test out InstaWebhooks before installing it or if you want to contribute.

GitHub Codespaces
~~~~~~~~~~~~~~~~~

.. image:: https://github.com/codespaces/badge.svg
   :target: https://codespaces.new/RyanLua/InstaWebhooks?quickstart=1
   :alt: Open in GitHub Codespaces

1. To get started, click the "Open in GitHub Codespaces" badge or the Code button, then click the Codespaces tab, and "Create codespace on main"
   .. image:: https://github.com/user-attachments/assets/229f37b8-9650-4809-b79a-37a565f6c855
      :alt: Create codespace on main
2. You may be prompted to configure your codespace, you can leave it alone since the default configuration is adequate enough
3. Wait for the codespace to be created and fully loaded. InstaWebhooks will be installed automatically.

For more information about creating a codespace, see `Creating a codespace for a repository <https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository>`_.

Visual Studio Code
~~~~~~~~~~~~~~~~~~

.. image:: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
   :target: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/RyanLua/InstaWebhooks
   :alt: Open in Dev Containers

1. Follow the `installation steps for Visual Studio Code Dev Containers <https://code.visualstudio.com/docs/devcontainers/containers#_installation>`_.
2. Click the "Open in Dev Containers" badge or locally clone this repository and click "Reopen in Container" from the `Dev Containers extension <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers>`_.
   .. image:: https://github.com/user-attachments/assets/c1fb1ba6-a423-4e03-9d69-d7df6635583d
      :alt: Reopen in Container
3. Wait for the codespace to be created and fully loaded. InstaWebhooks will be installed automatically.

For more information about dev containers in Visual Studio Code, see `Developing inside a Container <https://code.visualstudio.com/docs/devcontainers/containers#_installation>`_.

From source code
----------------

You can additionally install from source code. This allows you to modify the Python code yourself (i.e. change the embed looks or message contents).

1. `Clone the repository <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`_ onto your machine

   .. code-block:: console

       git clone https://github.com/RyanLua/InstaWebhooks.git

2. Navigate to the repository's directory

   .. code-block:: console

       cd InstaWebhooks

3. Install the required packages that InstaWebhooks uses:

   .. code-block:: console

       pip3 install -r requirements.txt

4. Enter `Development Mode <https://setuptools.pypa.io/en/latest/userguide/development_mode.html>`_:

   .. code-block:: console

       pip3 install --editable .