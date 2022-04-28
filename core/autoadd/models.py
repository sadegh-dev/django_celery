from django.db import models


class MyTime(models.Model):
    release = models.DateTimeField()
    
    def __str__(self):
        return self.release

