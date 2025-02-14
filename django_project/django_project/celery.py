import os
from celery import Celery


from .settings.base import DEBUG


if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings.production')

celery_app = Celery('django_project')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


@celery_app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')