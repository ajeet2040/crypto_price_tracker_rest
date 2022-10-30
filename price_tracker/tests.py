from django.test import TestCase, Client

from django.urls import reverse

from price_tracker.models import PriceTracker
from price_tracker.serializers import PriceTrackerSerializer


class TestPriceAPI(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_list_prices(self):
        """Sample Test Case to test lists prices api."""
        # Create a sample object
        PriceTracker.objects.create(**{"coin":"btc", "price":100, "currency": "USD"})
        # Call list API
        url = reverse('prices')
        response = self.client.get(url)
        # Expected Data
        prices = PriceTracker.objects.all()
        expected_data = PriceTrackerSerializer(prices, many=True,).data
        print(expected_data)
        print(response.data["data"])
        # Assertions
        assert response.status_code == 200
        assert response.data["data"] == expected_data
