import requests

from django.core.management.base import BaseCommand
from django.conf import settings
from assets.models import Asset

class Command(BaseCommand):
    help = 'Update the current price for all tracked assets'

    def handle(self, *args, **options):
        for asset in Asset.objects.all():
            response = requests.get(
                'https://api.hgbrasil.com/finance/stock_price?' +
                f'key={settings.HG_API_KEY}&symbol={asset.symbol}')

            if not response.ok:
                self.stdout.write(self.style.ERROR(
                    f'Request error: {response.text()}'))
                continue

            results = response.json().get('results')

            if 'error' in results:
                self.stdout.write(self.style.ERROR(
                    f'Invalid symbol error: {results.get("message")}'))
                continue

            symbol_data = results.get(asset.symbol)

            if 'error' in symbol_data:
                self.stdout.write(self.style.ERROR(
                    f'Symbol not found: {symbol_data.get("message")}'))
                continue

            price = symbol_data.get('price')
            asset.current_price = price
            asset.save()
            self.stdout.write(self.style.SUCCESS(
                f'Current price updated for {asset.symbol}: {price:.2f}'))
