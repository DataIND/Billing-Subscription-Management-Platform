from django.db import models

# Create your models here.

class UsageEvent(models.Model):
    customer = models.ForeignKey("accounts.Customer", on_delete=models.PROTECT)
    metric = models.CharField(max_length=100)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField()