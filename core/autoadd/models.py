from django.db import models


class MyTime(models.Model):
    release = models.DateTimeField()

