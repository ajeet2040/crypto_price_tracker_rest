from crypto_price_tracker_rest.settings import env

# Internal Configs
CRYPTOS_TO_BE_TRACKED = {
    'coins': [('btc', 'bitcoin')],  # list of coin name and id of coin for coin gecko
    'currencies': 'usd'  # comma separated currencies without space as required
}

# Min and Max Price limit to trigger emails
MIN_PRICE_USD = env('min')
MAX_PRICE_USD = env('max')

# SMTP Configs
EMAIL_HOST = env('host')
EMAIL_HOST_USER = env('username')
EMAIL_HOST_PASSWORD = env('password')
EMAIL_PORT = env('port')

# TEST sender and receiver for Mailtrap
SENDER = "Private Person <ajeet@example.com>"
RECEIVER = env('email')
