"""Generate the documentation for hrid."""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

import sphinx_autosummary_accessors

sys.path.insert(0, os.path.abspath("../../src/hrid"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "hrid"
copyright = "2024, Evelyn King"
author = "Evelyn King"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["numpydoc", "sphinx.ext.autodoc", "sphinx.ext.autosummary"]

# The suffix of source filenames
source_suffix = ".rst"

# The master toctree document
master_doc = "index"

templates_path = ["_templates", sphinx_autosummary_accessors.templates_path]
exclude_patterns = []

autosummary_generate = True

pygments_style = "sphinx"

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# -- Options for HTML output --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

htmlhelp_basename = "hriddoc"
