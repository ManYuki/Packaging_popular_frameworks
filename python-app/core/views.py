from django.http import JsonResponse
from django.conf import settings
import environ
import os

env = environ.Env()
environ.Env.read_env(os.path.join(settings.BASE_DIR, '.env'))

def health_check(request):
    return JsonResponse({
        "status": "active", 
        "message": env("APP_MESSAGE", default="Default Django Config"), 
        "framework": "Django"
    })
