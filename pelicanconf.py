AUTHOR = 'Aaron K'
SITENAME = 'Aaron Kyle'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# FAVICON
STATIC_PATHS = ['theme/images', 'images']
USE_SHORTCUT_ICONS=True

# Blogroll
LINKS = (('Contact Me', 'https://aaronkylec.com/'),
         ('LinkedIn', 'https://www.linkedin.com/in/aaronkcarpenter/'),
         ('Twitter', 'https://twitter.com/_kyleaaron')),

# Social widget
SOCIAL = (('github', 'https://www.github.com/aaronkcarpenter'),
          ('linkedin-square', 'https://www.linkedin.com/in/aaronkcarpenter/'),
          ('facebook','https://www.facebook.com/aaron.carpenter.77377/'),
          ('twitter', 'https://twitter.com/_kyleaaron')
          )

DEFAULT_PAGINATION = 10
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# PLUGIN PATH AND PLUGINS IN USE
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'neighbors', 'tipue_search.tipue_search']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc' :{'permalink' : 'true'}
    },
    'output_format': 'html5',
}

THEME = 'pelican-themes/elegant'

