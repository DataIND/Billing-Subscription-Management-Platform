# core/services/subscription_service.py
from django.db import transaction
from django.utils.timezone import now
from apps.subscriptions.models import Subscription


class SubscriptionService:

    @staticmethod
    @transaction.atomic
    def activate(subscription: Subscription):
        if subscription.status not in [Subscription.TRIALING, Subscription.PAST_DUE]:
            raise ValueError("Invalid state transition")

        subscription.status = Subscription.ACTIVE
        subscription.current_period_start = now()
        subscription.save()
        return subscription

    @staticmethod
    @transaction.atomic
    def cancel(subscription: Subscription):
        subscription.status = Subscription.CANCELED
        subscription.save()
        return subscription

    @staticmethod
    @transaction.atomic
    def pause(subscription: Subscription):
        subscription.status = Subscription.PAUSED
        subscription.save()
        return subscription