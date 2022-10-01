"""
Module that fetches coin prices in desired formats from third party API.
"""
import requests


class FetchPriceCryptoCoinGecko:
    """
    Module that fetches coin prices in desired formats from third party API.
    """
    price_url = "https://api.coingecko.com/api/v3/simple/price"

    def __init__(self, coin: str, price_currency: str) -> None:
        """
        Constructor for FetchPriceCrypto
        Args:
            coin (str): supported coin for which price needs to be fetched
            price_currency (str): currency in which price needs to be fetched
        """
        self.coin = coin
        self.price_currency = price_currency

    def fetch_price(self) -> dict:
        """
        Fetches price of the coin in desired currency.
        Returns: (dict) response data.
        """
        params = {
            "ids": self.coin,
            "vs_currencies": self.price_currency
        }
        try:
            res = requests.get(self.price_url, params=params)
            res.raise_for_status()
            print(res)
            return res.json()
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred", err)
            raise err
