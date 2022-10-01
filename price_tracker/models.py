from django.db import models
from django.utils.timezone import now as utcnow


class PriceTracker(models.Model):
    """
    Model for Price Tracker of crypto currency.
    """
    SUPPORTED_CURRENCIES = [('btc', 'Bitcoin')]

    timestamp = models.DateTimeField(default=utcnow)
    coin = models.CharField(max_length=100, blank=False, null=False, choices=SUPPORTED_CURRENCIES)
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=25)

    class Meta:
        ordering = ['timestamp']