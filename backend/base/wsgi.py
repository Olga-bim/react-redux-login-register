import os
from django.core.wsgi import get_wsgi_application

# Указываем правильный путь к файлу настроек
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproj.settings')

application = get_wsgi_application()
