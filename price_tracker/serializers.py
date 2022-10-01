"""Module containing all serializers"""
from rest_framework import serializers
from price_tracker.models import PriceTracker


class PriceTrackerSerializer(serializers.ModelSerializer):
    """
    Serializer for Price Tracker
    """

    class Meta:
        model = PriceTracker
        fields = ['timestamp', 'price', 'coin']

    def to_representation(self, instance):
        """
        Change data type of price from decimal to int
        """
        representation = super().to_representation(instance)
        representation['price'] = round(instance.price)
        return representation
