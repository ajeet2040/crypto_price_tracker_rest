from django.test import TestCase

# Create your tests here.

import pytest
from django.urls import reverse

from price_tracker.models import PriceTracker
from price_tracker.serializers import PriceTrackerSerializer


@pytest.mark.django_db
def test_list_prices(client):
    """Sample Test Case to test list of all prices."""
    url = reverse('prices')
    response = client.get(url)

    prices = PriceTracker.objects.all()
    expected_data = PriceTrackerSerializer(prices, many=True,).data

    assert response.status_code == 200
    assert response.data["data"] == expected_data


@pytest.mark.django_db
def test_list_prices(client):
    """Sample Test Case to test list of all prices."""
    url = reverse('prices')
    response = client.get(url)

    prices = PriceTracker.objects.all()
    expected_data = PriceTrackerSerializer(prices, many=True,).data

    assert response.status_code == 200
    assert response.data["data"] == expected_data