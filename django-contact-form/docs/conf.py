"""
Configuration file for the Sphinx documentation builder:

https://www.sphinx-doc.org/

"""
import os
import sys

import django_contact_form

extensions = [
    "notfound.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxcontrib_django",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "django-contact-form"
copyright = "2007, James Bennett"
version = django_contact_form.__version__
release = django_contact_form.__version__
exclude_trees = ["_build"]
pygments_style = "sphinx"
htmlhelp_basename = "django-contact-formdoc"
html_theme = "furo"
latex_documents = [
    (
        "index",
        "django-contact-form.tex",
        "django-contact-form Documentation",
        "James Bennett",
        "manual",
    )
]

intersphinx_mapping = {
    "django": (
        "https://docs.djangoproject.com/en/stable/",
        "https://docs.djangoproject.com/en/stable/_objects/",
    ),
    "python": ("https://docs.python.org/3", None),
}

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if "spelling" in sys.argv:
    extensions.append("sphinxcontrib.spelling")

# Spelling language.
spelling_lang = "en_US"

# Location of word list.
spelling_word_list_filename = "spelling_wordlist.txt"

# OGP metadata configuration.
ogp_enable_meta_description = True
ogp_site_url = "https://django-contact-form.readthedocs.io/"

# Django settings for sphinxcontrib-django.
sys.path.insert(0, os.path.abspath("."))
django_settings = "docs_settings"
