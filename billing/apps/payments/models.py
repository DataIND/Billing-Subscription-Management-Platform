from django.db import models

# Create your models here.

class Payment(models.Model):

    invoice = models.ForeignKey(
        "invoices.Invoice",
        on_delete=models.PROTECT
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    idempotency_key = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)