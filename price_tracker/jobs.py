"""
Module to define jobs (background/blocking)
"""
from price_tracker.fetch_crypto_price import FetchPriceCryptoCoinGecko
from price_tracker.models import PriceTracker
from django.utils.timezone import now as utcnow
from price_tracker.config import CRYPTOS_TO_BE_TRACKED, SENDER, RECEIVER, MIN_PRICE_USD, MAX_PRICE_USD, logger
from price_tracker.utils import send_email


def send_email_bitcoin_trigger(bitcoin_usd_price: float) -> None:
    """
    Send Email if trigger(min and max limit) satisfies for coin 'bitcoin'
    Args:
        bitcoin_usd_price (float): USD price of bitcoin
    Returns: None

    """
    subject = None
    message = None
    if bitcoin_usd_price < MIN_PRICE_USD:
        subject = "Bitcoin Price Drop Alert!"
        message = f"Bitcoin Price has dropped to '{bitcoin_usd_price}'!"
    if bitcoin_usd_price > MAX_PRICE_USD:
        subject = "Bitcoin Price Rise Alert!"
        message = f"Bitcoin Price has raised to '{bitcoin_usd_price}'!"
    if subject is not None:
        send_email(SENDER, RECEIVER, subject, message)


def fetch_save_crypto_price() -> None:
    """
    Fetches price for cryptos as per the 'CRYPTOS_TO_BE_TRACKED' config and saves in the database
    Returns: None
    """
    try:
        logger.info("Fetch and Store Price of Crypto process started...")
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
        logger.info("Fetch and Store Price of Crypto process completed successfully !")
        send_email_bitcoin_trigger(price_res["bitcoin"]["usd"])
    # Log error in case of any exception
    except Exception as err:
        logger.error("Error occurred while fetching and saving crypto price. Error is %s" % err)
