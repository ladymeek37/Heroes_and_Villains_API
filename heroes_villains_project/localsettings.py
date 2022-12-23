# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bsag&j9j^xs&78wih791dw)$10*h-ygp4ltr0!%+4)!f2^*kg^'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
}
}