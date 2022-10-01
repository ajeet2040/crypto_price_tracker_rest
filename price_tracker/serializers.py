from rest_framework import serializers
from price_tracker.models import PriceTracker


class PriceTrackerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Price Tracker
    """
    class Meta:
        model = PriceTracker
        fields = ['timestamp', 'price', 'coin']
