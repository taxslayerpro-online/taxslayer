# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'TaxSlayerPro Login / My Account'
copyright = '2025, TaxSlayerPro'
author = 'TaxSlayerPro Support Guide'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add more if needed later)
extensions = []

# Allow raw HTML inside .rst files (needed for buttons & CSS)
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Recommended theme (uncomment if installed)
# html_theme = 'sphinx_rtd_theme'

# SEO-friendly page titles
html_title = "TaxSlayerPro Login | My Account Access & Help Guide"
html_short_title = "TaxSlayerPro Login"

# Favicon (place file in _static or root)
html_favicon = 'favicon.ico'

# Hide “View page source”
html_show_sourcelink = False

# Allow unsafe raw HTML (required for embedded styles & buttons)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (CSS, images, favicon)
# html_static_path = ['_static']
