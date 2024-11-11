import os
from django.core.wsgi import get_wsgi_application

# Указываем правильный путь к настройкам
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.base.settings')  # Путь с учетом папки backend
application = get_wsgi_application()
