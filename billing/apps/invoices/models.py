from django.db import models

# Create your models here.
from django.db import models

class Invoice(models.Model):

    number = models.CharField(unique=True, max_length=50)
    customer = models.ForeignKey(
        "accounts.Customer",
        on_delete=models.PROTECT
    )

    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        choices=[("draft","Draft"),("paid","Paid"),("failed","Failed")],
        max_length=10
    )
    issued_at = models.DateTimeField(auto_now_add=True)