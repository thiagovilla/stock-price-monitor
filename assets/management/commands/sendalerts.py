from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from assets.models import Asset


class Command(BaseCommand):
    help = 'Send buy/sell alert emails for tracked assets'

    def handle(self, *args, **options):
        for asset in Asset.objects.all():
            if asset.lower_limit < asset.current_price < asset.upper_limit:
                continue

            subject = ''
            message = f'Current price for {asset.symbol} is {asset.current_price}, '

            if asset.current_price < asset.lower_limit:
                subject = f'Buy {asset.symbol} now'
                message += f'which is below your defined lower limit of {asset.lower_limit}'

            if asset.current_price > asset.upper_limit:
                subject = f'Sell {asset.symbol} now'
                message += f'which is above your defined upper limit of {asset.upper_limit}'

            send_mail(
                subject,
                message,
                'no-reply@example.com',
                ['user@example.com'],
                fail_silently=False
            )
