"""Module to defined django views that responds to REST API calls."""
from collections import OrderedDict
from rest_framework import generics, pagination, exceptions
from price_tracker.models import PriceTracker
from price_tracker.serializers import PriceTrackerSerializer
from rest_framework.response import Response

from price_tracker.utils import generate_date


class CustomPagination(pagination.LimitOffsetPagination):
    """
    Custom Pagination to override default behaviour
    """
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 10000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('url', self.request.build_absolute_uri()),
            ('next', self.get_next_link()),
            ('count', self.count),
            ('data', data)
        ]))


class PriceTrackerViewSet(generics.ListAPIView):
    """
    Price Tracker List API
    """
    queryset = PriceTracker.objects.all()
    pagination_class = CustomPagination
    serializer_class = PriceTrackerSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned records to a given date,
        by filtering against a `date` query parameter in the URL.
        """
        queryset = PriceTracker.objects.all()
        # Optional Filter for date
        date = self.request.query_params.get('date')
        if date is not None:
            try:
                date_filter = generate_date(date, '%d-%m-%Y')
                queryset = queryset.filter(timestamp__date=date_filter)
            except ValueError as err:
                raise exceptions.ValidationError({"error": "Date format for 'date' param should be 'DD-MM-YYYY'!"})
        return queryset
