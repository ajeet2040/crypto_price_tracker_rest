"""Module to schedule jobs"""
from price_tracker.jobs import fetch_save_crypto_price
from apscheduler.schedulers.background import BackgroundScheduler


def start_job():
    """
        Starts specified jobs using 'apscheduler' library.
    """
    # NOTE: Does not handle exceptions based on assumption to crash if job fails to schedule
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_save_crypto_price, 'interval', ['bitcoin', 'inr'], seconds=30)
    scheduler.start()
