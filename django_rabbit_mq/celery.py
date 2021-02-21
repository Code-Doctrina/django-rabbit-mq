import os
from celery  import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_rabbit_mq.settings')

app = Celery('django_rabbit_mq')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()