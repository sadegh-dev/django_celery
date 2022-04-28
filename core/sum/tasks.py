from celery import shared_task
from .models import SumNumbers
import time

@shared_task
def adding(x, y, id):
    time.sleep(10)
    num = SumNumbers.objects.get(id =id)
    num.result = x+y
    num.save()
    return num.result



