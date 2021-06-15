#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

development = not True
#ARTICLE_EXCLUDES = ['profs']

if development:
    RELATIVE_URLS = False
else :
    SITEURL = 'http://ulm.rock4temps.fr/public/'


OUTPUT_PATH = 'public/'
AUTHOR = 'R4T ENS Ulm'
copy_date = 2020
SITENAME = 'Club Rock 4 Temps ENS Ulm'

SITELOGO = 'images/logo4tps_blanc.png'
SITELOGO_SIZE = "25em"
FOOTERLOGO_SIZE = "35em"

BANNER = 'images/helo_nikita.jpg'
BANNER_SUBTITLE = """Bienvenue ! <br/> 
Retrouvez sur cette page les dernières activités du club, mise à jour hebdomadaire."""


PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme plugins & extensions

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

PLUGIN_PATHS = ["data/plugins"]
PLUGINS = ["i18n_subsites", "jinja2content", ]  # "tipue_search", ]
I18N_TEMPLATES_LANG = 'fr'

THEME = "themes/pelican-bootstrap3"
BOOTSTRAP_THEME = 'yeti_ulm'

PYGMENTS_STYLE = "monokai"
CUSTOM_CSS = 'theme/css/custom.css'

# Pelican Theme specials

DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = 'Actualités'

# Articles

SHOW_ARTICLE_CATEGORY = True
SHOW_ARTICLE_AUTHOR = True
HIDE_SIDEBAR = True

SLUGIFY_SOURCE = 'title'

SUMMARY_MAX_LENGTH = 140
SUMMARY_END_SUFFIX = '[…]'
SUMMARY_END_MARKER = '[…]'

# Order content

PAGE_PATHS = ['pages']
PAGE_ORDER_BY = "page-order"
PAGES_SORT_ATTRIBUTE = 'basename'


# Blogroll -- not used (sidebar), but keeping it here in case it is
LINKS = (
    ('Facebook du P4T', 'https://www.facebook.com/Printemps4Temps/ '),
    ('YouTube du P4T',
     'https://www.youtube.com/channel/UCFU1BM6d0mQzLJkha1idTtw '),
    ("Instagram du P4T", 'https://www.instagram.com/printemps4temps/'),
)

# Social widget
SOCIAL = (
    ('Facebook du Club',
     'https://www.facebook.com/Club-de-rock-4-temps-de-lENS-dUlm-375879339657986/'),
    ('YouTube du Club',
     'https://www.youtube.com/channel/UCENi2WW1tbMwdZFzfaLUu1g'),
)

DEFAULT_PAGINATION = 6

