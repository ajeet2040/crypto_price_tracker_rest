"""
Module that fetches coin prices in desired formats from third party API.
"""
import requests


class FetchPriceCryptoCoinGecko:
    """
    Module that fetches coin prices in desired formats from third party API.
    """
    price_url = "https://api.coingecko.com/api/v3/simple/price"

    def __init__(self, coins: str, price_currencies: str) -> None:
        """
        Constructor for FetchPriceCrypto
        Args:
            coins (str): coins for which price needs to be fetched
            price_currencies (str): currencies in which price needs to be fetched
        """
        self.coins = coins
        self.price_currencies = price_currencies

    def fetch_price(self) -> dict:
        """
        Fetches price of the coin in desired currency.
        Returns: (dict) response data.
        """
        params = {
            "ids": self.coins,
            "vs_currencies": self.price_currencies
        }
        try:
            res = requests.get(self.price_url, params=params)
            res.raise_for_status()
            print(res)
            return res.json()
        except requests.exceptions.HTTPError as err:
            print("HTTP error occurred", err)
            raise err
