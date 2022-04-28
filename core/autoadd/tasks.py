from celery import shared_task
from .models import MyTime

from datetime import datetime

@shared_task
def set_time():
    the_time = MyTime(release = datetime.now())
    the_time.save()
    return True

