# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'InstaWebhooks'
copyright = '2024, Ryan Luu'
author = 'Ryan Luu'
release = '0.1.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ['_static']

html_theme_options = {
    "announcement": "This is a early version of the documentation and not final.",
    "source_repository": "https://github.com/RyanLua/InstaWebhooks",
    "source_branch": "main",
    "source_directory": "docs/source",
}

# -- Options for sphinx_copybutton ----------------------------------------------------

copybutton_prompt_text = r"\$ | C\:\> "
copybutton_prompt_is_regexp = True