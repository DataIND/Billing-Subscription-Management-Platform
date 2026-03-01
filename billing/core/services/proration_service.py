# core/services/proration_service.py
from decimal import Decimal


class ProrationService:

    @staticmethod
    def calculate(old_price, new_price, days_used, total_days):
        unused_ratio = Decimal(total_days - days_used) / Decimal(total_days)
        return (new_price - old_price) * unused_ratio