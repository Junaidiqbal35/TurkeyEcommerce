import os

# set the default Django settings module for the 'celery' program.
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

app = Celery('web_project', backend='redis', broker='redis://localhost:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.timezone = 'UTC'
app.autodiscover_tasks()
