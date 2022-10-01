from django.shortcuts import render
from rest_framework import generics
from price_tracker.models import PriceTracker
from price_tracker.serializers import PriceTrackerSerializer


class PriceTrackerViewSet(generics.ListAPIView):
    """
    Price Tracker List API
    """
    queryset = PriceTracker.objects.all()
    serializer_class = PriceTrackerSerializer
