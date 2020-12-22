import os
from datetime import datetime, timedelta

from apscheduler.schedulers.blocking import BlockingScheduler
from django.utils.dateparse import parse_duration
from rq import Queue

from worker import conn
from assets.jobs import update_prices

scheduler = BlockingScheduler()

seconds = parse_duration(
    os.getenv('UPDATE_PRICES_INTERVAL', 'P0DT1H')).total_seconds()

q = Queue(connection=conn)


@scheduler.scheduled_job('interval', seconds=seconds, id='update_prices_job')
def update_prices_job():
    q.enqueue(update_prices)
    print('update_prices job sent to worker queue')


scheduler.start()
