# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime, timezone
from importlib.metadata import version

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

__version__ = version("instawebhooks")

project = 'InstaWebhooks'
copyright = f'2024-{datetime.now(tz=timezone.utc).year}, Ryan Luu'
author = 'Ryan Luu'
version = ".".join(__version__.split(".")[:2])
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'sphinxarg.ext',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ['_static']

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/RyanLua/InstaWebhooks",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
        {
            "name": "Read the Docs",
            "url": "https://readthedocs.org/projects/instawebhooks",
            "html": """
                <svg x="0px" y="0px" viewBox="-125 217 360 360" xml:space="preserve">
                    <path fill="currentColor" d="M39.2,391.3c-4.2,0.6-7.1,4.4-6.5,8.5c0.4,3,2.6,5.5,5.5,6.3 c0,0,18.5,6.1,50,8.7c25.3,2.1,54-1.8,54-1.8c4.2-0.1,7.5-3.6,7.4-7.8c-0.1-4.2-3.6-7.5-7.8-7.4c-0.5,0-1,0.1-1.5,0.2 c0,0-28.1,3.5-50.9,1.6c-30.1-2.4-46.5-7.9-46.5-7.9C41.7,391.3,40.4,391.1,39.2,391.3z M39.2,353.6c-4.2,0.6-7.1,4.4-6.5,8.5 c0.4,3,2.6,5.5,5.5,6.3c0,0,18.5,6.1,50,8.7c25.3,2.1,54-1.8,54-1.8c4.2-0.1,7.5-3.6,7.4-7.8c-0.1-4.2-3.6-7.5-7.8-7.4 c-0.5,0-1,0.1-1.5,0.2c0,0-28.1,3.5-50.9,1.6c-30.1-2.4-46.5-7.9-46.5-7.9C41.7,353.6,40.4,353.4,39.2,353.6z M39.2,315.9 c-4.2,0.6-7.1,4.4-6.5,8.5c0.4,3,2.6,5.5,5.5,6.3c0,0,18.5,6.1,50,8.7c25.3,2.1,54-1.8,54-1.8c4.2-0.1,7.5-3.6,7.4-7.8 c-0.1-4.2-3.6-7.5-7.8-7.4c-0.5,0-1,0.1-1.5,0.2c0,0-28.1,3.5-50.9,1.6c-30.1-2.4-46.5-7.9-46.5-7.9 C41.7,315.9,40.4,315.8,39.2,315.9z M39.2,278.3c-4.2,0.6-7.1,4.4-6.5,8.5c0.4,3,2.6,5.5,5.5,6.3c0,0,18.5,6.1,50,8.7 c25.3,2.1,54-1.8,54-1.8c4.2-0.1,7.5-3.6,7.4-7.8c-0.1-4.2-3.6-7.5-7.8-7.4c-0.5,0-1,0.1-1.5,0.2c0,0-28.1,3.5-50.9,1.6 c-30.1-2.4-46.5-7.9-46.5-7.9C41.7,278.2,40.4,278.1,39.2,278.3z M-13.6,238.5c-39.6,0.3-54.3,12.5-54.3,12.5v295.7 c0,0,14.4-12.4,60.8-10.5s55.9,18.2,112.9,19.3s71.3-8.8,71.3-8.8l0.8-301.4c0,0-25.6,7.3-75.6,7.7c-49.9,0.4-61.9-12.7-107.7-14.2 C-8.2,238.6-10.9,238.5-13.6,238.5z M19.5,257.8c0,0,24,7.9,68.3,10.1c37.5,1.9,75-3.7,75-3.7v267.9c0,0-19,10-66.5,6.6 C59.5,536.1,19,522.1,19,522.1L19.5,257.8z M-3.6,264.8c4.2,0,7.7,3.4,7.7,7.7c0,4.2-3.4,7.7-7.7,7.7c0,0-12.4,0.1-20,0.8 c-12.7,1.3-21.4,5.9-21.4,5.9c-3.7,2-8.4,0.5-10.3-3.2c-2-3.7-0.5-8.4,3.2-10.3c0,0,0,0,0,0c0,0,11.3-6,27-7.5 C-16,264.9-3.6,264.8-3.6,264.8z M-11,302.6c4.2-0.1,7.4,0,7.4,0c4.2,0.5,7.2,4.3,6.7,8.5c-0.4,3.5-3.2,6.3-6.7,6.7 c0,0-12.4,0.1-20,0.8c-12.7,1.3-21.4,5.9-21.4,5.9c-3.7,2-8.4,0.5-10.3-3.2c-2-3.7-0.5-8.4,3.2-10.3c0,0,11.3-6,27-7.5 C-20.5,302.9-15.2,302.7-11,302.6z M-3.6,340.2c4.2,0,7.7,3.4,7.7,7.7s-3.4,7.7-7.7,7.7c0,0-12.4-0.1-20,0.7 c-12.7,1.3-21.4,5.9-21.4,5.9c-3.7,2-8.4,0.5-10.3-3.2c-2-3.7-0.5-8.4,3.2-10.3c0,0,11.3-6,27-7.5C-16,340.1-3.6,340.2-3.6,340.2z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    "announcement": "This is a early version of the documentation and not final.",
    "source_repository": "https://github.com/RyanLua/InstaWebhooks",
    "source_branch": "main",
    "source_directory": "docs/source",
}

# -- Options for sphinx_copybutton ----------------------------------------------------

copybutton_prompt_text = r"\$ | C\:\> "
copybutton_prompt_is_regexp = True
