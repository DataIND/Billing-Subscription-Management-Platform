from celery import shared_task
from django.utils.timezone import now

from apps.subscriptions.models import Subscription
from apps.invoices.models import Invoice


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=30)
def run_monthly_billing(self):

    subscriptions = Subscription.objects.filter(
        status=Subscription.ACTIVE,
        current_period_end__lte=now()
    )

    for sub in subscriptions:

        invoice = Invoice.objects.create(
            number=f"INV-{sub.id}-{now().date()}",
            customer=sub.customer,
            total=sub.price.amount,
            status="draft"
        )

        print(f"Generated invoice {invoice.number}")