from celery import shared_task
from .stock_data import collect_stock_data
import logging

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def test_func(self):
    try:
        result = "Task executed successfully"
        logging.info(result)  # Log success message
        return result
    except Exception as e:
        error_msg = f"An error occurred: {e}"
        logging.error(error_msg)  # Log error message
        return error_msg

@shared_task(bind=True)
def collect_daily_data(self):
    logger.info('Starting daily data collection task')
    try:
        collect_stock_data('AAPL')  # Assuming AAPL is the stock symbol
        logger.info('Daily data collection task completed successfully')
    except Exception as e:
        logger.error(f"An error occurred during daily data collection: {e}")



