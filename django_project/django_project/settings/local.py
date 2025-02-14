"""
This file  contains settings of project for local environemnt.
"""
# pylint: disable=W0614
from .base import * # pylint: disable=W0401

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') 
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
