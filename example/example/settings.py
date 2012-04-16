TEMPLATE_DEBUG = DEBUG = True
DATABASES = { 'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': '.db',
}}
MEDIA_ROOT = MEDIA_URL = STATIC_ROOT = ''
STATIC_URL = '/static/'
SECRET_KEY = 'n!-0+-aoaim*)-qiwmml)10=v8pi#^4n2u)fl1fh%siu*7@*sg'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'example.urls'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'sample',
)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        }
}