from django.db import models

# Create your models here.

class SumNumbers(models.Model):
    id_task = models.CharField(max_length=100, null=True, blank=True)
    q = models.IntegerField()
    w = models.IntegerField()
    result = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.q} + {self.w} = {self.result} '

