from Weather.settings.base import *
import django_heroku

django_heroku.settings(locals())