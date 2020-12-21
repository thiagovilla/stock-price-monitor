from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from assets.models import TrackedAsset


class Command(BaseCommand):
    help = 'Send buy/sell alert emails for tracked assets'

    def handle(self, *args, **options):
        for tracked_asset in TrackedAsset.objects.all():
            asset = tracked_asset.asset

            if tracked_asset.lower_limit < asset.current_price < tracked_asset.upper_limit:
                continue

            subject = ''
            message = f'Current price for {asset.symbol} is {asset.current_price}, '

            if asset.current_price < tracked_asset.lower_limit:
                subject = f'Buy {asset.symbol} now'
                message += f'which is below your defined lower limit of {tracked_asset.lower_limit}'

            if asset.current_price > tracked_asset.upper_limit:
                subject = f'Sell {asset.symbol} now'
                message += f'which is above your defined upper limit of {tracked_asset.upper_limit}'

            send_mail(
                subject,
                message,
                'no-reply@example.com',
                ['user@example.com'],
                fail_silently=False
            )
