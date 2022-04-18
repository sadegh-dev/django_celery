from celery import Celery, shared_task
from .models import MyTime

from datetime import datetime

@shared_task
def set_time(request):
    the_time = MyTime(release = datetime.now())
    the_time.save()
    return True

