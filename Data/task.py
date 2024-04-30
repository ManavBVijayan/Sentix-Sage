from celery import shared_task
from .stock_data import collect_stock_data


@shared_task()
def collect_daily_data():
    collect_stock_data('AAPl')
