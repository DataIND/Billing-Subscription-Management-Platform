# core/services/audit_service.py
from apps.audit.models import AuditLog


class AuditService:

    @staticmethod
    def log(actor, action, before=None, after=None):
        AuditLog.objects.create(
            actor=actor,
            action=action,
            before=before,
            after=after,
        )