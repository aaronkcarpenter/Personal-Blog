AUTHOR = 'Aaron K'
SITENAME = 'aaronkyle'
RECENT_ARTICLES_COUNT=10
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Search Functionality
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"


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
         ('Twitter', 'https://twitter.com/_kyleaaron'),
         ('AngelList', 'https://angel.co/u/aaron-carpenter-4')),

# Social widget
SOCIAL_PROFILE_LABEL = u'Connect With Me'
SOCIAL = (('github', 'https://www.github.com/aaronkcarpenter'),
          ('linkedin-square', 'https://www.linkedin.com/in/aaronkcarpenter/'),
          ('facebook','https://www.facebook.com/aaron.carpenter.77377/'),
          ('twitter', 'https://twitter.com/_kyleaaron')
          )

DEFAULT_PAGINATION = 10
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# SEO
SITE_DESCRIPTION = (
    "Documenting the life and career of Entrepreneur & Software Engineer Aaron Kyle."
)

# PLUGIN PATH AND PLUGINS IN USE
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'neighbors', 'post_stats']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.4
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

READING_TIME_LOWER_LIMIT = 2

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

# LANDING_PAGE_TITLE = "Building Products with Code and Turning Them Into Money Makers"
LANDING_PAGE_TITLE = "Software Development | Entrepreneurship | Personal Development"

PROJECTS_TITLE = "Current Projects & Interests"

PROJECTS = [{
    'name': 'Entry/Exit Tool and Option Chain Scraper',
    'url': 'https://github.com/aaronkcarpenter/Automated-Option-Chain-Scraper',
    'description': 'Get the best entry and exit prices for SPY. Enter Trade. Profit.'
    },
    {'name': 'Analytics Site',
    'url': 'https://master.dhqg8jsbkxhqu.amplifyapp.com/',
    'description': 'I Built A Site Based Off Of A Few Endpoints Found On The Web.'
    },
    {'name': 'Portfolio Page',
    'url': 'http://www.aaronkylec.com',
    'description': 'Any Professional Inquiries Can Be Answered Here.'
    },
    {'name': 'Personal Blog',
    'url': 'http://www.aaronkyle.co',
    'description': 'I do front end development by day, but work heavily in Python for my personal projects.This blog is the first.'
    },
    {'name': 'Twitter Biz Bot',
    'url': 'https://github.com/aaronkcarpenter/Twitter-Biz-Bot',
    'description': 'Just combining my interests in web scraping, automation and Twitter to create a full automated Twitter profile.'
    },
    {'name': 'Bentley Bot',
    'url': 'https://github.com/aaronkcarpenter/Twitter-Biz-Bot',
    'description': 'Bentley auto-follows and auto-tweets randomly throughout the day. Built with Python, AWS Lambda Functions, and the Google Sheets API'
    },
    {
    'name': 'Aimé Leon Doré',
    'url': 'https://app-academy-capstone-project.web.app/',
    'description': 'One of the first projects that im still proud of.'
    }
    ]

