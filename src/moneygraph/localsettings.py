from settings import *  # @UnusedWildImport  # NOQA


ADMINS = ()
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = 'moneygraph.localurls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_DIR, 'moneygraph.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
