from .base import *

# Override anything in base_docker.py here before renaming the file to
# local_settings.py.
#
# The file can be managed using a new image, docker config, or a shared volume


DEBUG = True

DATABASE_ENGINE = 'mysql'
DATABASE_OPTIONS = {
    'use_unicode': True,
    'charset': 'utf8',
}

INSTALLED_APPS += ('django_cas_ng',)

MIDDLEWARE_CLASSES += ('django_cas_ng.middleware.CASMiddleware',)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)

CAS_SERVER_URL = "https://cas.wm.edu/cas/"

# Needed to enable compression JS and CSS files
COMPRESS = True
MEDIA_URL = '/media/'
MEDIA_ROOT = 'rooibos/static/'


ADMINS = (
#    ('Your name', 'your@email.example'),
)

MANAGERS = ADMINS

# Settings for MySQL
DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_OPTIONS = {
    'use_unicode': True,
    'charset': 'utf8',
}

# Settings for Microsoft SQL Server (use the appropriate driver setting)
#DATABASE_ENGINE = 'sql_server.pyodbc'
#DATABASE_OPTIONS= {
#    'driver': 'SQL Native Client',             # FOR SQL SERVER 2005
#    'driver': 'SQL Server Native Client 10.0', # FOR SQL SERVER 2008
#    'MARS_Connection': True,
#}

# Settings for all database systems
# DATABASE_NAME = 'mdid3'             # Or path to database file if using sqlite3.
# DATABASE_USER = 'mdid3'             # Not used with sqlite3.
# DATABASE_PASSWORD = ''         # Not used with sqlite3.
# DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

DEFAULT_CHARSET = 'utf-8'
DATABASE_CHARSET = 'utf8'

CLOUDFILES_API_KEY = ''

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ahj;dghjklasgkjh412897t2789gdsajhk'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

SOLR_URL = 'http://127.0.0.1:8983/solr/rooibos'

SCRATCH_DIR = '/var/mdid/media/scratch/'
AUTO_STORAGE_DIR = '/var/mdid/media/auto_storage/'

# File upload size limit in bytes (default 5 MB)
UPLOAD_LIMIT = 5 * 1024 * 1024

# Legacy setting for ImageViewer 2 support
SECURE_LOGIN = False


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

INTERNAL_IPS = ('127.0.0.1',)

HELP_URL = 'http://mdid.org/help/'

DEFAULT_LANGUAGE = 'en-us'

GOOGLE_ANALYTICS_MODEL = True

# Set to None if you don't subscribe to ARTstor
ARTSTOR_GATEWAY = 'http://sru.artstor.org/SRU/artstor.htm'


SESSION_COOKIE_AGE = 6 * 3600  # in seconds

SSL_PORT = None  # ':443'

# Theme colors for use in CSS
PRIMARY_COLOR = "rgb(152, 189, 198)"
SECONDARY_COLOR = "rgb(118, 147, 154)"

LOGO_URL = '/static/images/wmdid.png'
FAVICON_URL = None
COPYRIGHT = '&copy College of William &amp; Mary'
TITLE = 'WMDID'

WWW_AUTHENTICATION_REALM = "Please log in to access media from MDID at Your University"

CUSTOM_TRACKER_HTML = ""


SHOW_FRONTPAGE_LOGIN = 'yes'

# The Megazine viewer is using a third party component that has commercial
# licensing requirements.  To enable the component you need to enter your
# license key, which is available for free for educational institutions.
# See static/megazine/COPYING.
MEGAZINE_PUBLIC_KEY = ""

# To use a commercial licensed flowplayer, enter your flowplayer key here
# and add the flowplayer.commercial-3.x.x.swf file to the
# rooibos/static/flowplayer directory
FLOWPLAYER_KEY = ""

# MDID uses some Yahoo APIs that require an application key
# You can get one at https://developer.apps.yahoo.com/dashboard/createKey.html
YAHOO_APPLICATION_ID = ""


# By default, video delivery links are created as symbolic links. Some streaming
# servers (e.g. Wowza) don't deliver those, so hard links are required.
HARD_VIDEO_DELIVERY_LINKS = False


# MASTER_TEMPLATE = 'master_root.html'

additional_settings = [
#    'apps.jmutube.settings_local',
#    'apps.svohp.settings_local',
]
