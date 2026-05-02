from django.db import models

# Create your models here.

class Subscription(models.Model):

    TRIALING = "trialing"
    ACTIVE = "active"
    PAST_DUE = "past_due"
    CANCELED = "canceled"
    PAUSED = "paused"

    STATES = [
        (TRIALING, "Trialing"),
        (ACTIVE, "Active"),
        (PAST_DUE, "Past Due"),
        (CANCELED, "Canceled"),
        (PAUSED, "Paused"),
    ]

    customer = models.ForeignKey(
        "accounts.Customer",
        on_delete=models.PROTECT
    )

    price = models.ForeignKey(
        "pricing.Price",
        on_delete=models.PROTECT
    )

    status = models.CharField(max_length=20, choices=STATES)
    current_period_start = models.DateTimeField()
    current_period_end = models.DateTimeField()