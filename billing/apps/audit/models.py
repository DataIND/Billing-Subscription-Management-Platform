from django.db import models

# Create your models here.

class AuditLog(models.Model):
    actor = models.CharField(max_length=100)
    action = models.CharField(max_length=200)
    before = models.JSONField(null=True)
    after = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)