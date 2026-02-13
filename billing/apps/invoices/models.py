from django.db import models

# Create your models here.
from django.db import models

class Invoice(models.Model):
    DRAFT = "draft"
    PAID = "paid"
    FAILED = "failed"

    STATUSES = [(DRAFT, "Draft"), (PAID, "Paid"), (FAILED, "Failed")]

    number = models.CharField(unique=True, max_length=50)
    customer = models.ForeignKey("accounts.Customer", on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUSES)
    issued_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old = Invoice.objects.get(pk=self.pk)
            if old.status == self.PAID:
                raise ValueError("Paid invoices are immutable")
        super().save(*args, **kwargs)