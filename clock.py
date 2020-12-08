from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', seconds=2, id='my_job')
def my_job():
    print('This job runs every other second')

@scheduler.scheduled_job('date', run_date=datetime.now() + timedelta(seconds=10))
def reschedule_my_job():
    print('Reschedule job to every 5 seconds')
    scheduler.reschedule_job('my_job', trigger='interval', seconds=5)

scheduler.start()