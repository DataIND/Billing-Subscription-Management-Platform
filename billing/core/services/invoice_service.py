# core/services/invoice_service.py
import uuid
from django.db import transaction
from apps.invoices.models import Invoice


class InvoiceService:

    @staticmethod
    @transaction.atomic
    def create_invoice(customer, amount):
        return Invoice.objects.create(
            number=f"INV-{uuid.uuid4()}",
            customer=customer,
            total=amount,
            status=Invoice.DRAFT,
        )

    @staticmethod
    @transaction.atomic
    def mark_paid(invoice: Invoice):
        if invoice.status == Invoice.PAID:
            raise ValueError("Invoice already paid")

        invoice.status = Invoice.PAID
        invoice.save()
        return invoice