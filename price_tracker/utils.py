"""Module to define any utility methods"""
from datetime import datetime
import smtplib
from price_tracker.config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, logger


def send_email(sender, receiver, subject, message):
    message_body = f"""\
        Subject: {subject}
        To: {receiver}
        From: {sender}
        {message}"""
    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            logger.info("Sending Email through mailtrap to user %s" % receiver)
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(sender, receiver, message_body)
            logger.info("Email through mailtrap sent successfully!")
    except Exception as err:
        logger.error(f"Error occurred while sending email: {err}")


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
