import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "number_cruncher.settings")

app = Celery("number_cruncher")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
