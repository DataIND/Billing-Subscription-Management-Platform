# core/services/payment_service.py
from django.db import transaction
from apps.payments.models import Payment
from apps.invoices.models import Invoice


class PaymentService:

    @staticmethod
    @transaction.atomic
    def process_payment(invoice: Invoice, idempotency_key: str):

        if Payment.objects.filter(idempotency_key=idempotency_key).exists():
            return Payment.objects.get(idempotency_key=idempotency_key)

        payment = Payment.objects.create(
            invoice=invoice,
            amount=invoice.total,
            status="success",
            idempotency_key=idempotency_key,
        )

        invoice.status = Invoice.PAID
        invoice.save()

        return payment