"""
Module to define jobs (background/blocking)
"""
from price_tracker.fetch_crypto_price import FetchPriceCryptoCoinGecko
from price_tracker.models import PriceTracker
from django.utils.timezone import now as utcnow
from price_tracker.config import CRYPTOS_TO_BE_TRACKED


def fetch_save_crypto_price() -> None:
    """
    Fetches price for cryptos as per the 'CRYPTOS_TO_BE_TRACKED' config and saves in the database
    Returns:
    """
    try:
        print("fetch_price_coin_periodic started...")
        coins = [x[1] for x in CRYPTOS_TO_BE_TRACKED['coins']]
        coins = ','.join(coins)
        # Fetch Price Date
        fetch_price_crypto = FetchPriceCryptoCoinGecko(coins, CRYPTOS_TO_BE_TRACKED['currencies'])
        price_res = fetch_price_crypto.fetch_price()
        # Save Price Data in database

        for coin, value in price_res.items():
            coin = next(x[0] for x in CRYPTOS_TO_BE_TRACKED['coins'] if x[1] == coin)
            for curr, price in value.items():
                price_tracker = PriceTracker()
                price_tracker.coin = coin
                price_tracker.currency = curr
                price_tracker.price = price
                # Since timestamp is not returned from API, adding the timestamp
                # as soon as response is received
                price_tracker.timestamp = utcnow()
                price_tracker.save()
        print("fetch_price_coin_periodic completed!")
    # Log error in case of any exception
    except Exception as err:
        print("Error occurred while fetching and saving crypto price", err)
