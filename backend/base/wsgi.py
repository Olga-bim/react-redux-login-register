import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')  # Убедитесь, что здесь указано ваше приложение
application = get_wsgi_application()
