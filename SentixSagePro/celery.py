from __future__ import absolute_import ,unicode_literals

import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SentixSagePro.settings')
app = Celery('SentixSagePro')
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'test_func': {
        'task': 'Data.task.test_func',
        'schedule': crontab(hour=15, minute=24),
    },
    'collect-daily-data': {

        'task': 'Data.task.collect_daily_data',
        'schedule': crontab(hour=15, minute=41),
    },

}




