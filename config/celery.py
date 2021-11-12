import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTING_MODULE", 'config.settings.dev')

app = Celery('config')
app.config_from_object('config.settings.dev', namespace='CELERY')
app.autodiscover_tasks()