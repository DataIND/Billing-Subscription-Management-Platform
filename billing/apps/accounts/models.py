import uuid
from django.db import models


class Customer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    external_id = models.UUIDField(unique=True)
    email = models.EmailField()
    currency = models.CharField(max_length=3)
    billing_address = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)