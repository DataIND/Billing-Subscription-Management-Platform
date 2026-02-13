from django.db import models

# Create your models here.
from django.db import models

class Price(models.Model):
    FLAT = "flat"
    USAGE = "usage"

    PRICING_TYPES = [(FLAT, "Flat"), (USAGE, "Usage")]

    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interval = models.CharField(max_length=10)
    pricing_type = models.CharField(max_length=10, choices=PRICING_TYPES)