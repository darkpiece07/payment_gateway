from django.db import models

# Create your models here.

class Kulfi(models.Model):
    name = models.CharField(max_length = 100)
    amount = models.CharField(max_length = 100)
    payment_id = models.CharField(max_length = 100)
    paid = models.BooleanField(default = False)
    


class Payment(models.Model):
    payment_id = models.CharField(max_length = 100)
    order_id = models.CharField(max_length = 100)
    signature = models.CharField(max_length = 100)

