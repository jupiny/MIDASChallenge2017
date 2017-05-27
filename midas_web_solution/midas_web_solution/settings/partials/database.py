# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

import os
import dj_database_url


DATABASES = {}
DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))
