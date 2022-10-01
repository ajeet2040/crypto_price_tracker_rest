"""Module to define any utility methods"""
from datetime import datetime


def generate_date(date_text: str, date_format: str) -> datetime.date:
    """
    Generate and return python date object.
    Args:
        date_text (str): date in string.
        date_format (str): format in which the date is expected.
    Returns:
        python date object.
    """
    try:
        return datetime.strptime(date_text, date_format).date()
    except ValueError:
        raise ValueError(f"Incorrect date format.Format should be {date_format}")
