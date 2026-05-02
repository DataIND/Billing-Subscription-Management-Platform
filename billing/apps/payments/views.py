from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.invoices.models import Invoice
from apps.payments.serializers import PaymentSerializer
from core.services.payment_service import PaymentService

# Create your views here.
class PaymentView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        invoice_id = request.data.get("invoice")
        idempotency_key = request.headers.get("Idempotency-Key")
        invoice = Invoice.objects.get(id=invoice_id)
        payment = PaymentService.process_payment(
            invoice,
            idempotency_key
        )
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)