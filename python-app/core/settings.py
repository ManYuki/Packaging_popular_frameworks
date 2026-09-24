import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY', default='unsafe-secret')
DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
INSTALLED_APPS = []
MIDDLEWARE = []
