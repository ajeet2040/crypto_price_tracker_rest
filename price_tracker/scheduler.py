"""Module to schedule jobs"""
from price_tracker.jobs import fetch_save_crypto_price
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from price_tracker.config import INTERVAL_IN_SECONDS

def start_job() -> None:
    """
        Starts specified jobs using 'apscheduler' library.
    """
    # NOTE: Does not handle exceptions based on assumption to crash if job fails to schedule
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_save_crypto_price, 'interval', seconds=INTERVAL_IN_SECONDS)
    scheduler.start()

