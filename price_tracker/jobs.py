"""
Module to define jobs (background/blocking)
"""
from price_tracker.fetch_crypto_price import FetchPriceCryptoCoinGecko
from price_tracker.models import PriceTracker
from django.utils.timezone import now as utcnow


def fetch_save_crypto_price(coin: str, price_currency: str) -> None:
    """
    Fetches crypto price and saves in the database
    Args:
        coin (str): supported coin for which price needs to be fetched
        price_currency (str): currency in which price needs to be fetched
    Returns:
    """
    try:
        print("fetch_price_coin_periodic started...")
        # Fetch Price Date
        fetch_price_crypto = FetchPriceCryptoCoinGecko(coin, price_currency)
        price_res = fetch_price_crypto.fetch_price()
        # Save Price Data in database
        price_tracker = PriceTracker()
        price_tracker.coin = coin
        price_tracker.price = price_res[coin][price_currency]
        price_tracker.currency = price_currency
        # Since timestamp is not returned from API, adding the timestamp
        # as soon as response is received
        price_tracker.timestamp = utcnow()
        price_tracker.save()
        print("fetch_price_coin_periodic completed!")
    # Log error in case of any exception
    except Exception as err:
        print("Error occurred while fetching and saving crypto price", err)
