
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')  # Замените base на имя вашего приложения
application = get_wsgi_application()
