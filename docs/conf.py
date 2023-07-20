# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# conf.py

import os
import sys
import django

# Add your Django project path
sys.path.insert(0, os.path.abspath('..'))

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_SatFlora.settings')
django.setup()

# Sphinx configuration
project = 'SatFlora'
author = 'Your Name'
version = '1.0'
release = '1.0.0'
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'  # Use the ReadTheDocs theme
extensions.append('sphinx.ext.autosummary')