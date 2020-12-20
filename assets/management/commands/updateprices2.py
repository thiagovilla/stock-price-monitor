from django.core.management.base import BaseCommand
from django.conf import settings
from assets.jobs import update_prices

from rq import Queue
from worker import conn


class Command(BaseCommand):
    help = 'Enqueue a job update the current price for all tracked assets'

    def handle(self, *args, **options):
        q = Queue(connection=conn)
        q.enqueue(update_prices)
