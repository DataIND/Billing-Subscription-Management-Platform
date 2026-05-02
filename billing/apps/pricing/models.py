from django.db import models

# Create your models here.

class Price(models.Model):

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.PROTECT,
        related_name="prices"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    interval = models.CharField(max_length=20)

    pricing_type = models.CharField(max_length=20)