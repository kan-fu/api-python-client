# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "onc"
copyright = "2023, ONC Data Team"
author = "ONC Data Team"
release = "2.3.5"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Extension configuration -------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
]

# nb_execution_mode is off for faster local build. It is deleted in GitHub Action doc.yml
nb_execution_mode = "off"
nb_merge_streams = True
nb_execution_timeout = 60
nb_execution_raise_on_error = True

autoapi_dirs = ["../../src"]
autoapi_ignore = ["*modules*"]
suppress_warnings = ["autoapi.python_import_resolution"]
