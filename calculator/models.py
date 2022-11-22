from django.db import models

# Create your models here.
class Calculator(models.Model):
    num_1 = models.FloatField()
    num_2 = models.FloatField()
    sym = models.CharField(max_length=12, default=0)
    result = models.FloatField()



