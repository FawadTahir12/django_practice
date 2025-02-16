# your_app_name/tasks.py
import time
from celery import shared_task

@shared_task(name='addition_task', queue='worker1_queue')
def add(arg1, arg2):
    time.sleep(10)
    result = arg1 + arg2
    return result


@shared_task(name='subtraction_task', queue='worker2_queue')
def sub(arg1, arg2):
    time.sleep(10)
    result = arg1 - arg2
    return result