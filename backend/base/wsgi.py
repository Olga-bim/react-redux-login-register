import os
from django.core.wsgi import get_wsgi_application

# Указываем путь к файлу настроек в папке backend/myproj
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.myproj.settings')

application = get_wsgi_application()
